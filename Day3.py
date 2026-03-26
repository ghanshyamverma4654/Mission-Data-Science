'''Day 3: Loops Mastery'''

'''1st Program: 1 se 10 tak numbers print kro.'''
# for i in range(1,11,1):
#     print(i)

'''2nd Program: 1 se 10 tak even numbers print kro.'''
# num = range(1,11)
# for i in num:
#     if i%2 == 0:
#         print(i)

'''3rd Program: 1 se 10 tak odd numbers print kro.'''
# a = range(1,10)
# for i in a:
#     if i%2 != 0:
#         print(i)

'''4th Program: 1 se N tak ka sum, N is user input.'''
# user_input = int(input("Give me a number and I will give you the sum of all numbers till your given number: "))
# sum = 0
# if user_input < 0:
#     print("Invalid Input: enter a positive integer value.")
# else:
#     for i in range(1,user_input+1):
#         sum = i + sum
#     print(f"Sum of all number till {user_input}, is = {sum}")

'''5th Program: Table print kro(user input lekar).'''
# user_input = int(input("To print table enter a positive integer value:"))
# for i in range(user_input, (user_input*10)+1, user_input):
#     print(i)

'''6th Program: Factorial nikalna: Multiplication of all numbers below a given number.'''

# user_input = int(input("Enter a positive integer value: "))
# factorial = 1
# if user_input <= 0:
#     print(f"ValueError: enter a value greater than 1.")
# elif user_input == 1:
#     print("Factorial of 1 is = 1")
# else:
#     for i in range(1,user_input+1):
#         factorial *= i
#     print(f"Factorial of {user_input}, is = {factorial}")

''''''