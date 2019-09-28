#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 08:51:26 2019

@author: Furankyyy
"""

###write a recursive function to determine if a node is a valid binary search tree

class Node:
    def __init__(self, val, left=None, right=None):
        self.l_child = left
        self.r_child = right
        self.data = val
        
def isValid(root):
    if not root: 
        return True
    elif root.l_child and root.r_child: #when a node has two children
        if root.data < root.l_child.data or root.data > root.r_child.data: #but the children does not satisfy bst rules
            return False
    elif (not root.l_child) and root.r_child: #when a node has only right child, check the right child
        if root.data > root.r_child.data:
            return False
    elif (not root.r_child) and root.l_child: #when a node has only left child, check the left child
        if root.data < root.l_child.data:
            return False
    return isValid(root.l_child) and isValid(root.r_child) #recursively check nodes

#test
print(isValid(Node(5, Node(3))))
print(isValid(Node(3, Node(5))))

###Write a recursive function to determine whether there are any duplicates in a binary search tree
def traversal(root,output): #recursively run through the tree in ascending order
    if not root:
        return
    traversal(root.l_child,output)
    output.append(root.data)
    traversal(root.r_child,output)
    
def inorder(root): #use the traversal() function to return the list of data
    """returns a list of all data in the tree rooted at root produced using an in order traversal"""
    inorder_traversal = []
    traversal(root,inorder_traversal)
    return inorder_traversal

def hasDuplicates(root):
    entries = inorder(root) #find the ordered list of elements in bst
    unique = set(entries) #find the unique elements
    for i in unique: #count them in the bst to find duplicates
        if entries.count(i)>1:
            return True
    return False
#test
    
print(hasDuplicates(Node(5, right=Node(6, Node(5)))))
print(hasDuplicates(Node(5, Node(3))))