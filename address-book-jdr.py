#!/usr/bin/python

""" Address Book JDR  """
import sys
import os
import pickle

def main():
  """ Main entry point for the script."""

def menu():
  """ Main Menu """
  print("-----MENU-----")
  print("1. Add Contact")
  print("2. Delete Contact") 
  print("3. Display Details")
  print("4. Change Details")
  print("5. Display All")
  print("6. Exit")
  print("-------------")

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
  pickle_out = open("contacts.txt","wb")
  pickle.dump(all_records, pickle_out)
  pickle_out.close()


def delete_contact():
  """ Delete contact """\
  # Data file to store contacts in pickle form   
  filename = 'contacts.txt'
  
  # Check to see if the file exists
  if check():
    if os.stat(filename).st_size != 0:
    # If contacts.txt not empty read list in
      pickle_in = open(filename,"rb")
      all_records = pickle.load(pickle_in)

  new_all = []			
  # Get name to delete record of
  name = raw_input("Name to delete record of? ")			
  for i in all_records:
    if i[0] == name:
      for i in all_records:
        if j[0] != name:
          # Append records if they don't contain the name just entered
          [new_all.append(all_records[i]) for (i,record) in enumerate(all_records) if all_records[i][0] != name ]
          break
        else:
	  print(i[0])
          print(all_records[0])
      print("Name not in records.")
      return

  print(new_all)
  print("\n")
			
  # Write out all records to file
  pickle_out = open(filename, "wb")
  pickle.dump(new_all, pickle_out)
  pickle_out.close() 

	
def display_details():
  """ Contact search """
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

  name = raw_input("Name to display details for? ")	
  # Use enumerate to list and find incr and print
  for (i,record) in enumerate(all_records):
    if name in record:
      this_record = all_records[i]
      print(' | '.join(this_record))
      print("\n")
  raw_input("Press enter to continue.")
      
def change_details():
  # Chenge address, phone, email for a name 
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

  name = raw_input("Name to change details for? \n")
  print("Here are the contact details for that name: \n")
  
  # Use enumerate to list and find incr and print
  contact_details = []
  for (i,record) in enumerate(all_records):
    if name in record:
      contact_incr = i
      contact_details = all_records[i]
      print(all_records[i])
  
	# Request input for category and set to appropriate address increment
  category = raw_input("\nWhat category do you want to change for: address, phone, or email? \n")
  if category == 'address':
    print("The address is: " + contact_details[1] + "\n")
    j = 1	
  elif category == 'phone':
    print("The phone is: " + contact_details[2] + "\n")
    j = 2
  elif category == 'email':
    print("The email is: "  + contact_details[3] + "\n")
    j = 3
  else:
    print("You didn't select one of the three categories: address, phone, or email.")

  # Pick a new value and enter new value into old_location using i and j
  new_value = raw_input("\nWhat do you want the new value to be? ")
  all_records[i][j] = new_value
  print(all_records[i][j])	

  # Write out all records to file
  pickle_out = open(filename, "wb")
  pickle.dump(all_records, pickle_out)
  pickle_out.close()
	

def display_all():
  # Check to see if the file exists
  filename = 'contacts.txt'
  all_records = []
  if check():
    if os.stat(filename).st_size != 0:
    # If contacts.txt not empty read list in
      pickle_in = open(filename,"rb")
      all_records = pickle.load(pickle_in)
  else:
    print("The contacts file is empty!")
    return
  for a_line in all_records:
    print(a_line)
  print("\n")
  raw_input("Press enter to continue.")


# Overarching loop that calls other functions
loop=True
while loop:
  menu()
  choice = raw_input("What would you like to do? ")
  if choice == "1":
    print("\n-----Add Contact------")
    add_contact()
  elif choice == "2":
    print("\n------Delete Contact-----")
    delete_contact()
  elif choice == "3":
    print("\n------Display Details-----")
    display_details()
  elif choice == "4":
    print("\n-----Change Details------")
    change_details()
  elif choice == "5":
    print("\n-----Display All------")
    display_all()
  elif choice == "6":
    sys.exit("-----Goodbye------")			
  else: 
    print("\n Try again") 

if __name__ == '__main__':
  sys.exit(main())
