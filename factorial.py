#Write a program to print the factorial of numbers from 1 to 10

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

for i in range(1, 11):
    print("Factorial of", i, "is", factorial(i))