#if a recursive call starst at most one other, it is called a linear recursion

#binary search is a linear recursion 

def linear_sum(S, n):
    #return the sum of the first n numbers of sequence S
    if n==0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]
    
def reverse(S, start, stop):
    #reverse elements in implicit slice S[start:stop]
    if start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)
    
def power(x, n):
    #compute the value x**n for integer n
    if n==0:
        return 1
    else:
        return x*power(x, n-1)
    
def power_two(x, n):
    #compute the value x**n for integer n
    if n==0:
        return 1
    else:
        partial = power_two(x, n//2)
        result = partial*partial
        if n%2 == 1:
            result *= x
        return result