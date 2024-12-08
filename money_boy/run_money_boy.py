import cli
import gui

if __name__ == "__main__":
    while True:
        print()
        print("Choose an option:")
        print("1) Run CLI")
        print("2) Run GUI")
        print("Type 'exit' to quit")

        user_choice = input("Enter choice: ").strip().lower()

        if user_choice == "1":
            cli.run()
        elif user_choice == "2":
            gui.run()
        elif user_choice == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
