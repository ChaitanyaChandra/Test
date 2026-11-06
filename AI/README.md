# AI Infrastructure

Self-hosted AI infrastructure running on Kubernetes.

| Service | Host | Purpose |
|---------|------|---------|
| **OmniRoute** | `https://omni.chaitu.net` | AI gateway — multi-provider LLM routing |
| **ClaudeMem** | `https://claudemem.chaitu.net` | Persistent memory MCP server |

---

## OmniRoute

Multi-provider AI gateway supporting OpenAI, Anthropic, Gemini, and 100+ other providers.

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {},
  "apiBaseUrl": "https://omni.chaitu.net"
}
```

Or configure per-provider by pointing any OpenAI-compatible client to:
```
Base URL:  https://omni.chaitu.net
API Key:   <key generated from OmniRoute dashboard>
```

### Claude Code

```bash
claude config set apiBaseUrl https://omni.chaitu.net
```

Or set the environment variable:

```bash
export ANTHROPIC_BASE_URL=https://omni.chaitu.net
claude
```

---

## ClaudeMem (MCP Memory Server)

Persistent knowledge graph memory across Claude sessions, powered by [`@modelcontextprotocol/server-memory`](https://github.com/modelcontextprotocol/servers/tree/main/src/memory).

### Endpoints

| Endpoint | URL |
|----------|-----|
| SSE (connect) | `https://claudemem.chaitu.net/sse` |
| Messages (POST) | `https://claudemem.chaitu.net/message` |

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "memory": {
      "url": "https://claudemem.chaitu.net/sse"
    }
  }
}
```

Then restart Claude Desktop. You should see **memory** listed under MCP servers in Settings → Developer.

### Claude Code

```bash
claude mcp add memory --transport sse https://claudemem.chaitu.net/sse
```

Verify it's connected:

```bash
claude mcp list
```

### Available Memory Tools

Once connected, Claude will have access to these tools:

| Tool | Description |
|------|-------------|
| `create_entities` | Create named entities in the knowledge graph |
| `create_relations` | Link entities with typed relationships |
| `add_observations` | Add facts/observations to existing entities |
| `search_nodes` | Search the knowledge graph by query |
| `open_nodes` | Retrieve specific entities by name |
| `delete_entities` | Remove entities from the graph |
| `delete_relations` | Remove relationships |

### Example Usage

Once connected, you can ask Claude things like:
- *"Remember that my project uses PostgreSQL 15 and is deployed on k3s"*
- *"What do you remember about my infrastructure setup?"*
- *"Forget the old API key I told you about"*

---

## Deploying / Updating

```bash
# Apply all manifests
kubectl apply -f OmniRoute/
kubectl apply -f ClaudeMem/

# Check status
kubectl get po -n omni
kubectl get po -n claudemem
```

## Directory Structure

```
AI/
├── README.md
├── OmniRoute/
│   ├── deployment.yaml   # OmniRoute app + PVC + Secret
│   ├── service.yaml      # ClusterIP :443 → :20128
│   └── ingress.yaml      # omni.chaitu.net
└── ClaudeMem/
    ├── deployment.yaml   # supergateway + mcp/memory + PVC
    ├── service.yaml      # ClusterIP :80 → :3000
    └── ingress.yaml      # claudemem.chaitu.net
```

