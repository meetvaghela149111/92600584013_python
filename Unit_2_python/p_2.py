#2. Write a program to check whether a number is positive negative or zero using nested conditions.

n=int(input("Enter a Number :"))

if n>=0:
    if n==0:
        print("Number Zero")
    else:
        print("Number Positive")
else:
    print("NUmber Negative")
