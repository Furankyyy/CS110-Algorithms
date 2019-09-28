#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:30:03 2019

@author: Furankyyy
"""

##
## Binary Search Tree
## 
class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.parent = None
        self.data = val

def insert(root, node):
    """inserts a node into a tree rooted at root, returns the root"""
    #same as the textbook implementation
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
    
    
def search_data(root, value): 
    #search for a particular data value
    node = search(root, value)
    if node: 
        return node.data
    else: 
        return node

def transplant(root,node,replace):
    #transplant procedure as described in textbook
    node1 = node
    node2 = replace
    if node1.parent == None:
        root = node2
    elif node1 == node1.parent.l_child:
        node1.parent.l_child = node2
    else:
        node1.parent.r_child = node2
    if node2 != None:
        node2.parent = node1.parent

def tree_minimum(node):
    while node.l_child:
        node = node.l_child
    return node

def delete(root, value):
    """if a node with data = value is present in the tree rooted at root, deletes that node and returns the root"""
    node = search(root,value)
    #search for the node
    if node:
        if node.l_child==None:
            transplant(root,node,node.r_child)
        elif node.r_child==None:
            transplant(root,node,node.l_child)
        else:
            successor = tree_minimum(node.r_child) #define the successor as the minimum node in right subtree
            if successor.parent != node:
                transplant(root,successor,successor.r_child) #transplant the successor to the root
                successor.r_child = node.r_child
                successor.r_child.parent = successor
            transplant(root,node,successor)
            successor.l_child = node.l_child
            successor.l_child.parent = successor
        return root
    else:
        return root
     
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


def to_string(root): 
    """returns a string with the relevant binary tree structure associated with the BST with the given root """
    if not root: 
        return 'Nil'
    else: 
        r = to_string(root.r_child) if root.r_child else 'Nil'
        l = to_string(root.l_child) if root.l_child else 'Nil'
        return 'Node(' + str(root.data) + ' L: ' + l + ' R: ' + r + ')'
     

###
### Simple List Code
###

def list_insert(lst, value): 
    """inserts value into lst in sorted order"""
    if len(lst)>1:
        if value <= lst[0]:
            lst=[value]+lst
            
        elif value>lst[-1]:
            lst.append(value)
        else:
            for i in range(len(lst)-1):
                if value>=lst[i] and value<=lst[i+1]:
                    lst.insert(i+1,value)
                    break
    elif len(lst)==0:
        lst.append(value)
    elif len(lst)==1:
        if value>=lst[0]:
            lst.append(value)
        else:
            lst=[value,lst[0]]
    return lst
                        
def list_delete(lst, value): 
    """ deletes first instance of value from lst if it present"""
    lst.remove(value)

 
def list_search(lst, value): 
    """ searches lst for value and returns value if present, None if it is not present"""
    for i in lst:
        if i==value:
            return value
    return None


###
### Testing Code
###

    
import random
bst = None
lst = []

for x in [Node(random.randint(0,100)) for _ in range(50)]: 
    
    if not bst: 
        bst = x
    else: 
        insert(bst, x)
    
    lst=list_insert(lst, x.data)

for x in [random.randint(0,100) for _ in range(50)]: 
    bst = delete(bst, x)
    list_delete(lst,x)
'''
for x in [random.randint(0,100) for _ in range(50)]: 
    print(x, search_data(bst, x), list_search(lst, x))
''' 

print(inorder(bst))
#print(lst)

