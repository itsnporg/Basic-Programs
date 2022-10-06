def towerofhanoi(n,source,destination,auxiliary):
    if n==1:
        print(source,destination)
        return
    towerofhanoi(n-1,source,auxiliary,destination)
    print(source,auxiliary)
    towerofhanoi(n-1,auxiliary,destination,source)

n = 3
source = "a"
auxiliary = "b"
destination = "c"
print(towerofhanoi(n,source,auxiliary,destination))