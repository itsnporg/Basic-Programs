def binarySearch(a,x,si,ei):
    if si>ei:
        return -1
    mid = (si+ei)//2
    if a[mid]==x:
        return mid
    elif a[mid]>x:
        return binarySearch(a,x,si,mid-1)
    else:
        return binarySearch(a,x,mid+1,ei)

a=[1,4,5,6,8,9,12,14,15,16,17,19]
x=15
ei = len(a)-1
print(binarySearch(a, x, 0, ei))