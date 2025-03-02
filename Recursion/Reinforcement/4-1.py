'''
Q: Describe a recursive algorithm for finding the maximum element in a sequence, S,of n elements. What is your running time and space usage?
'''

def recursive_max(S):
    # Base case: if there's only one element, it's the maximum.
    if len(S) == 1:
        return S[0]
    else:
        # Recursively find the maximum of the sub-sequence
        max_rest = recursive_max(S[1:])
        # Compare the first element with the maximum of the rest
        return S[0] if S[0] > max_rest else max_rest

# Example usage:
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("Maximum element is:", recursive_max(numbers))

# Running time: O(n)
# Space usage: O(n) due to the recursive calls