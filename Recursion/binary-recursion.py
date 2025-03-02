def binary_sum(S, start, stop):
    #return the sum of the numbers in implicit slice S[start:stop]
    if start >= stop:       #zero elements in slice
        return 0
    elif start == stop - 1:     #one element in slice
        return S[start]
    else:                   #two or more elements in slice
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)
    

'''MULTIPLE RECURSION! (pseudocode)'''

'''
Algorithm PuzzleSolve(k,S,U):
Input: An integer k, sequence S, and set U
Output: An enumeration of all k-length extensions to S using elements in U
without repetitions
for each e in U do
Add e to the end of S
Remove e from U
if k ==1 then
Test whether S is a configuration that solves the puzzle
if S solves the puzzle then
return “Solution found: ” S
else
PuzzleSolve(k−1,S,U)
Remove e from the end of S
Add e back to U
'''