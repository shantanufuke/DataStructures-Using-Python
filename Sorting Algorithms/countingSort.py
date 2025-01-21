def coutingSort(array):
    # Find the maximum element in the array to determine the range of the count array
    max_element = max(array)

    # Initialize the count array with zeros, sized to the range of input elements
    count_array = [0] * (max_element + 1)

    # Initialize the result array to store the sorted elements
    result = [0] * len(array)
    
    # Count the occurrences of each element in the input array
    for element in array:
        count_array[element] += 1
   
    # Update the count array to store cumulative counts
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    # Place elements into the result array in sorted order
    # Iterate backward through the input array to maintain stability
    for i in range(len(array) - 1, -1, -1):
        element = array[i]
        index = count_array[element]  # Get the cumulative index for the element
        result[index - 1] = element  # Place the element at the correct position in the result array
        count_array[element] -= 1  # Decrement the count for the element

    return result

# Example usage
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]  # Example unsorted array
    print(f"Original Array: {arr}")
    sorted_arr = coutingSort(arr)
    print(f"Sorted Array: {sorted_arr}")
