# Day4: FUNCTIONS

'''1st Program: Function jo 2 numbers ko add kare'''
# def sum(a,b):#Defining function sum
#     return a+b

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# print(f"{num1} + {num2} = {sum(num1,num2)}") #Calling function sum

'''2nd Program: Function jo diye hue number ka square kare.'''
# def square(num):
#     return f"Square of {num} is {num**2}" #OR num * num

# num = int(input("Enter a number to square: "))
# print(square(num))

'''3rd Program: Function jo even/odd check kare.'''
# def even_or_odd(num):
#     if num == 0:
#         return f"YOUR NUMBER IS {num}, ENTER A VALUE GREATER THAN 0"
#     elif num % 2 == 0:
#         return f"{num} IS AN EVEN NUMBER."
#     else:
#         return f"{num} IS AN ODD NUMBER."
    
# num = int(input("Enter a number: "))
# print(even_or_odd(num))

'''4th Program: Function to find factorial of a given number.'''
# def factorial(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact *= i
#     return f"Factorial of {num} is = {fact}."

# num = int(input("Enter a number to find its factorial: "))
# print(factorial(num))

'''5th Program: Function to check the given number prime or not.'''
#Defining function for prime or not
# def is_prime(num):
#     if num == 0 or num == 1:
#         return "Not a prime number."
#     elif num == 2:
#         return "2 is a prime number."
#     else:
#         is_Prime = 1
#         for i in range(2,int(num**.5)+1):
#             if num % i == 0:
#                 is_Prime = 0
#                 break
#         if is_Prime:
#             return f"{num} is a prime number."
#         else:
#             return f"{num} is not a prime number."

# #print and calling function
# num =int(input("Enter a no. to check its prime: "))
# print(is_prime(num))

'''6th Program: Function to find max among 3 given numbers.'''
#Defining max() function
# def max(a,b,c):
#     if a>b and a>c:
#         return f"{a} is the greatest."
#     elif b>a and b>c:
#         return f"{b} is the greatest."
#     elif c>a and c>b:
#         return f"{c} is the greatest."
#     elif a==b and a==c:
#         return f"{a},{b},{c}, all are equal."

# n1 = int(input("Enter 1st no.: "))#taking inputs
# n2 = int(input("Enter 2nd no.: "))
# n3 = int(input("Enter 3rd no.: "))
# print(max(n1,n2,n3))#calling and printing function max()

'''7th Program: Function to print fibonacci series.'''
#Defining function
# def fibo(num):
#     r1,r2 = 0,1
#     for i in range(num+1):
#         print(r1,end=" ")
#         r1,r2 = r2, r1+r2

# num = int(input("Enter a number: "))#taking input by user
# fibo(num)#calling function

'''8th Program: Calculator using function'''
#Defining function calculator()
# def calculator(choice,a,b):
#     if choice == 1:
#         return f"{a}+{b} = {a+b}"
#     elif choice == 2:
#         return f"{a}-{b} = {a-b}"
#     elif choice == 3:
#         return f"{a}x{b} = {a*b}"
#     elif choice == 4:
#         if a>b:
#             return f"{a}/{b} = {a/b}"
#         else:
#             return f"{b}/{a} = {b/a}"
#     else:
#         return "Invalid Input, Choose b/w 1 to 4"
    
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# c = int(input("Choose operation - 1.Add, 2.Subtract, 3.Multiply, 4.Divide: "))

# print(calculator(c,a,b))#calling and printing calculator function