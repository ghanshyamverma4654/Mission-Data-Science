'''Dictionary Mastery'''
#Dictionary Problems
'''Problem: Create a dictionary: student and perform different operations.'''
student = {
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
        "marks":99,
        "city":"Bhulaan"
    },
    "student5":{
        "name":"Jaggu",
        "age":22,
        "marks":95,
        "city":"Kasauli"
    }
}
# print(student["name"],student["marks"])

#Adding new key
#student["city"] = "Delhi"
#print(student)#printing dictionary directly

#Printing Dictionary using loop
total_marks = 0
for key in student:
    print(key,student[key])
    total_marks += student[key]["marks"]
print(f"Total marks of all student: {total_marks}")