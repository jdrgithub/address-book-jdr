""" Address Book JDR  """
import sys
import os
import pickle

def main():
    """ Main entry point for the script."""

biglist = []
	
def menu():
    """ Main Menu """
    print(30 * "-", "MENU", 30 * "-")
    print("1. Add contact")
    print("2. Delete contact") 
    print("3. Display contact info")
    print("4. Change an entry")
    print("5. Display all records")
    print("6. Exit")
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
	

    # File holding data
    filename = 'contacts.txt'

    # New entries for 
    new_entries = []
    # Use the header titles in headers to prompt for input
    for header in headers:
        entry = raw_input(header + ': ')
        a_list.append(entry)

	# Is contacts.txt empty?
    if os.stat(filename).st_size != 0:
        # If not read nested list from file into all_records
        pickle_in = open("contacts.txt","rb")
        all_records = pickle.load(pickle_in)
    else:
	    all_records = []
	
	# Append the new entries to the master list
    all_records.append(a_list)

    # Write out all_records list to file
    pickle_out = open("contact.txt","wb")
    pickle.dump(all_records, pickle_out)
    pickle_out.close()
	
	
def delete_contact():
    """ Delete contact """
    # Get name to delete record of
    name = raw_input("Name to delete record of? ")
    
    # Data file to store contacts in pickle form   
    filename = 'contacts.txt'
 
    # Check to see if the file exists
    if check():
        if os.stat(filename).st_size != 0:
        # If contacts.txt not empty read list in
            pickle_in = open(filename,"rb")
            all_records = pickle.load(pickle_in)
    else:
        print("The contacts file is empty!")
        return

    new_all = []
    for i in all_records:
        if name not in i:
            new_all.append(i)
            print(new_all)

    # Write out all records to file
    pickle_out = open(filename, "wb")
    pickle.dump(all_records, pickle_out)
    pickle_out.close() 
	
		    
def print_file():

	# Check to see if the file exists
    filename = 'contacts.txt'
    if check():
        if os.stat(filename).st_size != 0:
        # If contacts.txt not empty read list in
            pickle_in = open(filename,"rb")
            all_records = pickle.load(pickle_in)
    else:
        print("The contacts file is empty!")
        return
		
    print(all_records)
    print("\n")
    raw_input("Press any key and enter to continue.")
		
def find_contact(name):
    """ Contact search """

	# Check to see if the file exists
    if check():
        if os.stat(filename).st_size != 0:
        # If contacts.txt not empty read list in
            pickle_in = open(filename,"rb")
            all_records = pickle.load(pickle_in)
    else:
        print("The contacts file is empty!")
        return
    # Use enumerate to list and find incr and print
    for (i,record) in enumerate(all_records):
        if name in record:
            print(all_records[i])
            

def modify_contact_data(name):
    
	# Check to see if the file exists
    if check():
        if os.stat(filename).st_size != 0:
        # If contacts.txt not empty read list in
            pickle_in = open(filename,"rb")
            all_records = pickle.load(pickle_in)
    else:
        print("The contacts file is empty!")
        return

    new_all = []
    for i in all_records:
        if name not in i:
            new_all.append(i)
            print(new_all)

    # Write out all records to file
    pickle_out = open(filename, "wb")
    pickle.dump(all_records, pickle_out)
    pickle_out.close()
		
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
        print_file()
    elif choice == 6:
        sys.exit("Goodbye")			
    else: 
        print("\n Try again") 


if __name__ == '__main__':
    sys.exit(main())
