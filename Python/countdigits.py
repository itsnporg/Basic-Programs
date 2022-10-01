def count_digits(num):
    count = 0
    
    while num != 0:
        num //= 10
        count += 1
    
    print("Number of digits: " + str(count))
    
n = int(input("Enter a number "))
count_digits(n)
