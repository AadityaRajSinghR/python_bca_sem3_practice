# divisible by 3 and 5 for a given number

def result(num1, num2):
    for i in range(num1, num2+1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)
            return

num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))

result(num1, num2)
