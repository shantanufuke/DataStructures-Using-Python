def selectionSort(array):
    """
    Perform selection sort on the given array.

    Parameters:
    array (list): The list of elements to be sorted.

    Returns:
    list: The sorted list.
    """
    n = len(array)  # Get the length of the array

    # Loop over the entire array
    for i in range(n):
        # Assume the current index is the minimum
        min_index = i

        # Find the index of the smallest element in the remaining unsorted part of the array
        for j in range(i, n):
            if array[j] < array[min_index]:
                min_index = j

        # Swap the smallest element with the first element of the unsorted part
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp

    return array

# Example usage
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]  # Example unsorted array
    print(f"Original Array: {arr}")
    sorted_arr = selectionSort(arr)
    print(f"Sorted Array: {sorted_arr}")
