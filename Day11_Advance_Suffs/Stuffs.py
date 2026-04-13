'''
DECORATOR: A function that modifies another function without changing its actual code
         => To create a decorator you first have to create a decorator functions and ___then inside that we will create a wrapper.
'''
# def my_decorator(fuction):
#     def wrapper():
#         print("Before the say_hello runs")
#         fuction()
#         print("After say_hello runs")
#     return wrapper


# @my_decorator
# def say_hello():
#     print("Hello, this is say_hello function")
# say_hello()
#               Before the say_hello runs
#===> Output => Hello, this is say_hello function
#               After say_hello runs

'''
Args and Kwargs: 
               => Special keywords python used in function definitions to accept a  ___flexible number of arguments.
               => Use * and ** and any name with them.(*args || **kwargs)
                  *args : can take multiple positional arguments and becomes tuple
                  **kwargs : can take multiple key-values and becomes dictionary
USES: No need to know number of inputs.
      Helps  in building flexible functions, decorators, APIs and more.
'''
# def fun(*args, **kwargs):
#     print("Args: ", args)
#     print("Kwargs: ", kwargs)

# fun(1,2,3,4,5,name="Monu", age=21, Marks=99, Rank="20th")
'''
===> Output => Args: (1,2,3,4,5)
               Kwargs: {'name': 'Monu', 'age': 21, 'Marks': 99, 'Rank': '20th'}
'''

'''LIST, DICTIONARY AND SET COMPREHENSION:'''

"""LIST"""
# labels =["EVEN" if x%2 == 0 else "ODD" for x in range(5)]
# print(labels) # OUTPUT => ['EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN']

# """DICTIONARY"""
# evens = {x: x*x for x in range(10) if x%2 == 0}
# print(evens) # OUTPUT => {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# """SET"""
# unique_values = {x*x for x in range(10) if x%2 == 0}
# print(unique_values) # OUTPUT => {0, 64, 4, 36, 16}

'''LAMBDA FUNCTIONS: An anonymous, inline function'''
# # With single argument
# square = lambda x: x**2
# print(square(4)) # OUTPUT => 16

# # With multiple Arguments
# check_evens = lambda x:"Even" if x%2 == 0 else "Odd"
# print(check_evens(23)) # OUTPUT => 23

'''MAP & FILTER:
                Used for applying a function to multiple items.
                Takes a list (or any sequence)
                Applies the same function to every item in the list
                Gives a new list (in Python 3, it gives a map object which can convert to a list)
'''
# numbers = [1,2,3,4,5,6,7]
# doubled = map(lambda x:x*2, numbers)
# print(doubled) # OUTPUT => <map object at 0x00000218FD53B9A0>
# print(list(doubled)) # OUTPUT => [2, 4, 6, 8, 10, 12, 14]

'''FILTER:
          Filters out the stuffs
          Takes a list(or any sequence)
          Checks each item using a function(a test)
          Keeps only the items that passes the test(i.e. returns True)
'''
# numbers = [1,2,3,4,5,5,6]
# evens = filter(lambda x: x%2==0, numbers)
# print(evens) # OUTPUT => <filter object at 0x00000226AD2CB9D0>
# print(list(evens)) # OUTPUT => [2, 4, 6]

'''MODULES AND PACKAGES'''

'''MODULES: A single file containing code and we can use this file code in other file.
            A single Python file(.py)
            Contains functions, variables, or classes
            Used to organize and reuse code
            Exanples: math, random, datetime
        =>  KeyWords use: import ____
'''
# import math
# print(math.sqrt(100)) # OUTPUT => 10.0

'''PACKAGES: A package is a folder contains one or more modules or sub-packages
            => Keywords use: from ____ import ___
'''
