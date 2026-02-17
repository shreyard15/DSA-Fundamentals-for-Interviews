# Linear Search Implementation

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Example usage
numbers = [10, 20, 30, 40, 50]
result = linear_search(numbers, 30)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
