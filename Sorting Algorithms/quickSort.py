def partition(array, left, right):
    pivot = array[right]
    
    i = left - 1

    # Iterate through the array from 'left' to 'right - 1'
    for j in range(left, right):
        # If the current element is smaller than the pivot, swap it with the element at 'i + 1'
        if array[j] < pivot:
            i += 1
            # Swap array[i] and array[j] to move smaller elements to the left
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    
    i += 1
    temp = array[i]
    array[i] = array[right]
    array[right] = temp

    return i

def quickSort(array, left, right):
    # If the subarray has more than one element
    if left < right:
        # Find the pivot index after partitioning
        pivot = partition(array, left, right)
        
        # Recursively sort the left and right subarrays
        quickSort(array, left, pivot - 1)  # Sort the left subarray
        quickSort(array, pivot + 1, right)  # Sort the right subarray

if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]  
    print(f"Original Array: {arr}")
    quickSort(arr, 0, len(arr) - 1)
    print(f"Sorted Array: {arr}")
