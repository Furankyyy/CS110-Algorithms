#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 22:56:10 2019

@author: Furankyyy
"""
###original code

import timeit
import random

eps = 1e-16
N = 10000
locations = [0.0, 0.5, 1.0 - eps]


def median(x1, x2, x3):
    if (x1 < x2 < x3) or (x3 < x2 < x1):
        return x2
    elif (x1 < x3 < x2) or (x2 < x3 < x1):
        return x3
    else:
        return x1

def qsort(lst):
    indices = [(0, len(lst))]

    while indices:
        (frm, to) = indices.pop()
        if frm == to:
            continue

        # Find the partition:
        N = to - frm
        inds = [frm + int(N * n) for n in locations]
        values = [lst[ind] for ind in inds]
        partition = median(*values)

        # Split into lists:
        lower = [a for a in lst[frm:to] if a < partition]
        upper = [a for a in lst[frm:to] if a > partition]
        counts = sum([1 for a in lst[frm:to] if a == partition])

        ind1 = frm + len(lower)
        ind2 = ind1 + counts

        # Push back into correct place:
        lst[frm:ind1] = lower
        lst[ind1:ind2] = [partition] * counts
        lst[ind2:to] = upper

        # Enqueue other locations
        indices.append((frm, ind1))
        indices.append((ind2, to))
    return lst


def randomized_quicksort():
    lst = [i for i in range(N)]
    random.shuffle(lst)
    return qsort(lst)


def test_quicksort():
    lst = randomized_quicksort()
    assert (lst == [i for i in range(N)])


# Is our algorithm correct
test_quicksort()

# How fast is our algorithm
print timeit.timeit(randomized_quicksort, number=1)



###A
def new_qsort(lst):
    indices = [(0, len(lst))]

    while indices:
        (frm, to) = indices.pop()
        if frm == to:
            continue

        # Find the partition:
        N = to - frm
        inds = [frm + int(N * n) for n in locations]
        values = [lst[ind] for ind in inds]
        partition = median(*values)

        # Split into lists:
        lower = [a for a in lst[frm:to] if a <= partition]
        upper = [a for a in lst[frm:to] if a > partition]

        ind = frm + len(lower)

        # Push back into correct place:
        lst[frm:ind] = lower
        lst[ind:to] = upper

        # Enqueue other locations
        indices.append((frm, ind))
        indices.append((ind, to))
    return lst

#1.
#The new quick sort puts all elements to the lower list.
#Therefore the ind is n-1 (n-2 in python)
#So to=n-1, and frm=0
#Each time we only exclude one element from the next round of sort
#Worst case: O(n^2)

#2.
#The original quick sort in the code provided exclude the elements from the lower list
#ind1=0, ind2=len(lst)
#frm=ind1, to=ind2
#Only the first round of comparison
#Best case: O(n)


###B
def qsort(lst):
    indices = [(0, len(lst))]

    while indices:
        (frm, to) = indices.pop()
        if frm == to:
            continue

        # Find the partition:
        N = to - frm
        partition = lst[0]

        # Split into lists:
        lower = [a for a in lst[frm:to] if a < partition]
        upper = [a for a in lst[frm:to] if a > partition]
        counts = sum([1 for a in lst[frm:to] if a == partition])

        ind1 = frm + len(lower)
        ind2 = ind1 + counts

        # Push back into correct place:
        lst[frm:ind1] = lower
        lst[ind1:ind2] = [partition] * counts
        lst[ind2:to] = upper

        # Enqueue other locations
        indices.append((frm, ind1))
        indices.append((ind2, to))
    return lst

#1.
#No, it doesn't. The algorithm structure does not change.
#The only thing changed is the probability of getting the largest/smallest element of the array at first
#That is, it only makes sure that the worst case (virtually, the only exception is that all the three elements compared are extrema) do not happen.

#2.
#It will change the performance, as explained above.
#It will significantly decrease the chance of worst case.
    

###C

#first method - need random shuffle before implementing
quick_sort_oneline = lambda arr: arr if len(arr) <= 1 else quick_sort_oneline([i for i in arr[:-1] if i <= arr[-1]]) + [arr[-1]] + quick_sort_oneline([i for i in arr[:-1] if i > arr[-1]])

#second method
def quick_sort(arr, l, r):
    random.shuffle(arr)
    if l < r:
        q = partition(arr, l, r) #partitioning the array
        #recursively solve for the two sides of partition
        quick_sort(arr, l, q - 1)
        quick_sort(arr, q + 1, r)
 
def partition(arr, l, r):
    x = arr[r]
    i = l - 1 #the index of partition
    for j in range(l, r):
        if arr[j] <= x:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[r] = arr[r],arr[i+1]
    return i + 1

quick_sort(lst1,0,len(lst1)-1)
quick_sort(lst2,0,len(lst2)-1)
print(lst1,lst2)


#Assume that each partition generates two sublists that are not strikingly skewed (one very long and one very short)
#For convenience of estimation - I assume the two sublists are of equal length (the pivot is median)
#Assume no identical elements in the list
#500 recursions --> i assume that 500 is the recursions depths, not times of recursion
#n=2^500

