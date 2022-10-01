# Program to check whether the given number is prime or not

num = int(input("Enter a number : "))
n = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            n = True
            break
if n:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
