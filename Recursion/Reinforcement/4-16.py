'''
Write a short recursive Python function that takes a character string s and outputs its reverse. For example, the reverse of pots&pans would be snap&stop .
'''

def reverse_string(s):
    if len(s)==0:
        return ''
    return s[-1] + reverse_string(s[:-1])

#example
print(reverse_string('pots&pans')) #snap&stop

'''
time complexity: O(n)
space complexity: O(n)
'''