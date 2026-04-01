'''Dictionary Mastery'''
#Dictionary Problems
'''Problem: Create a dictionary: student and perform different operations.'''
'''student = {
    "student1":{
    "name":"Atlas",
    "age":25,
    "marks":98,
    "city":"Delhi"},
    "student2":{
        "name":"Jugnu",
        "age":23,
        "marks":90,
        "city":"Kullu"
    },
    "student3":{
        "name":"Kishan",
        "age":23,
        "marks":99,
        "city":"Jhulanpur"
    },
    "student4":{
        "name":"Tiku",
        "age":25,
        "marks":96,
        "city":"Bhulaan"
    },
    "student5":{
        "name":"Jaggu",
        "age":22,
        "marks":95,
        "city":"Kasauli"
    }
}'''
# print(student["name"],student["marks"])

'''Adding new key'''
#student["city"] = "Delhi"
#print(student)#printing dictionary directly

'''Printing Dictionary using loop'''
# total_marks = 0
# for key in student:
#     print(key,student[key])
#     total_marks += student[key]["marks"]
# print(f"Total marks of all student: {total_marks}")

'''Finding Hightest Mark'''
# hst_mark = 0
# topper_student = ''
# for key in student:
#     if student[key]["marks"] > hst_mark:
#         hst_mark = student[key]["marks"]
#         topper_student = student[key]["name"]
# print(f"Student name: {topper_student}\nHighest mark: {hst_mark}")

'''Finding Average mark'''
# avg_mark = 0
# marks_sum = 0
# for key in student:
#     marks_sum += student[key]["marks"]
# avg_mark = marks_sum/len(student)
# print(avg_mark) 

'''Adding new students using List + Dictionay'''
# new_students = [
#     {"name":"Twinkle","age":20,"marks":92,"city":"Lucknow"},
#     {"name":"Teja","age":24,"marks":95,"city":"Kolhapur"},
#     {"name":"Lisa","age":27,"marks":98,"city":"Tokyo"}
# ]
'''Adding in existing dictionary by giving them id i.e. "student6","student7","student8"'''

# count = len(student)+1
# for id in new_students:
#     key = "student" + str(count)
#     student[key] = id
#     count += 1
'''Printing updated dictionary'''   
# for key in student:
#     print(key,student[key])

'''Creating a dictionary by taking input by user.'''

# new_dict = {}
# numOfStudents = int(input("How many students you want to add?: "))
# for i in range(1,numOfStudents+1):
#     print(f"{i}. Student ki details do: ")
#     name = input("Name:")
#     age = input("Age:")
#     marks = input("Marks:")
#     city = input("City:")
    
    # temp_dict = {
    #     "name":name,
    #     "age":age,
    #     "marks":marks,
    #     "city":city
    # }
    # '''creating keys for new students'''
    #key = "student" + str(i)
    # '''Adding student details in dictionary'''
    #new_dict[key]=temp_dict

# print(new_dict)
#'''Printing dictionary'''
# for key in new_dict:
#     print(f"\nStudent directory:\n{key,new_dict[key]}")