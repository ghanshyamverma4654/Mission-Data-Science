'''If-Else Mastery'''

'''1st Program'''
#Number Even hai ya Odd.

# num = int(input("Enter a number: "))
# if num%2 == 0:
#     print(f"{num} is an Even number.")
# else:
#     print(f"{num} is an Odd number.")

'''2nd Program: Positive or Negative.'''

# num = int(input("Enter a number: "))
# if(num > 0):
#     print(f"{num} is a positive number.")
# elif (num < 0):
#     print(f"{num} is a negative number.")
# else:
#     print(f"Entered value is 0")

'''3rd Program: Check age whether eligible for voting or not.'''
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible for voting 😊")
# else:
#     print("Sorry! You are not 18 or 18+, you can not voting 😔")

'''4th Program: Find largest among given 3 numbers.'''
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))
# if num1 > num2 and num1 > num3:
#     print(f"{num1} is the largest number.")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2} is the largest number.")
# elif num1 == num2 and num2 == num3:
#     print("All the numbers are same.")
# else:
#     print(f"{num3} is the largest number.")

'''5th Program: Student pass or fail (Passing mark >= 40)'''
# marks = int(input("Enter marks: "))
# if marks >= 40:
#     print(f"Your mark = {marks}, you are pass.")
# else:
#     print(f"Your marks = {marks}, you are fail.")

'''6th program: Divisible by 5 and 11'''
# num = int(input("Enter an Integer: "))
# if (num%5 == 0) and (num%11 == 0):
#     print(f"{num}, is divisible by both 5 and 11.")
# elif (num%5 != 0 and num%11 == 0):
#     print(f"{num}, is divisible by 11 only but not by 5.")
# elif (num%5 == 0 and num%11 != 0):
#     print(f"{num}, is divisible by 5 only but not by 11.")
# else:
#     print(f"{num}, neither divisible by 5 nor by 11.")
    
'''7th Program: Check leap or not.'''
# year = int(input("Enter a year: "))
# if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
#     print(f"{year}, is a leap year.")
# else:
#     print(f"{year}, is not a leap year.")

'''8th Program: Simple grading system.'''
# marks = int(input("Enter marks: "))
# if marks > 90:
#     print("Your grade is: A+")
# elif marks == 90:
#     print("Your grade is: A")
# elif marks < 90 and marks >= 80:
#     print("Your grade is: B+")
# elif marks < 80 and marks >= 70:
#     print("Your grade is: B")
# elif marks < 70 and marks >= 60:
#     print("You grade is: C")
# elif marks < 60 and marks >= 50:
#     print("Your grade is: D")
# elif marks < 50 and marks >= 40:
#     print("Your grade is: E")
# else:
#     print("You are fail.")

'''9th Program: Simple Calculator.'''
# num1 = int(input("Enter 1st integer: "))
# num2 = int(input("Enter 2nd integer: "))

# print("Choose operation: 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division")
# choice = int(input("Choice: "))
# if choice == 1:
#     print(f"{num1} + {num2} = {num1 + num2}")
# elif choice == 2:
#     print(f"{num1} - {num2} = {num1 - num2}")
# elif choice == 3:
#     print(f"{num1} x {num2} = {num1 * num2}")
# elif choice == 4:
#     print(f"{num1} / {num2} = {num1/num2}")
# else:
#     print("Invalid choice...")
