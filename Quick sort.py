#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 20:36:06 2019

@author: Furankyyy
"""


import random
random.seed(123)
lst1 = [random.random() for a in range(100000)]
lst2 = [a for a in range(100000)]

#quick sort - textbook implementation
def quick_sort(arr, l, r):
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


#this is a simple code for quick sort
quick_sort2 = lambda arr: arr if len(arr) <= 1 else quick_sort2([i for i in arr[:-1] if i <= arr[-1]]) + [arr[-1]] + quick_sort2([i for i in arr[:-1] if i > arr[-1]])


#Fibonacci Programming

def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

import timeit

time=timeit.timeit(stmt="fib(100)",setup="from __main__ import fib",number=30)

print("Average time for running fib(100) is", time/30)

#the time for Fibonacci is T(n)=T(n-1)+T(n-2)+O(1)
#consider a binary tree with fib(n) on the root, and fib(n-2),fib(n-1) as its leaves
#when we draw the tree down to the bottom, we have n levels
#so we have at least 2^(n-1) leaves
#each leave is O(1)
#therefore the complexity is O(2^n)

#worst-case running time for quicksort is O(n^2)
#much better than fib
#would rather do fib

