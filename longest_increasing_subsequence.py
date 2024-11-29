def longest_increasing_subsequence(arr):
    """
    Finds the length of the longest increasing subsequence in an array.
    
    Args:
        arr (list): Input array of integers
    
    Returns:
        int: Length of the longest increasing subsequence
    """
    if not arr:
        return 0
        
    # Create dp array where dp[i] represents the length of LIS ending at index i
    # Initialize with 1 as each element alone is an increasing subsequence
    dp = [1] * len(arr)
    
    # For each position, look at all previous positions
    for i in range(1, len(arr)):
        for j in range(i):
            # If current element is greater than previous element
            # We can extend the subsequence ending at j
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum value in dp array
    return max(dp)

# Test the implementation
if __name__ == "__main__":
    # Example problem:
    # Input: [10,9,2,5,3,7,101,18]
    # Expected output: 4 (The LIS is [2,5,7,101])
    
    arr = [10,9,2,5,3,7,101,18]
    print(f"Input array: {arr}")
    print(f"Length of LIS: {longest_increasing_subsequence(arr)}")

# Time complexity: O(n^2) where n is the length of input array
# Space complexity: O(n) for the dp array 