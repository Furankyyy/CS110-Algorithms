#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:12:37 2019

@author: Furankyyy
"""

import heapq

###Median Heap


#The idea behind the algorithm is that we create two heaps to divide the elements of the list, one max heap and one 
#min. The roots of the two heaps will always be the middle two elements in the list.
#Each time, we compare the added element to the root of maxheap. When it's larger than or equal to the max root, we
#put it in the min heap. Otherwise we put it in the maxheap. Whenever the min heap has more than 1 element than
#the max heap, we move the root of the min heap to the max heap. Whenever the max heap has more elements than min heap
#we move its root to the min heap. In this way, we maintain two properties: 1) the list is almost evenly divided by 
#the two heaps, the difference in their lengths is no greater than 1; 2) the root of the min heap is always smaller
#than (almost) half of the list and that of the max heap is always larger than (almost) half of the list. If the list 
#has an odd number of elements, the median will always be the root of min heap. If it has an even number of elements 
#(the two heap lengths are equal), the median will be the average of the two roots.


#since heapq only has functions for min heap, we need to first write algorithms for max heap.
def heappush_max(heap,item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1) #use the heapq sifting function to push the item to the heap        


def median_checker(minh,maxh): #check if the two lists are (almost) evenly divided
    #whenever the max heap has more elements than min heap, we move its root to the min heap
    if len(maxh)-len(minh)>0: 
        pop=heapq._heappop_max(maxh)
        heapq.heappush(minh,pop)
    #Whenever the min heap has more than 1 element than the max heap, we move the root of the min heap to the max heap
    if len(minh)-len(maxh)>1:
        pop=heapq.heappop(minh)
        heappush_max(maxh,pop)
        

def add_to_median_heap(minh, maxh, elem):
    #the very first element of the list goes to the maxheap
    if len(maxh)==0 and len(minh)==0:
        maxh.append(elem)   
    else:
        #compare the added element with the root of the max heap to decide where it goes
        if elem >= maxh[0]:
            heapq.heappush(minh,elem)
        else:
            heappush_max(maxh,elem)
        
        #check for the median property
        median_checker(minh,maxh)
    
    
def median(minh,maxh):
    #if list has even number of elements, find the average of the two roots
    if len(minh)==len(maxh):
        return (minh[0]+maxh[0])/2
    #if list has only one element, its in the max heap, so return the root of max heap
    elif len(minh)+len(maxh)==1:
        return maxh[0]
    #if it has odd number of elements (except for 1), return the min root
    else:
        return minh[0]

#test code
minh = []
maxh = []
for a in range(1,2,2):
    add_to_median_heap(minh, maxh, a)
print(median(minh, maxh))


#We know that pushing the additional element to the heap and maintaining the heap structure takes O(lgn) time. The 
#comparison takes O(1) time. The median checker procedure, in worst case (which means we need to move the element from)
#one heap to the other) also takes O(lgn) time. Therefore the total worst case complexity is O(lgn)+O(1)+O(lgn)=O(lgn)

#The worst case complexity for median() is just O(1)


###Quickselect
import random


def selectsort(lst): #modified quick sort
    #select the median of the first, mid, and last element of the list as pivot
    locations = [0.0, 0.5, 1.0 - 1e-16]
    N = len(lst)
    inds = [lst[int(N * n)] for n in locations]
    values = [ind for ind in inds]
    if (values[0]<values[1]<values[2]) or (values[2]<values[1]<values[0]):
        partition = values[1]
    elif (values[0]<values[2]<values[1]) or (values[1]<values[2]<values[0]):
        partition = values[2]
    else:
        partition = values[0]
    
    #divide the list into three parts
    lower = [a for a in lst if a < partition]
    upper = [a for a in lst if a > partition]
    mid = [a for a in lst if a == partition]
    
    return (lower,mid,upper)
    
    
#k here indicates the k-th element with 1-based index
def qselect(lst,k):
    #divide the list
    sort = selectsort(lst)
    left = sort[0]
    mid = sort[1]
    right = sort[2]
    #if and only if the lower part has k-1 elements, the pivot is the k-th smallest element
    #if the lower part has more than k-1 elements, we recursively select the lower part only
    #if the lower part has less than k-1 elements, we recursively select the upper part with k-len(left)
    if len(left)>k-1:
        return qselect(left,k)
    #if the lower part has no elements - this only occurs when there are only 2 elements in the list (so that one
    #goes to mid and the other goes to upper), we simply choose the elements based on the value of k (because k
    #can only be either 1 or 2)
    if len(left)==0:
        if k==2:
            return right[-1]
        if k==1:
            return mid[0]
    if len(left)<k-1:
        return qselect(mid+right,k-len(left))
    else:
        return mid[0]

     
random.seed(123)
lst = [a for a in range(1000)]
random.shuffle(lst)
for a in range(1,1001): #because the k is 1-based, I need to change the value of a here
    print(qselect(lst, a))   


  

    

    

