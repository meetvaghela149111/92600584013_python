#6

m = (10, 20, 30, 40, 50)

print("Tuple:", m)
print("First element:", m[0])
print("Length:", len(m))
print("Count of 20:", m.count(20))
print("Index of 30:", m.index(30))

#sets

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

print("Set 1:", a)
print("Set 2:", b)

a.add(70)
print("After adding 70:", a)

a.remove(70)
print("After removing 70:", a)

print("Union:", a.union(b))

print("Intersection:", a.intersection(b))

print("Difference:", a.difference(b))
