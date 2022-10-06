def arrsum(a):
    l = len(a)
    if l==1:
        return a[0]
    else:
        return a[0] + arrsum(a[1:])

a = [9,8,9]
print(arrsum(a))