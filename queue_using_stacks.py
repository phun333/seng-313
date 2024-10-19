#Task: Write a Python class that implements a Queue using two stacks. Implement the following methods:
# enqueue(): Adds an element to the queue.
# dequeue(): Removes and returns the front element of the queue.
# Analyze the time complexity for both enqueue and dequeue operations.

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # stack for enqueue operations
        self.stack2 = []  # stack for dequeue operations

    def enqueue(self, item):
        # push the item onto stack1
        self.stack1.append(item)

    def dequeue(self):
        # if stack2 is empty, move elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is still empty, the queue is empty
        if not self.stack2:
            raise IndexError("Dequeue from an empty queue")

        # Pop from stack2 and return the front element
        return self.stack2.pop()

#Time Complexity Analysis:

    #Enqueue Operation:
    # Time Complexity: O(1) since it only involves appending an item to stack1.

    #Dequeue Operation:
    # Time Complexity: Average Case: O(1) for the actual popping from stack2. Worst Case: O(n) when elements are transferred from stack1 to stack2, but this happens infrequently relative to the number of total operations, leading to amortized O(1) time per operation over a series of enqueues and dequeues.