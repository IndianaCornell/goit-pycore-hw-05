import re
from command_handlers.input_error import input_error

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args: tuple, contacts: dict) -> str:
    contact_name, phone = args
    pattern = r"[\D]"
    contacts[contact_name] = re.sub(pattern, "", phone)
    return "Contact added."

@input_error
def change_contact(args: tuple, contacts: dict) -> str: 
    contact_name, phone = args
    contacts[contact_name] = phone.strip()
    return "Contact updated."


@input_error
def show_phone(args: tuple, contacts: dict) -> str:
    contact_name = args[0]
    return f"{contact_name}: {contacts[contact_name]}"

@input_error
def show_all(contacts: dict) -> str:

    if not contacts: 
        return "Your contacts list is empty"
    else:
        response = "Your contacts:"
        for name, number in contacts.items():
            response += f"\v\t {name}: {number}"

    return response





