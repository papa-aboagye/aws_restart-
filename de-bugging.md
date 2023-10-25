
import subprocess
import getpass

def new_user():
    # Prompt for a username
    username = input("Enter the name of the user to add: ")

    # Ask for confirmation
    confirm = input(f"Use the username '{username}'? (Y/N)").strip().upper()
    if confirm != "Y":
        return

    # Use subprocess to run the adduser command with sudo
    command = f"sudo adduser {username}"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    else:
        print(f"User '{username}' added successfully.")

def remove_user():
    # Prompt for a username
    username = input("Enter the name of the user to remove: ")

    # Ask for confirmation
    confirm = input(f"Remove the user: '{username}'? (Y/N)").strip().upper()
    if confirm != "Y":
        return

    # Use subprocess to run the userdel command with sudo
    command = f"sudo userdel -r {username}"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    else:
        print(f"User '{username}' removed successfully.")

def add_user_to_group():
    username = input("Enter the name of the user that you want to add to a group: ")
    
    # Use subprocess to get the list of groups
    output = subprocess.getoutput('groups')
    available_groups = output.split()
    
    print("Enter a list of groups to add the user to")
    print("The list should be separated by spaces, for example: group1 group2 group3")
    print("The available groups are:")
    print("\n".join(available_groups))
    
    # Prompt for the groups to add the user to
    chosen_groups = input("Groups: ").strip().split()
    
    # Check if the chosen groups are valid
    invalid_groups = [group for group in chosen_groups if group not in available_groups]
    if invalid_groups:
        print(f"Invalid group(s): {', '.join(invalid_groups)}")
        return
    
    # Use subprocess to add the user to the chosen groups
    for group in chosen_groups:
        command = f"sudo usermod -a -G {group} {username}"
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
        else:
            print(f"User '{username}' added to group '{group}' successfully.")



new_user()
add_user_to_group()
remove_user()