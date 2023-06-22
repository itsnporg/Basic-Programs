def mul(m,n):
    if n==0:
        return 0
    a = mul(m,n-1)
    return a + m

print(mul(5,4))