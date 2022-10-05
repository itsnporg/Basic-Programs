# A number that equals to the sum of its own digits, where each digit raised to the power of number of digits is known as Armstrong Number.

num = int(input("Enter the Number: "))

temp = num
noOfDigit = 0
res = 0
while num>0:
    num = int(num/10)
    noOfDigit = noOfDigit+1
num = temp
while num>0:
    rem = num%10
    pow = 1
    i = 0
    while i<noOfDigit:
        pow = pow*rem
        i = i+1
    res = res+pow
    num = int(num/10)

if res==temp:
    print("\nThe number is an Armstrong Number")
else:
    print("\nThe number is not an Armstrong Number")
