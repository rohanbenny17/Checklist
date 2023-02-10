from colorama import Fore, Style
import sys
import os


def main():
    # Check for correct number of arguments
    if count(len(sys.argv)) == 1:
        print(Fore.RED, Style.BRIGHT + "Error: Invalid usage")
        print(Style.RESET_ALL, end="")
        help()

    # Call help
    if sys.argv[1] == "--help":
        help()

    # Check for correct number of arguments
    if count(len(sys.argv)) < 3:
        print(Fore.RED, Style.BRIGHT + "Error: Invalid usage")
        print(Style.RESET_ALL, end="")
        help()

    # Option_1 is the option names having no arguments
    # Option_2 is the option name having one or more argument
    option_1 = ["--ls", "--help", "--delete"]
    option_2 = ["--add", "--rm"]

    # Check if profile name is one of the option names
    if sys.argv[1] in option_2 + option_1:
        print(Fore.RED, Style.BRIGHT + f'Error: Cannot use an option name as profile name: "{sys.argv[1]}"')
        print(Style.RESET_ALL, end="")
        print('Use: "python checklist.py --help" for help')
        sys.exit()

    # Check if option value is valid
    if sys.argv[2] in option_1 + option_2:
        # Check if the option selected has the correct number of arguments
        if sys.argv[2] in option_1 and len(sys.argv) != 3:
            print(Fore.RED, Style.BRIGHT + f"Error: {sys.argv[2]} must not have any argument")
            print(Style.RESET_ALL, end="")
            print('Use: "python checklist.py --help" for help')
            sys.exit()
    # Option value is not valid
    else:
        print(Fore.RED, Style.BRIGHT + f"Error: {sys.argv[2]} not a valid option")
        print(Style.RESET_ALL, end="")
        help()

    # Corresponding option value functions
    match (sys.argv[2]):
        case "--add":
            n = count_add(len(sys.argv))
            add(n)

        case "--rm":
            n = count_rm(len(sys.argv))
            remove(n)

        case "--ls":
            list_items()

        case "--help":
            help()

        case "--delete":
            delete()

        case _:
            print(Fore.RED, Style.BRIGHT + f"Error: {sys.argv[2]} not a valid option")
            print(Style.RESET_ALL, end="")
            help()


# Help menu
def help():
    print(Fore.BLUE, end="")
    try:
        with open("data/help.txt") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(Fore.YELLOW + "Unexpected error: Data File is missing")
        print(Style.RESET_ALL, end="")
    print(Style.RESET_ALL, end="")

    sys.exit()


# Add an item to list
def add(n):
    # Get the profile name
    profile = sys.argv[1]

    # Get the items present in the to-do list
    items = []
    try:
        with open(f"data/{profile}.txt") as file:
            for line in file:
                items.append(line.rstrip())
    except FileNotFoundError:
        pass

    args = []
    # Get  all the arguments
    for i in range(n + 1):
        args.append(sys.argv[i + 3])

    for item in args:
        # Check if item already present in the to-do list
        # Prompt the user if the item is to be added
        if item in items:
            print(Fore.YELLOW + f'"{item}" already present in the to-do list')
            print(Fore.GREEN + "Are you sure you want to add the item (Y/N): ", end="")
            print(Style.RESET_ALL, end="")
            choice = input().strip()

            if choice.lower() in ["n", "no"]:
                sys.exit()

        try:
            # Write the item into the to-do list
            with open(f"data/{profile}.txt", "a") as file:
                file.write(f"{item}\n")
        except FileNotFoundError:
            print(Fore.YELLOW + "An unexpected error has occured")
            print(Style.RESET_ALL, end="")

    sys.exit()


# Remove an item from list
def remove(n):
    # Get the profile name
    profile = sys.argv[1]

    # Get the items present in the to-do list
    items = []
    try:
        with open(f"data/{profile}.txt") as file:
            for line in file:
                items.append(line.rstrip())
    except FileNotFoundError:
        print(Fore.RED, Style.BRIGHT + "Error: Profile doesn't exist")
        print(Style.RESET_ALL, end="")
        sys.exit()

    args = []
    # Get  all the arguments
    for i in range(n):
        args.append(sys.argv[i + 3])

    for item in args:
        # Check if item is present in the to-do list
        # Delete the item if present
        if item in items:
            i = items.index(item)
            items.pop(i)

            try:
                with open(f"data/{profile}.txt", "w") as file:
                    for i in items:
                        file.write(f"{i}\n")
            except FileNotFoundError:
                print(Fore.YELLOW + "An unexpected error has occured")
                print(Style.RESET_ALL, end="")

        # Item not present in the to-do list
        else:
            print(Fore.YELLOW + f'"{item}" not in the to-do list')
            print(Style.RESET_ALL, end="")

    sys.exit()


# List items
def list_items():
    # Get the profile name
    profile = sys.argv[1]

    try:
        # Print the items present in the to-do list
        with open(f"data/{profile}.txt") as file:
            print()
            for line in file:
                print(line, end="")
            print()
    except FileNotFoundError:
        print(Fore.RED, Style.BRIGHT + "Error: Profile doesn't exist")
        print(Style.RESET_ALL, end="")

    sys.exit()


# Delete a profile
def delete():
    # Get the profile name
    profile = sys.argv[1]

    # File path
    file_path = f"data/{profile}.txt"

    # Check if file exist
    # Delete the file
    if os.path.exists(file_path):
        os.remove(file_path)
        print(Fore.GREEN + f"Profile: {profile} has been deleted")
        print(Style.RESET_ALL, end="")
    else:
        print(Fore.RED, Style.BRIGHT + "Error: Profile doesn't exist")
        print(Style.RESET_ALL, end="")

    sys.exit()


# Count for add()
def count_add(x):
    return x - 4


# Count for remove()
def count_rm(x):
    return x - 3


# Count
def count(x):
    return x


# Call the main
if __name__ == "__main__":
    main()
