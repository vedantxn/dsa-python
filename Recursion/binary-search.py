def binary_search(data, taget, low, high):
    #return ture if target is found in indicated portion of a Python list
    # The search only considers the portion from data[low] to data[high] inclusive.

    if low > high:
        return False # interval is empty; no match
    else:
        mid = (low + high) // 2
        if taget == data[mid]: # found a match
            return True
        elif taget < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, taget, low, mid - 1)
        else:
            return binary_search(data, taget, mid + 1, high) # recur on the portion right of the middle
        