def count_zero(n):
    if n == 0:
        return 0
    
    if n%10==0:
        return 1 + count_zero(int(n/10))
    else:
        return count_zero(int(n/10))

n = 405004020
print(count_zero(n))