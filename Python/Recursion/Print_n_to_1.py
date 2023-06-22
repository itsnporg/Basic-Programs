def print_n_to_1(n):
    if n==0:
        return
    print(n)
    print_n_to_1(n-1)

n = 5
print(print_n_to_1(n))