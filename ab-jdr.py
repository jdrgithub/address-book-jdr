""" Address Book JDR  """
import sys
import os.path

def main():
    """ Main entry point for the script."""
    pass

def check_4_file(contacts_file):
    """ Check for contacts.txt file """
    try:
        my_path = os.path.exists(contacts_file)
    except FileNotFoundError:
        print("Doesn't exist.")
    else:
        print("Exists")

check_4_file("contacts.txt")

def add_contact(name, address, phone, email):
    """ Add contact """
    name, address, phone, email = [str(x) for x in input().split()]

def print_book():
    """ Print book """
    pass

def contact_search(name):
    """ Contact search """
    pass

def modify_contact(name):
    """ Modify contact """
    pass

def delete_contact(name):
    """ Delete contact """
    pass

def manage_menu():
    """ Manage menu """
    pass

if __name__ == '__main__':
    sys.exit(main())
