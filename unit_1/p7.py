#7

meet = {
    "Name" : "Meet",
    "Age": 20,
    "City": "Rajkot"
    }
print("Dictionry :",meet)

print("Keys :",meet.keys())
print("Values :",meet.values())
print("Items :",meet.items())
print("get method :",meet.get("Name"))

meet.update({"Collage": "Marwadi"})
print("After update :",meet)

remove=meet.pop("Age")
print("Remove Age :",remove)
print(meet)

meet.setdefault("Course","MCA")
print("After :",meet)

print("\n Values :")
for value in meet.items():
    print(value)

print("\n Keys :")
for key in meet.items():
    print(key)

print("\nKey Values pair :")
for key,value in meet.items():
    print(key,":",value)

print("\nis 'Name' in ?","Name" in meet)
print("Length :",len(meet))
