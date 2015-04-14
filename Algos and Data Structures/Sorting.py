from itertools import product

def bubble_sort(l):
    for i, j in product(range(len(l)), range(len(l))):
        if l[j] > l[i]:
            l[i], l[j] = l[j], l[i]
    return l

def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i+=1
            else:
                l[k] = right[j]
                j+=1
            k+=1
        while i<len(left):
            l[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            l[k] = right[j]
            j+=1
            k+=1


def quick_sort(l):
    quick_sort_helper(l, 0,len(l)-1)

def quick_sort_helper(l, start, end):
    if start < end:
        splitpoint = partition(l, start, end)

        quick_sort_helper(l, start, splitpoint-1)
        quick_sort_helper(l, splitpoint+1, end)

def partition(l, first, last):
    pivot = l[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and l[leftmark] <= pivot:
            leftmark = leftmark+1
        while l[rightmark] >= pivot and rightmark >= leftmark:
            rightmark = rightmark-1
            
        if rightmark < leftmark:
            done = True
        else:
            l[leftmark], l[rightmark] = l[rightmark], l[leftmark]
            
    l[first], l[rightmark] = l[rightmark], l[first]

    return rightmark


alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist)
print(alist)
        

            
        
