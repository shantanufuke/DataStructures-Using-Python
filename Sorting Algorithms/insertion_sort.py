def insertion_sort(array):
    """
    Perform insertion sort on the given array.

    Parameters:
    array (list): The list of elements to be sorted.

    Returns:
    list: The sorted list.
    """
    n = len(array)  # Get the length of the array
    # Iterate through each element starting from the second element (index 1)
    for i in range(1, n):
        key = array[i]  # The element to be positioned
        j = i - 1       # Index of the last sorted element
        
        # Move elements of array[0..i-1] that are greater than the key
        # one position ahead to make space for the key
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        
        # Place the key in its correct position
        array[j + 1] = key

    return array

# Example usage
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]  # Example unsorted array
    print(f"Original Array: {arr}")
    sorted_arr = insertion_sort(arr)
    print(f"Sorted Array: {sorted_arr}")

