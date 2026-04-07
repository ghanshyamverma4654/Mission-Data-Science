'''CRUD OPERATION IN FILE HANDLING'''


'''This 👇 library will provide the functionallity to check the path of the files'''

from pathlib import Path

import os #for remove finction in deletefile()

'''This 👇 function will print all the files in the directory.'''

def fileandfolders():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")


def createfile():
    try:
        fileandfolders()
        file_name = input("Enter your file name: ")
        p = Path(file_name)
        
        if not p.exists():
            
            with open(p,"w") as fs:
                data = input("Write content for your file: ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY")
        else:
            print("This file alredy exists.")
        
    except Exception as error:
        print(f"An error occured as: {error}")

def readfile():
    try:
        fileandfolders()
        file_name = input("File name?? ")
        p = Path(file_name)
        if p.exists() and p.is_file():
            with open(p,'r') as file:
                content = file.read()
                print(content)
            print("READED SUCCESSFULLY")
        else:
            print("File does not exist.")
    except Exception as error:
        print(f"An error occured as: {error}")

def updatefile():
    try:
        fileandfolders()
        file_name = input("File name to update?? ")
        p = Path(file_name)
        if p.exists() and p.is_file():
            print("Enter 1 to rename the file")
            print("Enter 2 to add new content in the file")
            print("Enter 3 to delete old and add new content in the file")

            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                new_file_name = input("Enter the new name of the file: ")
                p2 = Path(new_file_name)
                p.rename(p2)
                print("Renamed successfully.")
            if choice == 2:
                with open(p, 'a') as file:
                    content = input(f"Enter content to add in the file: ")
                    file.write(content)
                    print("New content added successfully.")
            
            if choice == 3:
                with open(p,'w') as file:
                    content = input("Enter content (NOTE: this will replace all the existing content): ")
                    file.write(content)
                    print("Content replaced successfully.")
        else:
            print("File does not exist.")
    except Exception as error:
        print(f"An error occured as: {error}")
            
def deletefile():
    try:
        fileandfolders()
        file_name = input("Name the file you want to delete: ")
        p = Path(file_name)
        if p.exists() and p.is_file():
            os.remove(file_name)
            print("File deleted successfully.")
        else:
            print("This file dose not exixts.")
    except Exception as error:
        print(f"An error occured as: {error}")  
    
    

print("Enter 1 to CREATE a file: ")
print("Enter 2 to READ a file: ")
print("Enter 3 to UPDATE a file: ")
print("Enter 4 to DELETE a file: ")

choice = int(input("Enter your choice: "))

if choice == 1:
    createfile()
    
elif choice == 2:
    readfile()

elif choice == 3:
    updatefile()

elif choice == 4:
    deletefile()
else:
    print("Invalid choice.")