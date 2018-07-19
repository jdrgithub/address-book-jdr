  # Check to see if the file exists
  if check():
    if os.stat(filename).st_size != 0:
    # If contacts.txt not empty read list in
      pickle_in = open(filename,"rb")
      all_records = pickle.load(pickle_in)



  new_all = []
  # Get name to delete record of
  name = raw_input("Name to delete record of? ")
  for _ in range(
  for i in all_records:
        if i[0] == name:

