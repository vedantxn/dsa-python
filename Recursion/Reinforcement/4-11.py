'''
Describe an efficient recursive function for solving the element uniqueness problem, which runs in time that is at most O(n2) in the worst case without using sorting
'''

def is_unique_recursive(seq, index=0):
    if index >= len(seq):   #base case: no more elements to compare
        return True
    
    #check if seq[index] appears later in the sequence
    if seq[index] in seq[index+1:]:
        return False
    
    #recur for the rest of the sequence
    return is_unique_recursive(seq, index+1)


#example
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(is_unique_recursive(sequence)) #True

sequence_with_duplicates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
print(is_unique_recursive(sequence_with_duplicates)) #False
