#Calculate factorial using recursive function
n=int(input("Enter a number: "))
def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
# Prints the Factorial !
print("Factorial of",n,"is",factorial(n))