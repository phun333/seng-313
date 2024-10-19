def merge_sort(arr):
    # if the array has one or no elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # divide the array into two halves
    mid = len(arr) // 2  # find the middle index
    left_half = merge_sort(arr[:mid])  # recursively sort the left half
    right_half = merge_sort(arr[mid:])  # recursively sort the right half

    # merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    # this function merges two sorted lists into one sorted list
    merged = []  # list to store the merged results
    left_index, right_index = 0, 0  # initialize pointers for both halves

    # compare elements from both halves and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])  # append smaller element
            left_index += 1  # move pointer in left half
        else:
            merged.append(right[right_index])  # append smaller element
            right_index += 1  # move pointer in right half

    # if there are remaining elements in left half, add them to merged
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # if there are remaining elements in right half, add them to merged
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged  # return the merged sorted list


'''Explanation of Implementation

    Base Case: If the array has one or no elements, it is already sorted, so we return it.
    Divide: The array is split into two halves, which are then sorted recursively using the same merge_sort function.
    Merge: The merge function combines two sorted arrays into one sorted array by comparing their elements.

2. Time and Space Complexity Analysis
Time Complexity

    Dividing: The array is divided in half recursively until we reach base cases, which takes O(log⁡n)O(logn) levels of recursion.
    Merging: Merging two sorted arrays takes linear time, O(n)O(n), for each level of recursion.
    Overall: The overall time complexity of Merge Sort is:

O(n log ⁡n)

Space Complexity

    Auxiliary Space: Merge Sort requires additional space for the temporary arrays used during the merging process. The space needed for merging is proportional to the size of the input array.
    Overall: The overall space complexity of Merge Sort is:

O(n)

Summary

    Time Complexity: O(n log ⁡n)
    Space Complexity: O(n)O(n)

Merge Sort is efficient for large datasets and is a stable sorting algorithm, making it a great choice for many applications.
'''