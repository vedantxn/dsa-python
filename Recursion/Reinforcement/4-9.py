def find_min_max(seq, index=0, min_val=None, max_val=None):
    if index == len(seq):   # Base case: reached the end of the sequence
        return min_val, max_val
    
    current = seq[index]
    if min_val is None or current < min_val:
        min_val = current  
    if max_val is None or current > max_val:
        max_val = current
    
    return find_min_max(seq, index + 1, min_val, max_val)

#example usage:
sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_val, max_val = find_min_max(sequence)
print(f"Min: {min_val}, Max: {max_val}")