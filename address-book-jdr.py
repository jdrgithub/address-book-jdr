""" Address Book JDR  """
import sys
import os.path

def main():
    """ Main entry point for the script."""

def menu():
    """ Main Menu """
    print(30 * "-", "MENU", 30 * "-")
    print("1. Add a record")
    print("2. Delete contact") 
    print("3. Look up record")
    print("4. Change a record")
    print("5. Display all records")
    print("6. Check contact file")
    print("7. Exit")
    print(67 * "-")

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
        entry = raw_input(header + ': ')
        list.append(entry)
    filename = 'contacts.txt'
    with open(filename, 'a') as file_object:
        line = str(':'.join(list))
        file_object.write(str(line) + "\n")
		
def delete_contact():
    """ Delete contact """
    """ General steps
	Ask the user for a name to delete record of
	Read in all records to a list, unless the first field matches the supplied name
	Write lists out to contacts.txt  """
    filename = 'contacts.txt'
    name = raw_input("Name to delete record of? ")
    with open(filename) as file_object:
        lines = f_obj.readlines()
    list_out = []		
    for line in lines:
        if line[0] == name:
            continue
        else:
            list_out.append(line)		
    with open(filename, 'w') as file_object:
        file_object.write(str(list_out))	
		    
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

		
def find_contact(name):
    """ Contact search """
    pass

def modify_contact_data(name):
    """ Modify contact """
    """ Do a conditional test """
    """ like name in list """
    pass


		
loop=True
while loop:
    menu()
    choice = input("What would you like to do? ")

    if choice == 1:
        print("\n Add Record")
        add_contact()
    elif choice == 2:
        print("\n Delete contact")
        delete_contact()
    elif choice == 3:
        print("\n Find Record")
        find_record()
    elif choice == 4:
        print("\n Change Record")
        modify_contact_data()
    elif choice == 5:
        print("\n Display All Records")
        print_book()
    elif choice == 6:
        print("\n Check on contact.txt")
        check()
    elif choice == 7:
        sys.exit("Goodbye")			
    else: 
        print("\n Try again") 


if __name__ == '__main__':
    sys.exit(main())
