def find_primes(lower, num2):
    prime_numbers = []
    for num in range(lower, num2 + 1):
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)
    return prime_numbers

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2st number: "))
if (num1 > num2) or num1<0 >num2  : 
    print("Please Enter Right Number")
else:
    print("Prime numbers between", num1, "and", num2, "are:", find_primes(num1, num2))