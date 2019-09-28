#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:31:37 2019

@author: Furankyyy
"""

###Average number of comparisons when searching

import random

#bst
class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.parent = None
        self.data = val

def insert(root, node):
    """inserts a node into a tree rooted at root, returns the root"""
    parent = None
    while root:
        parent = root
        if node.data<root.data:
            root = root.l_child
        else:
            root = root.r_child
    node.parent = parent
    if parent == None:
        root = node
    elif node.data<parent.data:
        parent.l_child = node
    else:
        parent.r_child = node


def search(root, value):
    """searches a tree rooted at root for a node with data = value, returns the node if found, None otherwise"""
    #same as the textbook implementation
    #if value is smaller than current root value, search left subtree
    #otherwise search right subtree
    while root!=None and value!=root.data:
        if value<root.data:
            root=root.l_child
        else:
            root=root.r_child
    return root

def traversal(root,output):
    if not root:
        return
    traversal(root.l_child,output)
    output.append(root.data)
    traversal(root.r_child,output)
    
def inorder(root): 
    """returns a list of all data in the tree rooted at root produced using an in order traversal"""
    inorder_traversal = []
    traversal(root,inorder_traversal)
    return inorder_traversal

#count the number of comparisons while searching, modified based on search()
def search_count(root,value):
    count=0
    while root!=None and value!=root.data:
        count+=1
        if value<root.data:
            root=root.l_child
        else:
            root=root.r_child
    count+=1       
    return count

#average comparisons
def avg_cmp(bst):
    #record all the values in the bst
    data=inorder(bst)
    #initialize the sum of counts
    count=0
    #count all the comparisons
    for i in data:
        count+=search_count(bst,i)
    #return the average comparison
    return count/len(data)

#test code
bst = None
for x in [Node(random.randint(0,100)) for _ in range(50)]:  
    if not bst: 
        bst = x
    else: 
        insert(bst, x)
        
print(avg_cmp(bst))


###Height of randomly-built trees
import matplotlib.pyplot as plt

#1.maximum height of a bst

#recursively find the maximum height of a tree
def max_height(bst):
    #if none return 0
    if not bst:
        return 0
    else:
        #check the left and right subtree
        #choose the deeper subtree + 1 as the maximum height of the current subtree
        height_left = max_height(bst.l_child)
        height_right = max_height(bst.r_child)
        if height_left > height_right:
            return height_left+1
        else:
            return height_right+1
    
#2.average height
def avg_height(bst):
    return avg_cmp(bst)-1

#3.insert randomly shuffled list and calculate height
bst2 = None
avg_h=[]
max_h=[]
n=[x for x in range(1,10000,100)]

for x in [Node(random.randint(0,10000)) for _ in range(1,10000,100)]:  
    if not bst2: 
        bst2 = x   
    else: 
        insert(bst2, x)
    avg_h.append(avg_height(bst2))
    max_h.append(max_height(bst2))
        

plt.plot(n,max_h,label='Maximum height')
plt.plot(n,avg_h,label='Average height')
plt.legend(loc='upper left')
plt.xlabel('Tree size')
plt.ylabel('Height')
plt.title('Height change with respect to tree size')

#As we can see, the average and maximum height all increase with respect to the size of the tree.
#The average depth follows a logrithmic growth just as the average height of tree is O(lgN)

