import re

text = "Welcome to Python Programming"

pattern = "Welcome"

result = re.search(pattern, text)

if result:
    print("Pattern found")
    print("Matched text:", result.group())
else:
    print("Pattern not found")
