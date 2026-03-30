'''DATA STRUCTURE'''
'''''''''LIST'''''''''

'''1st Problem: Create a list and print it.'''
l = [1,2,3,4,5,6]
# print(l)

'''2nd Problem: Print the elements of list using loop.'''
# for i in l:
#     print(i,end=" ")

'''3rd Problem: Find the sum of all elements in list.'''
# sum = 0
# for i in l:
#     sum += i
# print(f"Sum of all elements in {l} = {sum}.")    

'''4th Problem: Find the largest number in the list with index.'''
# lgst = l[0]
# index = 0
# for i in range(len(l)):
#     if l[i]>lgst:
#         lgst = l[i]
#         index = i
    
# print(f"Largest number in list is {lgst} at position {index}.")

'''5th Problem: Find smallest number in the given list with index.'''
# l = [1,2,3,4,2,3]
# smallest = l[0]
# index = 0
# for i in range(len(l)):
#     if l[i]<smallest:
#         smallest = l[i]
#         index = i
# print(f"Smallest number in the list is: {smallest}.")

'''6th Problem: Store even numbers in a new list and print it.'''
# l=[12,232,434,65,78789,2,4234,5435]

# evens = []
# for i in l:
#     if i%2 == 0:
#         evens.append(i)
# if len(evens) == 0:
#     print(f"There is no even numbers in the list:\n{l}")
# else:
#     print(f"Even numbers in list {l} is/are:\n{evens}.")

'''7th Problem: Take input from the user and store it in a list.'''
# user_list = []
# while True:
#     user_input = input("Enter anything to store in list: ")
#     user_list.append(user_input)
    
#     choice = input("Do you want to add anything else?? (y/n): ")
#     if choice.casefold() == 'n':
#         break
# print(f"List of things you entered:\n{user_list}")

'''8th Problem: Reverse the list.'''
# lst = [12,342,5465,676,12,11]
# reversed_list = []

# for i in range(len(lst)-1,-1,-1):
#     reversed_list.append(lst[i])

# print(f"Original lis is: {lst}\nReversed list is: {reversed_list}. ")

'''9th Problem: '''