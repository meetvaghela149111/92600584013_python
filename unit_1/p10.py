#10

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

num=int(input("Enter number :"))
show=fact(num)

print("Factorial",num,"is",show)


