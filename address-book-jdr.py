""" Address Book JDR  """
import sys
import os.path

def main():
    """ Main entry point for the script."""

def menu():
    """ Main Menu """
    print(30 * "-", "MENU", 30 * "-")
    print("1. Add a record")
    print("2. Delete a record") 
    print("3. Look up record")
    print("4. Change a record")
    print("5. Display all records")
    print("6. Check contact file")
    print("7. Exit")
    print(67 * "-")
		
loop=True
while loop:
    menu()
    choice = input("What would you like to do? ")

    if choice == "1":
        print("\n Add Record")
		add_contact()
    elif choice == "2":
        print("\n Delete Record")
    elif choice == "3":
        print("\n Find Record")
    elif choice == "4":
        print("\n Change Record")
    elif choice == "5":
        print("\n Display All Records")
		print_book()
    elif choice == "6":
        print("\n Check on contact.txt")
		check()
    elif choice == "7":
        print("\n Goodbye")
        exit()			
    else: 
        print("\n Try again") 

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
    for entry in headers:
        entry = input(entry)
        list.append(entry)
    filename = 'contacts.txt'
    if check():
        with open(filename, 'a') as file_object:
                file_object.write(print(','.join(list)))

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

""" How about I replace this with something simpler """
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
