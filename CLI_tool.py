from datetime import datetime

print("1. Add Journal Entry")
print("2. View Journal Entries")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    entry = input("Write your journal entry: ")

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file = open("journal.txt", "a")
    file.write(f"\n[{date}] {entry}")
    file.close()

    print("Journal entry saved!")

elif choice == "2":
    try:
        file = open("journal.txt", "r")
        content = file.read()
        file.close()

        print("\n--- Journal Entries ---")
        print(content)

    except FileNotFoundError:
        print("No journal entries found.")

else:
    print("Invalid choice!")