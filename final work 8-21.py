#Ex 8:
student = {
         'name': 'John',
          'age': 20,
        'hobbies': ['reading', 'games', 'coding'],
}
#1
print("Ex 8:")
print("all the student data:")
def print_student_data(student):
    for key, value in student.items():
        print(f"{key}: {value}")
print_student_data(student)
print()

#2
"""student's hobbies array if it’s not exist already"""
def new_hobby(student, hobbies):
    if hobbies not in student["hobbies"]:
        student["hobbies"].append(hobbies)
new_hobby(student, "cooking")
#3
print("added new hobby:")
print_student_data(student)

#4
def del_hobby(student, hobbies):
    if hobbies in student["hobbies"]:
        student["hobbies"].remove(hobbies)
del_hobby(student, 'reading')
print()

#5
print("Student after deleting one hobby:")
print_student_data(student)
print()

#6
student["family_name"] = "bond"
print("student new property after adding family name:")
print_student_data(student)
print()

#Ex 9:
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print("Ex 9: matrix=", end=" ")
def print_matrix(matrix):
    for row in matrix:
        for matrix in row:
         print(matrix, end=" ")
    print()
print()
print_matrix(matrix)

#Ex 10:
matrix =[
[0,1,1],
[0,1,0],
[1,0,0]
]
def zero_count(matrix):
    count = 0
    for row in matrix:
        for counter in row:
            if counter == 0:
                count += 1
    return count

print("Ex 10: matrix count=",zero_count(matrix))
print()

#Ex 11:
arr = [4,2,34,4,1,12,1,4]

def repeated_more_once(arr):
    duplicates = []
    for i in range(len(arr)):
        for _ in range(i + 1, len(arr)):
            if arr[i] == arr[_] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates

print("Ex 11: repeated more than once=",repeated_more_once(arr))
print()

#Ex 12:
def appearing_in_reverse(array):
    reverse = []
    for i in range(len(array) - 1, -1, -1):
        reverse.append(array[i])
    return reverse

array = [43, "what", 9, True, "cannot", False, "be", 3, True]
print("Ex 12:",appearing_in_reverse(array))
print()

#Ex 13:
def sum_arrays(first_array, second_array):
    sum = []
    for i in range(len(first_array)):
        sum.append(first_array[i] + second_array[i])
    return sum

first_array = [4, 6, 7]
second_array = [8, 1, 9]
print("Ex 13:",sum_arrays(first_array, second_array))
print()

#Ex 14:
first_str = "racecar"
second_str = "Java"
print("Ex 14:")
print(f"{first_str} is a palindrome? {first_str == "racecar"[::-1]}")
print(f"{second_str} is a palindrome? {second_str== "java"[::-1]}")
print()

#Ex 15:
counter = 1
print("Ex 15:")

while counter < 100:
    print(counter, " ", end=" ")
    counter *= 2
print()
print()

#Ex 16:
counter = 900000
print("Ex 16:")
while counter > 50:
    print(counter, " ", end=" ")
    counter //= 2
print()
print()

#Ex 17:
def while_more_than_once(array_str):
    duplicates = []
    counter= []
    x = 0

    while x < len(array_str):
        array_strings = array_str[x]
        if array_strings not in counter:
            count = 0
            y = 0
            while y < len(array_str):
                if array_str[y] == array_strings:
                    count += 1
                y += 1
            if count > 1:
                duplicates.append(array_strings)
            counter.append(array_strings)
        x += 1
    return duplicates

fruits = ["watermelon", "grapes", "pineapple", "apple", "strawberries", "banana", "watermelon", "grapes", "pineapple", "strawberries"]
print("Ex 17:",while_more_than_once(fruits))
print()

#Ex 18:
def without_any_duplicated(array_str):
    without_duplicates = []
    i=0
    while i < len(array_str):
        array_strings = array_str[i]
        if array_strings not in without_duplicates:
            without_duplicates.append(array_strings)
        i += 1
    return without_duplicates

fruits =  ["watermelon", "grapes", "pineapple", "apple", "strawberries", "banana", "watermelon", "grapes", "pineapple", "strawberries"]
print("Ex 18:", without_any_duplicated(fruits))
print()

#Ex 19:
def without_any_duplicated(array, name_str):
    without_duplicated = []
    i = 0
    while i < len(array):
        array_string = array[i]
        if array_string != name_str and array_string not in without_duplicated:
            without_duplicated.append(array_string)
        i += 1
    return without_duplicated


name_str = 'Pete'
names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']

print("Ex 19:", without_any_duplicated(names, name_str))
print()

#Ex 20:
def boolean_array_loop(array):
    i = 1

    while i < len(array):
        if array[i] == array[i - 1]:
            return i
        i += 1
    else:
        return -1

array1 = [True, False, False, True, True, False]
array2 = [True, False, True, False, True, True]
array3 = [True, False, True, False, True, False]

print("Ex 20:")
print(boolean_array_loop(array1)),print(boolean_array_loop(array2)),print(boolean_array_loop(array3))

#Ex 21:
def input_full_name():
    while True:
        full_name = str(input("enter full name: "))
        if len(full_name.split()) == 2:
            return full_name
        else:
            print("Invalid input.enter two words for First and Last name")

def input_age():
    while True:
            age = int(input("enter age:"))
            if 1 <= age <= 130:
                return age
            else:
                print("Invalid input.enter age 1-130")

def input_email():
    while True:
        email = input("enter email:")
        if '@' in email:
            return email
        else:
            print("Invalid input.Enter an email containing the '@' sign")

def user_input():
    print("Ex 21:")
    full_name = input_full_name()
    age = input_age()
    email = input_email()

    print(f"Full Name: {full_name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
print()
user_input()

