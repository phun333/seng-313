import heapq
from collections import defaultdict

class Node:
    """
    Node class for Huffman tree.
    """
    def __init__(self, char, freq):
        self.char = char    # Character stored in node
        self.freq = freq    # Frequency of character
        self.left = None    # Left child
        self.right = None   # Right child
    
    def __lt__(self, other):
        # Comparison method for priority queue
        return self.freq < other.freq

def build_huffman_tree(chars, freqs):
    """
    Builds a Huffman tree from characters and their frequencies.
    
    Args:
        chars (list): List of characters
        freqs (list): List of corresponding frequencies
    
    Returns:
        Node: Root node of Huffman tree
    """
    # Create a min heap of nodes
    heap = []
    for char, freq in zip(chars, freqs):
        heapq.heappush(heap, Node(char, freq))
    
    # Build tree by combining nodes
    while len(heap) > 1:
        # Get two nodes with minimum frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create internal node with these two as children
        internal = Node(None, left.freq + right.freq)
        internal.left = left
        internal.right = right
        
        # Add new internal node back to heap
        heapq.heappush(heap, internal)
    
    return heap[0]  # Return root of Huffman tree

def generate_codes(root, code="", codes=None):
    """
    Generates Huffman codes for each character by traversing the tree.
    
    Args:
        root (Node): Current node in Huffman tree
        code (str): Current code string (path to node)
        codes (dict): Dictionary to store character-code mappings
    
    Returns:
        dict: Dictionary mapping characters to their Huffman codes
    """
    if codes is None:
        codes = {}
    
    if root is not None:
        # If leaf node, store the code
        if root.char is not None:
            codes[root.char] = code
        # Recurse left (add '0' to code)
        generate_codes(root.left, code + "0", codes)
        # Recurse right (add '1' to code)
        generate_codes(root.right, code + "1", codes)
    
    return codes

# Test the implementation
if __name__ == "__main__":
    # Example problem:
    # Characters: a, b, c, d, e, f
    # Frequencies: 5, 9, 12, 13, 16, 45
    
    chars = ['a', 'b', 'c', 'd', 'e', 'f']
    freqs = [5, 9, 12, 13, 16, 45]

    # Build Huffman tree and generate codes
    root = build_huffman_tree(chars, freqs)
    codes = generate_codes(root)
    
    # Print results
    print("Huffman Codes:")
    for char in chars:
        print(f"{char}: {codes[char]}")

# Time complexity: O(n log n) where n is number of characters
# Space complexity: O(n) for storing the Huffman tree 