'''
Write a short recursive Python function that determines if a string s is a palindrome, that is, it is equal to its reverse. For example, 'racecar' and 'gohangasalamiimalasagnahog' are palindromes.
'''

def is_palindrome(s):
    if len(s) <= 1:     # Base case: if the string is empty or has only one character, it is a palindrome
        return True
    if s[0] != s[-1]:   # If the first and last characters are not the same, it is not a palindrome
        return False
    return is_palindrome(s[1:-1])   # Recur with the string without the first and last characters


#example
print(is_palindrome('racecar')) # True
print(is_palindrome('gohangasalamiimalasagnahog')) # True
print(is_palindrome('hello')) # False

'''
time complexity: O(n)
space complexity: O(n)
'''