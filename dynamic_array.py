'''
Task: Simulate a dynamic array in Python that resizes itself when it reaches
capacity (doubling its size). Implement a function to perform a sequence of
insertions and print the array’s capacity after each insertion. Analyze the
amortized cost of insertions and explain how the amortized analysis ensures
that the average insertion time is O(1).
'''
class DynamicArray:
    def __init__(self):
        self.size = 0  # number of elements in the array
        self.capacity = 1  #initial capacity of the array
        self.array = [None] * self.capacity  # create an array with initial capacity

    def insert(self, value):
        if self.size == self.capacity:
            self._resize()  # resize the array if capacity is reached

        # new value
        self.array[self.size] = value
        self.size += 1  # increment the size

        print(f"Inserted {value}, Capacity: {self.capacity}")

    def _resize(self):
        # double the capacity
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity  # create a new array with increased capacity
        
        # copy elements to the new array
        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array  # update reference to the new array
        self.capacity = new_capacity  # update capacity
'''
Explanation of the Implementation

    Dynamic Array Class:
        Initializes with a size of 0 and a capacity of 1.
        When inserting an element, if the size reaches the capacity, it calls the _resize() method.

    Insert Method:
        Inserts the new value at the current size index and increases the size.
        Prints the current capacity after each insertion.

    Resize Method:
        Doubles the current capacity and copies existing elements to the new array.

Amortized Cost of Insertions
Amortized Analysis

    Regular Insertions: Most insertions occur in constant time, O(1), when there is space in the array.
    Resizing: When the capacity is reached, resizing takes O(n) time because it involves copying all existing elements to the new array.

Analyzing Amortized Cost

To analyze the amortized cost over multiple insertions:

    Cost Breakdown:
        Let's say we perform nn insertions.
        The total cost involves nn insertions at O(1) each, plus a few costly resize operations.
        The total cost of resizing happens at specific intervals, approximately after every 2k2k insertions (1, 2, 4, 8, ...).

    Total Cost Calculation:
        For nn insertions, the total cost is:
        O(1)+O(1)+O(1)+…+O(n) (from resizing)≤O(n)
        O(1)+O(1)+O(1)+…+O(n) (from resizing)≤O(n)
        The most expensive resizing (copying all elements) occurs only a few times.

    Amortized Cost:
        The average cost per insertion, considering both the regular and occasional resizing, is:
        O(n)/n=O(1)


Conclusion

The amortized analysis shows that even though some insertions may take longer due to resizing, the average time per insertion remains O(1). This ensures that, over a sequence of insertions, the dynamic array operates efficiently, maintaining performance as it grows.
'''