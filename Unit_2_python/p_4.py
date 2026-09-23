#4 Write a program to find the sum of digits of a number using a while loop.
'''
n=int(input("Enter Number :"))


sum=0

while n>0:
    m=n%10
    sum=sum+m
    num=n // 10

print("sum of =",sum)
'''

num = int(input("Enter a number: "))

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum of digits =", sum)
