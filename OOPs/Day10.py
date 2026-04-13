'''OOPs'''

'''CLASSES'''
# class Car:
#     brand = "Toyota" #===> Attribute
#     numOfCars = 120 #===> Attribute
    
#     def greeting(self): #===> Method
#         print("Hey welcome to the toyota moters.")
        
# object = Car() #===> Object/ Instance

# object.numOfCars = 150 #===>Overwriting the value inside the class using an object
# # print(object.brand)
# # print(object.numOfCars)
# object.greeting()
# print(f"We have total {object.numOfCars} {object.brand} cars in our store currently.")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''CONSTRUCTOR'''

# class Student:
#     sr_no = 1 #===> class attribute
    
#     def __init__(self,name,age): # This is constructor
#         self.name = name     # Instance Attribute 
#         self.age = age       # Instance Attribute
        
# S = Student("Ghanshyam",25) #Now this class will required a parameter like "name"

# print(f"SrNo. {S.sr_no} {S.name}, age {S.age}") #===> Output: SrNo. 1 Ghanshyam, age 25

'''INSTANCE METHOD'''

# class MyClass:
#     def instance_method(self):
#         print("This is an instance method.")
        
# obj = MyClass()
# obj.instance_method() #===> Output: This is an instance method.

'''CLASS METHOD'''

# class MyClass:
#     @classmethod
#     def class_method(cls):
#         print("This is a class method.")

# obj = MyClass() #===> Object/Instance
# obj.class_method() #===> Output: This is a class method.

'''STATIC METHOD'''

# class MyClass:
#     @staticmethod
#     def static_method():
#         print("This is a static method.")
        
# obj = MyClass() #===> Object/Instance
# obj.static_method() #===> Output: This is a static method.

'''"INHERITANCE" : PROPERTIES OR ANY POSSESSION COMES TO AN HEIRARICHY.'''

# class Parent:
#     def speak(self):
#         print("I can speak.")
        
# class Child(Parent): #===> Child class inheriting method of Parent class
#     pass

# object = Child() #===> Object for Child class
# object.speak() #===> Output: I can speak. <=== Accessing method in Parent class using Child class's object

'''Constructor in Inheritance'''

# class Parent:
#     def __init__(self,name):
#         self.name = name

# class Child(Parent): #===> Child class can inherit costructor of the parent class
#     def display(self):
#         print(f"My name is {self.name}")

# # obj = Parent("ATLAS")
# obj1 = Child("ATLAS")
# obj1.display() #===> Output: My name is ATLAS

'''Now If I want to initilize a constructor inside the child class I must have to use the "super()" function'''

# class Parent:
#     def __init__(self,name):
#         self.name = name
# class Child(Parent):
#     def __init__(self, name,age):
#         super().__init__(name) #===> It took name from Parent class and  
#         self.age = age         #===> initialized a new attribute age
#     def display(self):
#         print(f"My name is {self.name} and I am {self.age} years old.")
        

# obj = Child("ATLAS",25) #===> An object for Child class with parameters
# obj.display() #===> Output: My name is ATLAS and I am 25 years old.

'''TYPES OF INHERITANCE'''
'''SINGLE INHERITANCE => All of the above examples'''

'''MULTIPLE INHERITANCE => 2 Parent Classes and 1 Child Class
    NOTE: In case of Inheritance of Constructor- Child will inherate constructor of only  first parent class which the child inherit first.
'''
# class Father:
#     def skills(self):
#         print("Coding")

# class Mother:
#     def skills(self):
#         print("Cooking")

# #class Child(Mother,Father): #===> Case: 1
# class Child(Father,Mother): #===> Case: 2
#     def show(self):
#         print("I have multiple skills.")
        
# obj = Child()
# obj.show() #===> Output => I have multiple skills.
# obj.skills() #===> OUTPUT IN =>  Case:1 => Cooking | Case:2 => Coding | 
# Cause => MRO (Method Resolution Order)

