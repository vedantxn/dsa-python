def count_trailing_ones(n):
    """Returns the number of consecutive 1s at the end of the binary representation of n."""
    count = 0
    while n & 1:  # Check if the last bit is 1
        count += 1
        n >>= 1  # Shift right to check next bit
    return count

def draw_interval(c):
    """Non-recursive function to draw the tick lines for an English ruler."""
    total_ticks = (2 ** c) - 1  # The total number of tick lines

    for i in range(total_ticks):
        num_dashes = count_trailing_ones(i) + 1  # Rule for computing dashes
        print("-" * num_dashes)  # Print the tick mark

# Example usage
draw_interval(4)

'''
time complexity: O(2^c)
space complexity: O(1)
'''