"""
Huffman Coding - Optimal compression algorithm
"""

import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(text):
    """
    Build Huffman tree and generate encoding.
    Greedy: Always merge two smallest frequencies.
    """
    # Count frequencies
    freq = Counter(text)
    
    # Edge case: single character
    if len(freq) == 1:
        return {list(freq.keys())[0]: '0'}, freq
    
    # Build heap of nodes
    heap = [HuffmanNode(f, char=c) for c, f in freq.items()]
    heapq.heapify(heap)
    
    # Build tree: always merge two smallest
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        parent = HuffmanNode(
            left.freq + right.freq,
            left=left,
            right=right
        )
        heapq.heappush(heap, parent)
    
    root = heap[0]
    
    # Generate codes
    codes = {}
    def generate_codes(node, code=''):
        if node.char:  # Leaf node
            codes[node.char] = code or '0'
        else:
            if node.left:
                generate_codes(node.left, code + '0')
            if node.right:
                generate_codes(node.right, code + '1')
    
    generate_codes(root)
    return codes, freq

def huffman_compress(text):
    """Compress text using Huffman encoding."""
    codes, freq = huffman_encoding(text)
    
    compressed = ''.join(codes[c] for c in text)
    
    return compressed, codes, freq

def huffman_decompress(compressed, codes):
    """Decompress Huffman encoded text."""
    reverse_codes = {v: k for k, v in codes.items()}
    
    current = ''
    result = []
    
    for bit in compressed:
        current += bit
        if current in reverse_codes:
            result.append(reverse_codes[current])
            current = ''
    
    return ''.join(result)

# Example 1: Basic Huffman encoding
print("=== Huffman Encoding ===\n")

text = "hello world"
print(f"Original text: '{text}'")
print(f"Length: {len(text)} characters\n")

codes, freq = huffman_encoding(text)

print("Character frequencies:")
for char, f in sorted(freq.items()):
    print(f"  '{char}': {f}")

print("\nHuffman codes:")
for char, code in sorted(codes.items()):
    print(f"  '{char}': {code}")

compressed, codes, freq = huffman_compress(text)
print(f"\nCompressed: {compressed}")
print(f"Compressed length: {len(compressed)} bits")
print(f"Original length: {len(text) * 8} bits")
print(f"Compression ratio: {len(compressed) / (len(text) * 8):.2%}")

# Decompress
decompressed = huffman_decompress(compressed, codes)
print(f"Decompressed: '{decompressed}'")
print(f"Matches original? {decompressed == text}")

# Example 2: Different text
print("\n=== Another Example ===\n")

text2 = "aaaaaabbbcc"
print(f"Text: '{text2}'")

codes2, freq2 = huffman_encoding(text2)
compressed2, _, _ = huffman_compress(text2)

print("\nFrequencies:")
for char, f in sorted(freq2.items()):
    print(f"  '{char}': {f}")

print(f"\nCompressed: {compressed2} ({len(compressed2)} bits)")
print(f"Compression: {len(text2) * 8} → {len(compressed2)} bits")

# Example 3: Why greedy works
print("\n=== Why Greedy Works ===")
print("""
Huffman Greedy Principle:
1. Always merge two nodes with SMALLEST frequencies
2. Intuition: Frequent chars get shorter codes

Proof of optimality:
- If we don't merge smallest, a frequent char gets long code
- We can swap to move frequent chars closer to root
- This gives shorter codes = better compression
- Greedy choice is always optimal!
""")

print("=== Complexity ===")
print("Build tree: O(n log n) - heap operations")
print("Compress:   O(m) - m = text length")
print("Decompress: O(m)")
print("Space:      O(n) - n = unique characters")
