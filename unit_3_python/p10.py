import os
import re

with open("data.txt", "w") as f:
    f.write("Name: Meet\nAge: 21\nEmail: meet@gmail.com\nPhone: 8401368311\n")

with open("data.txt", "r") as f:
    text = f.read()

name = re.findall(r"Name:\s*(.*)", text)
age = re.findall(r"Age:\s*(\d+)", text)
email = re.findall(r"Email:\s*([\w.-]+@[\w.-]+)", text)
phone = re.findall(r"Phone:\s*(\d+)", text)

print("Name:", name[0])
print("Age:", age[0])
print("Email:", email[0])
print("Phone:", phone[0])

os.remove("data.txt")
print("Test File deleted successfully")
