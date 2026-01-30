import time
from pprint import pformat
from textwrap import dedent
import streamlit as st
from agno.team import Team

from k8s_agent.agent.agent_model import AgentModel
from k8s_agent.agent.agent import k8s_agent
from agno.db.sqlite import SqliteDb

# -------------------------------------------------------------------
# Model setup
# -------------------------------------------------------------------
agent_model = AgentModel()
model = agent_model.ollama_client()
model_name = getattr(model, "model", "unknown")
db = SqliteDb(db_file="/tmp/agent.db")


# -------------------------------------------------------------------
# Team initialization
# -------------------------------------------------------------------
def initialize_team():
    return Team(
        id="k8s_team",
        name="K8s Team",
        description="A team of agents that can help with Kubernetes related questions",
        model=model,
        members=[k8s_agent],
        markdown=True,
        db=db,
        add_history_to_context=True, # simple history
        num_history_runs=5,  # max history chat
        read_chat_history=True,   # Agent decides when to look up
        role=dedent("""
Role: Kubernetes Diagnostic Expert 🧠

You are an expert Kubernetes assistant capable of managing and diagnosing clusters with precision.  
You have access to the **K8sFullResourceReader** tool that can:
- List all resources.
- Detect unusual resources (crashing pods, pending PVCs, failed deployments, etc.).
- Fetch YAML manifests for specific resources.

Follow this diagnostic workflow:
1. When the user asks to *check the cluster*, start by running `detect_unusual_resources()`.
2. If anomalies are found, automatically call `get_resource_yaml()` for each one.
3. Examine the YAML for potential causes (e.g., imagePullBackOff, wrong selector, resource limits).
4. Suggest clear remediation steps with sample `kubectl` commands or YAML patches.
5. When listing resources, use `list_all_resources()` and summarize the output.
6. Always respond in a structured, step-by-step, and explanatory manner.

Example prompts you handle:
- “Check what’s wrong with my pods.”
- “Show all deployments in my cluster.”
- “Find and analyze any failed resources.”
- “Fetch the YAML for pod nginx-xyz in namespace prod.”

"""),
    )


# -------------------------------------------------------------------
# Session state initialization (CRITICAL)
# -------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "team" not in st.session_state:
    st.session_state.team = initialize_team()

if "team_session_id" not in st.session_state:
    st.session_state.team_session_id = f"streamlit-team-session-{int(time.time())}"


# -------------------------------------------------------------------
# UI
# -------------------------------------------------------------------
st.title("🤖 Research Assistant Team")
st.markdown("""
This team coordinates specialists to assist with:
- Kubernetes
""")


# -------------------------------------------------------------------
# Display chat history
# -------------------------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -------------------------------------------------------------------
# Chat input
# -------------------------------------------------------------------
user_query = st.chat_input("Ask the k8s team anything...")

if user_query:
    # Store user message
    st.session_state.messages.append(
        {"role": "user", "content": user_query}
    )

    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            # ------------------------------------------------
            # STREAMING RESPONSE (NO RunResponse import)
            # ------------------------------------------------
            response_stream = st.session_state.team.run(
                user_query,
                stream=True
            )

            for chunk in response_stream:
                # Only rely on the stable contract: chunk.content
                if hasattr(chunk, "content") and isinstance(chunk.content, str):
                    full_response += chunk.content
                    message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)

            # ------------------------------------------------
            # Optional memory debug
            # ------------------------------------------------
            if hasattr(st.session_state.team, "memory") and hasattr(
                st.session_state.team.memory, "messages"
            ):
                st.session_state.memory_dump = [
                    {
                        "role": getattr(m, "role", "unknown"),
                        "content": getattr(m, "content", str(m)),
                    }
                    for m in st.session_state.team.memory.messages
                ]

            # Save assistant response
            st.session_state.messages.append(
                {"role": "assistant", "content": full_response}
            )

        except Exception as e:
            st.exception(e)
            error_message = f"An error occurred: {e}"
            st.error(error_message)
            st.session_state.messages.append(
                {"role": "assistant", "content": error_message}
            )


# -------------------------------------------------------------------
# Sidebar
# -------------------------------------------------------------------
with st.sidebar:
    st.title("Team Settings")

    if st.checkbox("Show Team Memory Contents", value=False):
        st.subheader("Team Memory Contents (Debug)")
        if "memory_dump" in st.session_state:
            st.code(
                pformat(st.session_state.memory_dump, indent=2),
                language="python",
            )
        else:
            st.info("No memory contents yet.")

    st.markdown(f"**Session ID**: `{st.session_state.team_session_id}`")
    st.markdown(f"**Model**: `{model_name}`")

    st.subheader("Team Memory")
    st.markdown(
        "This team remembers conversations within this browser session."
    )

    if st.button("Clear Chat & Reset Team"):
        st.session_state.messages = []
        st.session_state.team = initialize_team()
        st.session_state.team_session_id = (
            f"streamlit-team-session-{int(time.time())}"
        )
        st.session_state.pop("memory_dump", None)
        st.rerun()

    st.title("About")
    st.markdown("""
**Examples**:
- Check what’s wrong with my pods  
- Show all deployments in my cluster  
- Find failed resources  
- Fetch YAML for pod nginx-xyz in prod  
""")
