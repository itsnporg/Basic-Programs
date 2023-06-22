def fib(n):
    if n==1 or n==2:
        return 1
    output = fib(n-1) + fib(n-2)
    return output

n=6
print(fib(n))