def print_1_to_n(n):
    if n==0:
        return
    print_1_to_n(n-1)
    print(n)
    return

n = 4
print(print_1_to_n(n))