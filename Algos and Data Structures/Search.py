def linear_binary_search(l, item):
    mid = -1
    while mid != 0:
        mid = len(l)//2
        
        if l[mid] == item:
            return True
        elif l[mid] > item:
            l = l[:mid]
        elif l[mid] < item:
            l = l[mid:]
    return False

def recursive_binary_search(l, item):
    mid = len(l)//2

    if l[mid] == item:
        return True
    elif mid == 0:
        return False
    elif l[mid] > item:
        return recursive_binary_search(l[:mid], item)
    elif l[mid] < item:
        return recursive_binary_search(l[mid:], item)
    



l = [1, 2, 3, 4, 5]
print(recursive_binary_search(l, 6))
print(recursive_binary_search(l, 5))
print(recursive_binary_search(l, 100))
print(recursive_binary_search(l, 3))
print(recursive_binary_search(l, 1))


