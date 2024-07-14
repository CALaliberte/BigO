# The linear_search function is optimized using a dictionary (index_dict) to store the index of each element in the array.
# This allows for constant time (O(1)) lookup of the target element, improving the overall efficiency of the function.
# If the target element is not found in the array, the function returns -1.

def linear_search(arr, target):
    index_dict = {val: idx for idx, val in enumerate(arr)}
    return index_dict.get(target, -1)


# It iterates through the array multiple times, comparing adjacent elements and swapping them if they are in the wrong order.
# The function stops early if no swaps are made during a pass, indicating that the array is already sorted.
# This optimization reduces unnecessary iterations and improves the overall efficiency of the function.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr