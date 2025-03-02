'''
tower of hanoi problem
'''

def towers_of_hanoi(n, source, auxiliary, destination):
    if n==1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    
    #move n-1 disks from source to auxiliary
    towers_of_hanoi(n-1, source, destination, auxiliary)    

    #move nth disk from source to destination
    print("Move disk", n, "from source", source, "to destination", destination)

    #move n-1 disks from auxiliary to destination   
    towers_of_hanoi(n-1, auxiliary, source, destination)


#example
n = 4
towers_of_hanoi(n, 'A', 'B', 'C')

'''
time complexity: O(2^n)
space complexity: O(n)
'''