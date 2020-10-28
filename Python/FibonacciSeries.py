'''
This is a program that prints the Fibonacci Series to the nth digit
according to the users input.

Fibonacci Series is a series of numbers such that each number is a sum of
the two preceding numbers before it.

Fibonacci Series - 1,1,2,3,5,8......

'''

n = int(input("Number of terms to be printed : "))

n1,n2 = 0,1
count = 0

# Checks whether the input is invalid 
if n<=0:
    print("Input a positive integer")
elif n==1:
    print(f"Fibonacci Series => {n1}")
else:
    print(f"Fibonacci Series => ",end="")
    while count < n:
        print(n1,end=" ")
        # Calculating the next term
        nth = n1+n2
        # Updating the terms
        n1,n2 = n2,nth
        count+=1
