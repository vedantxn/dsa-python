#example
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def binary_search_iterative(data, target):
    #return true if target is found in the given python list.
    low = 0
    high = len(data) -1
    while low <= high:
        mid = (low + high) //2
        if target == data[mid]:     #found a match
            return True
        elif target < data[mid]:    #only consider values left of mid
            high = mid -1
        else:
            low = mid + 1           #only consider values right of mid
    return False                    #loop ended without success

def reverse_iterative(S):
    #reverse elements in sequence S
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]  #swap first and last
        start, stop = start + 1, stop - 1          #narrow the range