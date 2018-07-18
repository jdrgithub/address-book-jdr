#!/usr/bin/python

""" Address Book JDR  """
import sys
import os
import pickle

def main():
    """ Main entry point for the script."""

def check():
    """ Check for contacts.txt file """
    try:
        f = open('contacts.txt')
        f.close()
    except IOError as e:
        return False
    return True

def check_answer():	
    """ CHECK ANSWER FUNCTION """\
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
            print("It's there.")
            return True
    else:
	print("It's not there!")

check_answer()
