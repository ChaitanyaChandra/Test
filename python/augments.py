import re
import sys

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@gmail\.com$")
all_clusters = ["prdusr001", "prdusr001", "nonprd001", "nonprd101"]
prod_clusters = ["prdusr001", "prdusr001"]
non_prod_clusters = ["nonprd001", "nonprd101"]
selected_clusters = set()
selected_email = ""
aug_state = True

def valid_email(email):
    global selected_email
    if EMAIL_REGEX.match(email):
        selected_email = email
        return email
    print(f"❌ '{email}' is not a valid gmail email address.")
    return None

def choose_cluster():
    global selected_clusters

    while True:
        cluster_input = input("\nEnter a cluster alias (or type 'c' to continue, 'q' to quit): ").strip().lower()

        if cluster_input == 'c' or cluster_input == 'continue':
            continue_execution(None)
            break
        elif cluster_input == 'q':
            quit_program()
        elif cluster_input in all_clusters:
            selected_clusters.add(cluster_input)
            print(f"✅ You have chosen cluster '{cluster_input}'")
            print(f"selected clusters '{sorted(selected_clusters)}'")
        else:
            print(f"❌ '{cluster_input}' is not valid.")
            print(f"valid clusters are :\n{all_clusters}")

def quit_program():
    print("👋 Exiting.")
    sys.exit(0)

def continue_execution(cluster_type):
    global aug_state
    global selected_clusters
    if cluster_type ==  "prod_clusters":
        selected_clusters.update(prod_clusters)
    elif cluster_type ==  "non_prod_clusters":
        selected_clusters.update(non_prod_clusters)
    else:
        pass

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
        user_input = input("Enter your email address: ").strip()
        email = valid_email(user_input)

    # Dispatch table with both numbers and names
    actions = {
        "1": ("ALL PROD clusters", lambda: continue_execution("prod_clusters")),
        "2": ("ALL NON PROD clusters", lambda: continue_execution("non_prod_clusters")),
        "3": ("Enter cluster alias manually ??", lambda: choose_cluster()),
        "q": ("Quit", quit_program),
        "quit": ("Quit", quit_program),
        "c": ("continue", lambda: continue_execution(None)),
        "continue": ("continue", lambda: continue_execution(None)),
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
