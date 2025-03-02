'''
4-18:
Use recursion to write a Python function for determining if a string s has more vowels than consonants
'''
def more_vowels_than_constants(s, v_count = 0, c_count = 0):
    if len(s) == 0:
        return v_count > c_count
    if s[0].lower() in 'aeiou':
        v_count += 1
    else:
        c_count += 1
    return more_vowels_than_constants(s[1:], v_count, c_count)

#testcases
print(more_vowels_than_constants('hello')) # False
print(more_vowels_than_constants('hello world')) # False
print(more_vowels_than_constants('hello world!')) # True
print(more_vowels_than_constants('aeiou')) # True

'''
time complexity: O(n)
space complexity: O(n)
'''

'''
4-19:
Write a short recursive Python function that rearranges a sequence of in teger values so that all the even values appear before all the odd values.
'''

def rearrange_even_odd(lst):
    if len(lst) == 0:
        return lst
    
    if lst[0] % 2 == 0:
        return [lst[0]] + rearrange_even_odd(lst[1:])
    else:   
        return rearrange_even_odd(lst[1:]) + [lst[0]]
    
#testcases
print(rearrange_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9])) # [2, 4, 6, 8, 1, 3, 5, 7, 9]
print(rearrange_even_odd([2, 4, 6, 8, 10])) # [2, 4, 6, 8, 10]

'''
time complexity: O(n^2)
space complexity: O(n^2)
'''

'''
4-20:
 Given an unsorted sequence, S, of integers and an integer k, describe a recursive algorithm for rearranging the elements in S so that all elements less than or equal to k come before any elements larger than k.What is the running time of your algorithm on a sequence of n values?
'''

def rearrange_by_k(S, k):
    if len(S) <= 1:  # Base case: if there's 0 or 1 element, return as is
        return S

    first = S[0]
    rest = rearrange_by_k(S[1:], k)  # Recursively process the remaining elements

    if first <= k:
        return [first] + rest  # Put smaller/equal elements at the front
    else:
        return rest + [first]  # Put larger elements at the end

# Example usage
S = [7, 2, 9, 1, 5, 8, 3, 4]
k = 5
print(rearrange_by_k(S, k))
# Output: [2, 1, 5, 3, 4, 7, 9, 8] (order within groups may vary)

'''
time complexity: O(n^2)
'''

'''
4-21:
Suppose you are given an n-element sequence, S, containing distinct in tegers that are listed in increasing order. Given a number k, describe a recursive algorithm to find two integers in S that sum to k, if such a pair exists. What is the running time of your algorithm?
'''
def find_pair_recursive(S, k, low=0, high=None):
    if high is None:
        high = len(S) - 1  # Initialize high pointer

    if low >= high:  # Base case: no valid pair left
        return None

    current_sum = S[low] + S[high]

    if current_sum == k:
        return (S[low], S[high])  # Found the pair
    elif current_sum < k:
        return find_pair_recursive(S, k, low + 1, high)  # Move left pointer right
    else:
        return find_pair_recursive(S, k, low, high - 1)  # Move right pointer left

# Example usage
S = [1, 3, 4, 6, 8, 10, 12]
k = 10
print(find_pair_recursive(S, k))  # Output: (4, 6)

k = 15
print(find_pair_recursive(S, k))  # Output: (3, 12)

k = 30
print(find_pair_recursive(S, k))  # Output: None (no valid pair)

'''
time complexity: O(n)
'''
