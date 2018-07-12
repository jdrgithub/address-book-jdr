""" Address Book JDR  """
import sys
import os.path

def main():
    """ Main entry point for the script."""

biglist = []
	
def menu():
    """ Main Menu """
    print(30 * "-", "MENU", 30 * "-")
    print("1. Add contact")
    print("2. Delete contact") 
    print("3. Find contact")
    print("4. Change an entry")
    print("5. Display all records")
    print("6. View and verify contact.txt file")
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
    # Parameter names
    headers = ['Name', 'Address', 'Phone', 'Email']
    
    # List representing each record as it is input
    a_list = []
	
    # List representing all records
    all_records = []
	
    # File holding data
    filename = 'contacts.txt'

    # Use the header titles in headers to prompt for input
    for header in headers:
        entry = raw_input(header + ': ')
        a_list.append(entry)
		
    # Read nested list from file into all_records	
    with open(filename) as file_object:
        all_records = list(file_object.read())
		
    # Change from string into list
    list(all_records)

    """  Put the nested list from the file into biglist		
    biglist = all_records[:] """
	
    # Append current contact record to biglist
    all_records.append(a_list)

    # Write out nested list biglist to file
    with open(filename, 'a') as file_object:
        file_object.write(str(all_records))
		
	
def delete_contact():
    """ Delete contact """
    filename = 'contacts.txt'
    name = raw_input("Name to delete record of? ")
    with open(filename) as file_object:
        a_lines = file_object.reada_lines()
    list_out = []		
    for a_line in a_lines:
        if a_line[0] == name:
            continue
        else:
            list_out.append(a_line)		
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
        a_lines = file_object.readlines()
    
    for a_line in a_lines:
        print(a_line.rstrip())


def read_file():
    """ Read in contents of contacts.txt into a list """
    if check():
        print("The contact.txt file is there.")
    else:
        return "You need a new contact.txt file!"
    list = []
    filename = 'contacts.txt'
    with open(filename) as f_obj:
        a_lines = f_obj.reada_lines()
    for a_line in a_lines:
        print(a_line.rstrip())

		
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
