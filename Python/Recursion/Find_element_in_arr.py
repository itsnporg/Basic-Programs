def findarr(a,x):
    l = len(a)
    if l==0:
        return False
    if a[0]==x:
        return True
    return findarr(a[1:],x)

a = [1,2,3,4,5,6]
x = 6
print(findarr(a,x))