""" Address Book JDR  """
import sys
import os.path

def main():
    """ Main entry point for the script."""
    pass

def menu():
    answer=True
    while answer:
        print ("""			1. Add a record
	    2. Delete record
	    3. Look up record
	    4. Change record
	    5. Display all
	    6. Exit/Quit """)
    answer = raw_input("What would you like to do? ")
    if answer == "1":
        print("\n Record added")
    elif answer == "2":
        print("\n Record deleted")
    elif answer == "3":
        print("\n Record Found")
    elif answer == "4":
        print("\n Record Changed")
    elif answer == "5":
        print("\n Display Record")
    elif answer == "6":
        print("\n Goodbye")
        exit()			
    elif answer != "":
        print("\n Try again") 

menu()
 
def check():
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
    if check():
        with open(filename, 'a') as file_object:
                file_object.write("%s \n" % list)

add_contact()

def print_book():
    """ Display contents of contacts.txt file."""
    filename = 'contacts.txt'
    if check():
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
    if check():
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


if __name__ == '__main__':
    sys.exit(main())