'''MULTILEVEL INHERITANCE: GrandParent Class --> Parent Class --> Child Class'''

# class GrandParent:
#     def heritage(self):
#         print("Heritage from grandparent.")
        
# class Parent(GrandParent): 
# #===> Parent class will inherite all properties of its Parent or GrandParent class
#     pass

# class Child(Parent): 
# #===> Child class will inherite all the properties of Both Parent and GrandParent Class
#     pass

# obj = Child()
# obj.heritage() #===> Output => Heritage from grandparent.

'''POLYMORPHISM : Same innterface or method name but behave differently.'''
'''Types of Polymorphism: 
                    1. Method Overriding: 
                                    Child class overrides a method of the parent class, and python decides at runtime which method to call based on the object type.
                                    
                    2. Method Overloading (NOT SUPPORTED IN PYTHON) Same method name diff. parameters.
                    
                    3. Duck Typing:
                                Python follows the philosophy:
                                    "If it walks like a duck and quacks like a duck, it must be a duck."
'''

'''METHOD OVERRIDING'''
# class Animal:
#     def sound(self):
#         print("Animal makes a sound.")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks.")
        
# object = Animal()
# object1 = Dog()
# # Although Dog inherite sound() from Animal but the method sound() has overriden in  Dog class.

# object.sound() #===> Output => Animal makes a sound.
# object1.sound() #===> Output => Dog barks.

'''DUCK TYPING'''
# class Duck:
#     def talk(self):
#         print("Quack!")
# class Human:
#     def talk(self):
#         print("Hello!")
        
# obj = Duck()
# obj1 = Human()

# obj.talk() #===> Output => Quack!
# obj1.talk() #===> Output => Hello!

'''ENCAPSULATION : Hiding the internal details of how things works.

   ACCESS MODIFIERS: 
                This is how we give access of our attributes and methods to the object or inherited classes.
                
   Types of Access modifiers:
                1. PUBLIC Attributes and Modifiers => All the above examples.
                2. PROTECTED Attributes and Methods => 
                        Using a single underscore but still can be accessed from outside of the class.
                        It only uses a naming convention to tell developers.
                3. PRIVATE Attributes and Methods =>
                        Cannot be accessed from outside of the class - only inside class
                        We use 2 underscore(__) before the name to make it private.
'''
# class Demo:
#     def __init__(self):
#          self.name = "Public Member" # Public
#          self._age = 21              # Protected
#          self.salary = 50000         # Private
         
#     def show(self):
#         print("Inside the class: ") #===> Output => Inside the class:
#         print("Public:", self.name) #===> Output => Public: Public Member
#         print("Protected:", self._age) #===> Output => Protected: 21
#         print("Private:", self.__salary) #===> 
#         #===> AttributeError: 'Demo' object has no attribute '_Demo__salary'

# object = Demo()
# object.show()

'''ABSTRACTION: 
            => Astraction doesn't exist in python but we can achieve using a library ___"abc" as 'ABC'
            => Is used to simplifying complex system by focusing on essential ___features and hiding unnecessary details.
            => Is used to define a common interface for different subclasses.
   ABSTRACT: 
            => CLASSES: Class that contains 1 or more abstract methods.
            => METHODS: A method defined but not implemented in the abstract class.
                => Subclasses must provide the implementation.
'''

# from abc import ABC,abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print("Dog says Woof!")
# class Cat(Animal):
#     def make_sound(self):
#         print("Cat says Meow!")
        
# obj = Dog()
# obj1 = Cat()

# obj.make_sound() #===> Output => Dog says Woof!
# obj1.make_sound() #===> Output => Cat says Meow!

'''
DUNDER METHODS: Special methods starts and ends with double underscore(__).
'''
# class Person:
#     def __init__(self,name):
#         self.name = name

# p = Person("Ravi")
# print(p.name) #===> Output => Ravi

