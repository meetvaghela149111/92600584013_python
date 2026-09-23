#6 Write a program to iterate over lists strings and dictionaries using loops.

# List
numbers = [10, 20, 30, 40]

print("List:")
for n in numbers:
    print(n)


# String
name = "Python"

print("String:")
for ch in name:
    print(ch)


# Dictionary
student = {
    "name": "Meet",
    "age": 21,
    "course": "Python"
}

print("Dictionary:")
for key, value in student.items():
    print(key, ":", value)
