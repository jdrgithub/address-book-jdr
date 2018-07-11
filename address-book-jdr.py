""" Address Book JDR  """
import sys
import os.path

def main():
    """ Main entry point for the script."""
    pass

def check_4_file():
    """ Check for contacts.txt file """
    try:
        f = open('contacts.txt')
        f.close()
    except IOError as e:
                return False
    return True

check_4_file()

def add_contact():
    """ Add contact """
    headers = ['name', 'address', 'phone', 'email']
    list = []
    for header in headers:
        header = input(header + ": ")
        list.append(header)
    return list

add_contact()

def print_book():
    """ Print book """
    pass

def contact_search(name):
    """ Contact search """
    pass

def modify_contact(name):
    """ Modify contact """
    """ Do a conditional test """
    """ like name in list """
    pass

def delete_contact(name):
    """ Delete contact """
    pass

def manage_menu():
    """ Manage menu """
    pass

if __name__ == '__main__':
    sys.exit(main())
