# Array operations in Python

def display_array(arr):
    print("Array elements:", arr)


def insert_element(arr, element):
    arr.append(element)
    return arr


def delete_element(arr, element):
    if element in arr:
        arr.remove(element)
    else:
        print("Element not found")
    return arr


def search_element(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1


# --------- MAIN PROGRAM ---------

arr = [10, 20, 30, 40]

display_array(arr)

arr = insert_element(arr, 50)
display_array(arr)

arr = delete_element(arr, 20)
display_array(arr)

index = search_element(arr, 30)
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found")
