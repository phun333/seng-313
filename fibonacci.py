'''
Task: Write a Python function to calculate the nth Fibonacci number using a
recursive approach. Then, analyze the time complexity of this recursive
implementation.
2. Bonus Task: Implement a memoized version of the Fibonacci function to
improve the time complexity. Compare the time complexities of the recursive and
memoized versions.
'''
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # recursive case: sum of the two preceding numbers
        return fibonacci(n - 1) + fibonacci(n - 2)
'''
Time Complexity Analysis

The time complexity of the recursive Fibonacci function is:

    Exponential Growth: Each call to fibonacci(n) results in two more calls (fibonacci(n-1) and fibonacci(n-2)), leading to a tree-like structure of calls.
    The total number of calls made grows exponentially, approximately O(2n)O(2n).

Thus, the time complexity of this recursive implementation is:
O(2^n)
'''

# Memoized Version of the Fibonacci Function #

def fibonacci_memo(n, memo={}):
    # check if the value is already computed
    if n in memo:
        return memo[n]
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # compute and store the result in the memo dictionary
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
        return memo[n]


'''
Comparison of Time Complexities

    Recursive Version:
        Time Complexity: O(2^n) due to the exponential number of calls.
    Memoized Version:
        Time Complexity: O(n) because it computes each Fibonacci number only once and stores it in the memo dictionary. The space complexity is also O(n) due to the storage of computed values.

Summary

    Recursive Fibonacci:
        Time Complexity: O(2^n)

    Memoized Fibonacci:
        Time Complexity: O(n)
        Space Complexity: O(n)

The memoized version significantly improves efficiency, making it feasible to compute larger Fibonacci numbers.
'''

