def bubble_sort(array):
    """
    Perform Bubble Sort on the given array.

    Bubble Sort is a simple sorting algorithm that repeatedly steps through 
    the list, compares adjacent elements, and swaps them if they are in the 
    wrong order. The process is repeated until the list is sorted.

    Parameters:
        array (list): The list of elements to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """
    n = len(array)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(n - i - 1):
            # Swap if the element found is greater than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


# Example usage
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    print(f"Original Array: {arr}")
    sorted_arr = bubble_sort(arr)
    print(f"Sorted Array: {sorted_arr}")
