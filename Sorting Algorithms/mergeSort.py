def mergeSort(array, left, right):
    # Check if the array has more than one element
    if left < right:
        # Find the middle point of the array
        mid = (left + right) // 2

        mergeSort(array, left, mid)
        mergeSort(array, mid + 1, right)
        merge(array, left, mid, right)


def merge(array, left, mid, right):
    # Create temporary arrays for the two halves
    leftArray = array[left: mid + 1]
    rightArray = array[mid + 1: right + 1]

    # Initialize indices for iteration
    i, j, k = 0, 0, left

    # Merge the two arrays back into the original array
    while i < len(leftArray) and j < len(rightArray):
        # Choose the smaller element and place it in the original array
        if leftArray[i] < rightArray[j]:
            array[k] = leftArray[i]
            i += 1
        else:
            array[k] = rightArray[j]
            j += 1
        k += 1

    # Copy any remaining elements from the left array
    while i < len(leftArray):
        array[k] = leftArray[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right array
    while j < len(rightArray):
        array[k] = rightArray[j]
        j += 1
        k += 1


# Example usage
if __name__ == "__main__":
    # Define an example unsorted array
    arr = [5, 4, 3, 2, 1]  
    print(f"Original Array: {arr}")
    mergeSort(arr, 0, len(arr) - 1)
    print(f"Sorted Array: {arr}")
