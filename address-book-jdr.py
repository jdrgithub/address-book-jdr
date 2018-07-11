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

def add_contact():
    """ Add contact """
    headers = ['name', 'address', 'phone', 'email']
    list = []
    for header in headers:
        header = input(header + ": ")
        list.append(header)
    filename = 'contacts.txt'
    if check_4_file():
        with open(filename, 'a') as file_object:
                file_object.write("%s \n" % list)

add_contact()

def print_book():
    """ Display contents of contacts.txt file."""
    filename = 'contacts.txt'
    if check_4_file():
        print("The contact.txt file is there.")
    else:
        return "You need a new contact.txt file!"
	
    with open(filename) as file_object:
        lines = file_object.readlines()
    
    for line in lines:
        print(line.rstrip())

print_book()

def read_file():
    """ Read in contents of contacts.txt into a list """
    if check_4_file():
        print("The contact.txt file is there.")
    else:
        return "You need a new contact.txt file!"
    list = []
    filename = 'contacts.txt'
    with open(filename) as f_obj:
        lines = f_obj.readlines()
    for line in lines:
        print(line.rstrip())

read_file()

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
