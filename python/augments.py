import re
import sys

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@gmail\.com$")
clusters = ["cluster1", "cluster2"]
selected_clusters = set()
selected_email = ""
aug_state = True

def valid_email(email):
    global selected_email
    if EMAIL_REGEX.match(email):
        selected_email = email
        return email
    print(f"❌ '{email}' is not a valid Gmail address.")
    return None

def choose_cluster(cluster):
    if cluster in clusters:
        print(f"✅ You chose cluster '{cluster}'")
        selected_clusters.add(cluster)
    else:
        print(f"❌ '{cluster}' is not valid.")

def quit_program():
    print("👋 Exiting.")
    sys.exit(0)

def continue_execution():
    global aug_state
    if not selected_clusters:
        print("❌ Please select at least one cluster before continuing.")
        return
    # Otherwise proceed:
    print(f"\n🚀 Proceeding with:")
    print(f"  Email   : {selected_email}")
    print(f"  Selected Clusters: {sorted(selected_clusters)}")
    # Add your next steps here...
    aug_state = False

def main():
    email = None
    while not email:
        user_input = input("Enter your Gmail address: ").strip()
        email = valid_email(user_input)

    # Dispatch table with both numbers and names
    actions = {
        "1": ("cluster1", lambda: choose_cluster("cluster1")),
        "2": ("cluster2", lambda: choose_cluster("cluster2")),
        "cluster1": ("cluster1", lambda: choose_cluster("cluster1")),
        "cluster2": ("cluster2", lambda: choose_cluster("cluster2")),
        "q": ("Quit", quit_program),
        "quit": ("Quit", quit_program),
        "c": ("continue", continue_execution),
        "continue": ("continue", continue_execution),
    }

    while aug_state:
        print("\nChoose an option:")
        for key, (label, _) in sorted(actions.items()):
            if key.isdigit():
                print(f"{key}. {label}")
        print("c. Continue")
        print("q. Quit")

        choice = input("Your choice: ").strip().lower()
        action = actions.get(choice)
        if action:
            _, func = action
            func()
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
