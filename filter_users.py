'''
This module provides functions to filter users based on their name, age, or email.
The users are stored in a JSON file named "users.json". The module includes functions to filter users by name, age, and email, as well as a helper function to print the filtered results in a standardized format.
No specific main-Function is defined, the main program logic is executed in the if __name__ == "__main__": block.
No Exception-Handling is implemented, so it is assumed that the "users.json" file exists and is properly formatted, and that user input is valid.
'''

import json


def print_filtered_users(filtered_users: list, filter_type: str, filter_value: str):
    '''
    Standardfunction to print filtered users based on the filter type and value.
    :param filtered_users: List of users that match the filter criteria.
    :param filter_type: The type of filter applied (e.g., "name", "age", "email").
    :param filter_value: The value used for filtering (e.g., "Alice", 30, "alice@example.com").
    :return: None
    All parameters are type of string (Including age)
    '''
    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print(f"No users found with {filter_type}: '{filter_value}'.")


def filter_users_by_name(name: str):
    '''
    Filter users by their name.
    :param name: The name to filter users by.
    :return: None
    '''
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    print_filtered_users(filtered_users, "name", name)


def filter_by_age(age: int):
    '''
    Filter users by their age.
    :param age: The age to filter users by.
    :return: None
    '''
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]
    print_filtered_users(filtered_users, "age", str(age))


def filter_by_email(email: str):
    '''
    Filter users by their email.
    :param email: The email to filter users by.
    :return: None
    '''
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] == email]
    print_filtered_users(filtered_users, "email", email)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name', 'email' and 'age' are supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: "))
        filter_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_by_age(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
