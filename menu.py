""" Address Book JDR  """ 
import sys 
import os.path

answer=True 

while answer:
    print (""" 1. Add a record
               2. Delete record
               3. Look up record
               4. Change record
               5. Display all
               6. Exit/Quit """)
    answer=input("What would you like to do? ")
    if answer == "1":
        print("\n Record added")
    elif answer == "2":
        print("\n Record deleted")
    elif answer == "3":
        print("\n Record Found")
    elif answer == "4":
        print("\n Goodbye") 
    elif answer != "":
        print("\n Try again")
