import re
import sys

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

def valid_email(email):
    if EMAIL_REGEX.match(email):
        return email
    else:
        print(f"❌ '{email}' is not valid.")
        return None

def option1():
    print("✅ You chose OPTION 1")

def option2():
    print("✅ You chose OPTION 2")

def quit_program():
    print("👋 Exiting.")
    sys.exit(0)

def main():
    # Get a valid email
    email = None
    while not email:
        user_input = input("Enter your email: ").strip()
        email = valid_email(user_input)

    # Define options
    options = {
        "1": ("Option 1", option1),
        "2": ("Option 2", option2),
        "option1": ("Option 1", option1),
        "option2": ("Option 2", option2),
        "q": ("Quit", quit_program),
        "quit": ("Quit", quit_program),
    }

    # Interactive menu
    while True:
        print("\nChoose an option:")
        for key, (label, _) in sorted(options.items()):
            if key.isdigit():
                print(f"{key}. {label}")
        print("q. Quit")

        choice = input("Your choice: ").strip().lower()
        action = options.get(choice)
        if action:
            _, func = action
            func()
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
