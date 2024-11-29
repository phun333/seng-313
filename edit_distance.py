def edit_distance(str1, str2):
    """
    Computes the minimum edit distance between two strings using dynamic programming.
    Edit operations: insertion, deletion, substitution
    
    Args:
        str1 (str): First string
        str2 (str): Second string
    
    Returns:
        int: Minimum number of operations required to convert str1 to str2
    """
    m, n = len(str1), len(str2)
    
    # Create a 2D DP table with space optimization (only 2 rows needed)
    # dp[i][j] represents minimum operations needed to convert str1[0:i] to str2[0:j]
    dp = [[0] * (n + 1) for _ in range(2)]
    
    # Initialize first row - converting empty string to str2
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the dp table
    for i in range(1, m + 1):
        dp[1][0] = i  # Initialize first column of current row
        
        for j in range(1, n + 1):
            # If characters match, no operation needed
            if str1[i-1] == str2[j-1]:
                dp[1][j] = dp[0][j-1]
            else:
                # Take minimum of three operations:
                dp[1][j] = 1 + min(
                    dp[0][j],      # deletion
                    dp[1][j-1],    # insertion
                    dp[0][j-1]     # substitution
                )
        
        # Copy current row to previous row for next iteration
        dp[0] = dp[1][:]
    
    return dp[1][n]

# Test the implementation
if __name__ == "__main__":
    # Example problem:
    # Convert "sunday" to "saturday"
    # Expected output: 3 operations
    
    str1 = "sunday"
    str2 = "saturday"
    print(f"Edit distance between '{str1}' and '{str2}': {edit_distance(str1, str2)}")

# Time complexity: O(m*n) where m and n are lengths of input strings
# Space complexity: O(n) with space optimization (only 2 rows needed) 