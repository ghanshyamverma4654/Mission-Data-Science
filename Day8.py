'''Errors, Exception & Exception Handling'''
# ERRORS: Errors are just common mistakes done buy the developers.
# i.e. Syntax error --> Missing closing paranthesis
#      Indentation error
#      Tab or Space error

'''EXCEPTIONS: These are unexcepted errors that affects the code execution and flow of the programs.'''

# a = int(input("Enter a number: "))
# print(10/a)# It will throw an error if the value of a = 0

'''EXCEPTION HANDLING'''

# a = int(input("Enter a number: "))
# try:
#     print(10/a)
# except Exception as error:
#     print(f"There is an error as : {error}")

# else:
#     print("Good! there is no error.")

# finally:
#     print("This block will execute no matter there is an error or not.")    

"""There is a keyword named: 'raise' used to throw a munnual  exception."""
#example

# age = int(input("Enter your age: "))
# if age<10 or age>18:
#     raise ValueError("Your age must be between 10 and 18.")
# else:
#     print("Welcome to the club.")
# print("Club will start soon!")#this line will not execute if there will be an error

#lets handle this

# age = int(input("Enter your age: "))

# try:
#     if age < 10 or age > 18:
#         raise ValueError("Your age must be between 10 and 18.")
#     else:
#         print("Welcome to the club.")
# except Exception as error:
#     print(f"An error occured as : {error}")#Exception is handled here

# print("The club will start soon.")#This line will excute now