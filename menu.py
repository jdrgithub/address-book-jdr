import sys
import os.path

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
add_contact()






