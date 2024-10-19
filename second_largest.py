#Task: Write a Python function to find the second largest element in an unsorted list of integers. Analyze the time complexity of your implementation

def second_largest(nums):
    if len(nums) < 2:
        return None  # not enough num in nums

    # empty values
    first = second = None

    for num in nums:
        if first is None or num > first:
            second = first  # update second largest num
            first = num  # update first largest num
        elif num != first and (second is None or num > second):
            second = num  # if value bigger than first but larger than second, just update second value

    return second  # return second largest number or none


##Time Complexity Analysis:

#Time Complexity: The time complexity of this implementation is O(n), where n is the number of elements in the list. This is because we iterate through the list exactly once.

#Space Complexity: The space complexity is O(1) since we are using a constant amount of space regardless of the input size (just a few integer variables).