import time
import bisect
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
def binary_search(arr, x, low, high):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, x, low, mid - 1)
        else:
            return binary_search(arr, x, mid + 1, high)
    else:
        return -1
arr = list(range(1, 1000001))  # Large sorted array
x = 999999
start = time.time()
print("Linear Search Result:", linear_search(arr, x))
end = time.time()
print("Linear Search Time:", end - start, "seconds")
start = time.time()
print("Binary Search Result:", binary_search(arr, x, 0, len(arr)-1))
end = time.time()
print("Binary Search Time:", end - start, "seconds")
