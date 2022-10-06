def sum_int(n):
    if n==0:
        return 0
    return (n%10 + sum_int(int(n/10)))

n =12345
print(sum_int(n))