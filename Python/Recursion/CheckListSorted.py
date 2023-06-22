def isSorted(a, si):
#     si = start index
    l = len(a)
    if si == l-1 or si==l:
        return True
    if a[si]>a[si+1]:
        return False
    return isSorted(a, si+1)

a = [1,2,3,4,5]
print(isSorted(a, 0))