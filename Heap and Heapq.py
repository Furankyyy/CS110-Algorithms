#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 15:03:02 2019

@author: Furankyyy
"""
#Heappush means satisfying the heap property for one element
#Heapify means building the maximum heap
#Heappop is returning the current root and re-satisfy the heap property

def Max_Heappush(arr,i):
    left = 2*i+1 #getting the index of the left child
    right= 2*i+2 #getting the index of the right child
    #check if the left child satisfy the heap property, if not, denote the left child as largest
    if left < len(arr) and arr[left]>arr[i]:
        largest = left
    else:
        largest = i
    #check if the right child satisfy the heap property, if not, denote the right child as largest
    if right < len(arr) and arr[right]>arr[left]:
        largest = right
    #if the heap property is violated, swap the largest with the current parent
    if largest != i:
        swap = arr[i]
        arr[i] = arr[largest]
        arr[largest] = swap
        Max_Heappush(arr,largest) #continue checking for the new child

def Max_Heapify(arr):
    for i in range(len(arr)//2,-1,-1): #do for any non-leaf nodes (any node that has child(ren))
        Max_Heappush(arr,i) #heap push for max-heap structure
        
def Max_Heappop(arr):
    if arr==[]:
        return IndexError
    else:
        #I don't know if we should first build the heap
        #according to documentation, the input should be a heap
        #but here I suggest we should first build a heap with the input in case the input is not a heap
        Max_Heapify(arr)
        #record the largest term in the array
        pop=arr[0]
        #change the first element to the last element in the array
        arr[0]=arr[-1]
        #pop out the last element
        arr.pop()
        #heappush the first element so the new maximum now goes onto the top of the list
        Max_Heappush(arr,0)
        return pop