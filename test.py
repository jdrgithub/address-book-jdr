#!/usr/bin/python

import sys
import os
import pickle


def is_it_there(name):
  # Check to see if name is in file                                                      
  filename = "contacts.txt"                      
  print(name)
                                                         
  # Check to see if the file exists                        
  all_records = []
  if os.stat(filename).st_size != 0:                     
    # If contacts.txt not empty read list in             
    pickle_in = open(filename,"rb")                      
    all_records = pickle.load(pickle_in)                 
  
  for i in all_records:
    if i[0] == name:
      return True
  return False

def delete_contact():
  # Data file to store contacts in pickle form   
  filename = 'contacts.txt'
  
  # Check to see if the file exists
  if os.stat(filename).st_size != 0:
    # If contacts.txt not empty read list in
    pickle_in = open(filename,"rb")
    all_records = pickle.load(pickle_in)

  while True:
    name = raw_input("Enter name or type quit.")			
    if name == "quit":
      return
    else:
      new_all = []
      if is_it_there(name):
        print("OOgabooga")
        for i in all_records:
          if i[0] != name:
            new_all.append(i)
      else:
        break 

  # Write out all records to file
  pickle_out = open(filename, "wb")
  pickle.dump(new_all, pickle_out)
  pickle_out.close() 

delete_contact()
