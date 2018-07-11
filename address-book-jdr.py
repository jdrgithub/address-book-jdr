""" Address Book JDR  """
import sys
import os.path

def main():
    """ Main entry point for the script."""
    pass

def check_4_file(contacts_file='contacts.txt'):
    """ Check for contacts.txt file """
    try:
                f = open(contacts_file, mode)
                f.close()
        except IOError as e:
                return False
        return True

check_4_file("contacts.txt")

def add_contact():
    """ Add contact """
    for param in (name, address, email, phone):
                param = input(param + "? ")
                little_list = [name, address, email, phone]
                big_list = big_list.append(little_list)
        return big_list

big_list = add_contact():

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
