#Task: For the following Python function, calculate the time complexity:

def find_duplicates(arr):
    duplicates = []

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                duplicates.append(arr[i])

    return duplicates

''' Step-by-Step Analysis

    Initialization:
        We create an empty list called duplicates to hold the duplicate values found in the input array arr.

    Outer Loop:
        The outer loop runs from i = 0 to len(arr) - 1. This means it will iterate through each element of the array. If n is the length of arr, this loop runs n times.

    Inner Loop:
        The inner loop starts from j = i + 1 and runs to len(arr) - 1. For each element arr[i], it compares it with all subsequent elements in the array. The number of iterations of the inner loop decreases with each iteration of the outer loop.
        Specifically, when i = 0, the inner loop runs n - 1 times, when i = 1, it runs n - 2 times, and so on, down to 1 time when i = n - 2.

    Comparison:
        For each pair of elements (arr[i], arr[j]), we check if they are equal. If they are, we append arr[i] to the duplicates list.

    Return:
        Finally, the function returns the duplicates list, which contains all found duplicates.

Time Complexity Analysis

    Outer Loop: Executes n times (for each element).

    Inner Loop: The number of executions decreases as i increases. The inner loop runs a total of:
    (n−1)+(n−2)+(n−3)+...+1=n(n−1)2
    (n−1)+(n−2)+(n−3)+...+1=2n(n−1)​

    This is the sum of the first n-1 natural numbers.

    The inner loop, therefore, contributes a time complexity of O(n2).

Final Time Complexity

Considering both loops, the overall time complexity of the find_duplicates function is:
Time Complexity=O(n^2)

Conclusion

This O(n^2) complexity arises because we are using a nested loop approach to compare each pair of elements in the array. This approach can be inefficient for large arrays. For a more efficient solution, consider using a hash set to keep track of seen elements, which would reduce the time complexity to O(n)O(n).'''
