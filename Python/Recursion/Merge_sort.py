def merge(a1,a2,a):
    i = 0
    j = 0
    k = 0
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            a[k] = a1[i]
            k= k+1
            i = i+1
        else:
            a[k]=a2[j]
            k=k+1
            j=j+1
            
    while i<len(a1):
        a[k] = a1[i]
        k= k+1
        i = i+1
    
    while j<len(a2):
        a[k]=a2[j]
        k=k+1
        j=j+1

def merge_sort(a):
    if len(a)==0 or len(a)==1:
        return
    mid = len(a)//2
    a1 = a[0:mid]
    a2 = a[mid:]
    
    merge_sort(a1)
    merge_sort(a2)
    
    merge(a1,a2,a)

a = [7,3,9,4,1,8,5,2,6]
merge_sort(a)
print(a)