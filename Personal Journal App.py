from datetime import datetime

FILE_NAME = "journal.txt"

while True:
    print("\n=== Personal Journal App ===")
    print("1. Add Entry")
    print("2. View Journal")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        entry = input("Write your journal entry: ")

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(FILE_NAME, "a") as file:
            file.write(f"\n[{current_time}]\n")
            file.write(entry + "\n")
            file.write("-" * 40 + "\n")

        print("Entry saved successfully!")

    elif choice == "2":
        try:
            with open(FILE_NAME, "r") as file:
                content = file.read()

                if content.strip():
                    print("\n=== Your Journal ===")
                    print(content)
                else:
                    print("Journal is empty.")

        except FileNotFoundError:
            print("No journal entries found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")