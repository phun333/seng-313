def knapsack(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using dynamic programming.
    
    Args:
        weights (list): List of item weights
        values (list): List of item values
        capacity (int): Maximum weight capacity of knapsack
    
    Returns:
        tuple: (maximum value possible, list of selected items)
    """
    n = len(weights)
    # Create a 2D DP table with dimensions (n+1) x (capacity+1)
    # dp[i][w] represents the maximum value that can be achieved with first i items and weight limit w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    selected = []
    
    # Fill the dp table using bottom-up approach
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # If current item can fit in the knapsack
            if weights[i-1] <= w:
                # Two choices:
                # 1. Include current item: values[i-1] + dp[i-1][w-weights[i-1]]
                # 2. Exclude current item: dp[i-1][w]
                # Take maximum of these two choices
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], 
                             dp[i-1][w])
            else:
                # If current item is too heavy, skip it and use previous value
                dp[i][w] = dp[i-1][w]
    
    # Backtrack to find selected items
    # Start from the bottom-right cell of dp table
    w = capacity
    for i in range(n, 0, -1):
        # If value changed from previous row, item was selected
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)  # Add item index to selected list
            w -= weights[i-1]     # Reduce remaining capacity
    
    return dp[n][capacity], selected

# Test the implementation
if __name__ == "__main__":
    # Example problem:
    # Items: [0, 1, 2, 3]
    # Weights: [2, 3, 4, 5]
    # Values: [3, 4, 5, 6]
    # Knapsack capacity: 5
    
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    # Get maximum value and selected items
    max_value, selected_items = knapsack(weights, values, capacity)
    
    # Print results
    print(f"Maximum value: {max_value}")
    print(f"Selected items: {selected_items}")
    
    # Print selected items details
    print("\nSelected items details:")
    for item in selected_items:
        print(f"Item {item}: weight = {weights[item]}, value = {values[item]}")

# Time Complexity: O(n * capacity) where n is number of items
# Space Complexity: O(n * capacity) for the dp table 