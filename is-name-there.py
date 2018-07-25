import os
import pickle
import os

filename = "contacts.txt"

def is_it_there():
  
  filename = "contacts.txt"

# Check to see if the file exists
  if os.stat(filename).st_size != 0:
    # If contacts.txt not empty read list in
    pickle_in = open(filename,"rb")
    all_records = pickle.load(pickle_in)

  name = raw_input("Enter a name to delete.")
  for i in all_records:
    if i[0] == name:
      status = True
      break
    else:
      status = False
  print(status)
  return status

is_it_there()
