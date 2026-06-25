#!/usr/bin/env python3
"""
Personal Journal App
---------------------
A simple command-line journal that demonstrates Python file handling.

Features:
  - Add a new dated entry to journal.txt (append mode)
  - View all past entries (read mode)

Usage:
    python journal.py add "Today I learned about file handling in Python."
    python journal.py add            (prompts for multi-line entry input)
    python journal.py view
    python journal.py                (interactive menu)
"""

import argparse
import os
from datetime import datetime

JOURNAL_FILE = "journal.txt"
SEPARATOR = "-" * 50


def add_entry(text=None):
    """Append a new dated entry to the journal file."""
    if text is None:
        print("Write your journal entry below.")
        print("Press ENTER on an empty line when you're done.\n")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        text = "\n".join(lines).strip()

    if not text:
        print("Empty entry — nothing was saved.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # "a" = append mode: adds to the end of the file without
    # erasing existing content. Creates the file if it doesn't exist.
    with open(JOURNAL_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}]\n")
        f.write(f"{text}\n")
        f.write(f"{SEPARATOR}\n")

    print(f"\nEntry saved to {JOURNAL_FILE} at {timestamp}.")


def view_entries():
    """Read and display all past journal entries."""
    if not os.path.exists(JOURNAL_FILE) or os.path.getsize(JOURNAL_FILE) == 0:
        print("No journal entries yet. Use 'add' to write your first one!")
        return

    # "r" = read mode: opens the file for reading only.
    with open(JOURNAL_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    print("\n" + "=" * 50)
    print("YOUR JOURNAL ENTRIES")
    print("=" * 50 + "\n")
    print(content)


def interactive_menu():
    """Simple text menu for when the script is run with no arguments."""
    while True:
        print("\n=== Personal Journal ===")
        print("1. Add a new entry")
        print("2. View all entries")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def main():
    parser = argparse.ArgumentParser(description="Personal Journal CLI App")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new journal entry")
    add_parser.add_argument(
        "text", nargs="?", default=None,
        help="Entry text (if omitted, you'll be prompted to type it)"
    )

    subparsers.add_parser("view", help="View all past journal entries")

    args = parser.parse_args()

    if args.command == "add":
        add_entry(args.text)
    elif args.command == "view":
        view_entries()
    else:
        interactive_menu()


if __name__ == "__main__":
    main()