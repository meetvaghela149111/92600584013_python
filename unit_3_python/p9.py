import re

text = "Python is easy. Python is powerful."

result1 = re.match("Python", text)
if result1:
    print("Match:", result1.group())

result2 = re.search("easy", text)
if result2:
    print("Search:", result2.group())

result3 = re.findall("Python", text)
print("Findall:", result3)
