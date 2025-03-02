'''
Write a recursive function that will output all the subsets of a set of nelements (without repeating any subsets).
'''

def generate_subsets(s, current_subset=[], index=0):
    if index == len(s):
        print(current_subset)
        return
    
    #exclude the current element and move to the next element
    generate_subsets(s, current_subset, index+1)

    #include the current element and move to the next element
    generate_subsets(s, current_subset + [s[index]], index+1)

#example    
generate_subsets([1, 2, 3])
'''
[]
[3]
[2]
[2, 3]
[1]
[1, 3]
[1, 2]
[1, 2, 3]
'''

'''
time complexity: O(2^n)
space complexity: O(n)
'''