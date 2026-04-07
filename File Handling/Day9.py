'''FILE HANDLING'''
#A name with any extension like .py,.txt, .mp3, .pdf etc is known as a file.

'''MODES
        'r' --> Read (Default) - file must exist.
        'w' --> Write - creates file or overwrites.
        'a' --> Append - adds to end of the file.
        'x' --> creates a new file - fails if it exist.
   Syntax: 
            file = open("myfile.txt","r")
            print(file.read())==> Read entire file
            print(file.readline())==> Read one line
            print(file.readlines())==> Read all lines into a list.
            print(file.close())==> Closes current file.
            
   'with' KEYWORD: 
                    with open("data.txt","r") as f:
                        content = f.read()
                        print(content)
'''
'''Writing a file and in a file'''
# file = open("new_file.txt","w")
# file.write("Writing in the file.")

'''Appending in the file'''
# file = open("new_file.txt","a")
# file.write(' And now i am appending in the file.')

'''Reading the file'''
# file = open("new_file.txt") #OR file = open("new_file.txt","r")

# print(file.read()) #---> Reads entire file.

# print(file.readline())#---> Reads single line.

# print(file.readlines())#---> Reads multiple lines in a list i.e. ['Writing in the file. And now i am appending in the file.\n', 'Second line to read.']
