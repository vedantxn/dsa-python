'''
Describe a recursive algorithm to compute the integer part of the base-two logarithm of n using only addition and integer divisiona
'''

def log2_recursive(n):
    if n == 1:
        return 0
    return 1 + log2_recursive(n // 2) 

#example usage
n = 16
print(log2_recursive(n)) #4

#explanation
log2_recursive(16) = 1 + log2_recursive(8)
log2_recursive(8) = 1 + log2_recursive(4)
log2_recursive(4) = 1 + log2_recursive(2)
log2_recursive(2) = 1 + log2_recursive(1)
log2_recursive(1) = 0 #base case
