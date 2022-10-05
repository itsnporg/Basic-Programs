import math
numbers = [1,2,4,3,7,5,6,8,9,10]
numbers.sort()
target = 5
def search(arr):
    low = 0
    high = len(arr) - 1
    mid = math.floor((low+high)/2)
    while low <= high:
        if arr[mid] == target:
            print("Found target")
            break
        elif arr[mid] < target:
            low = mid +1
            mid = math.floor((low+high)/2)
        elif arr[mid] > target:
            high = mid -1
            mid = math.floor((low+high)/2)
        else:
            print("Number Not Found")
search(numbers)