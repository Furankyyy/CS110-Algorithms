#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:52:03 2019

@author: Furankyyy
"""

###Direct Address Table

#1.initialize N empty guesses
def create_dir_addr_table(n):
    table = [None for i in range(n)] #initialize an empty table with length n
    return table

#2.set a guess for the i-th entry    
def set_guess(table,i,guess):
    table[i-1] = guess #since i represents the i-th entry, we need to use i-1 for actual Python indexing

#3.clear an incorrect guess for the i-th entry
def remove_guess(table,i):
    table[i-1] = None #remove the i-th entry = set the entry to None
    

###social security

'''
It is a bad idea to store the id number in a single set. The dataset is too large, often several millions. The universe
is also expanding/contracting depending on birth rate and death rate of the country, so we cannot possibly know the size of
the entire universe (possible keys)
'''


###chained hash table

import random
import string
import timeit


def randomword(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def empty_hash_table(N):
    return [[] for n in range(N)]


def add_to_hash_table(hash_table, item, hash_function):
    N = len(hash_table)
    # Your code here
    slot = hash_function(item)
    if slot < N: #if there is a existing slot for the item
        hash_table[slot].append(item)
    else: #if the slot computed by the hash function exceeds the total number of slot, Index error
        return IndexError
    return hash_table


def contains(hash_table, item, hash_function):
    N = len(hash_table)
    # Your code here
    slot = hash_function(item)
    if slot < N:
        if item in hash_table[slot]:
            return True #return true if the item has already been stored in the hash_table
        else:
            return False #return false otherwise
    else: 
        return False #item out of index range is also a case of the table not containing the item



def remove(hash_table, item, hash_function):
    if not contains(hash_table, item, hash_function):
        raise ValueError()
    # Your code here
    slot = hash_function(item)
    hash_table[slot].remove(item)
    
    return hash_table


def hash_str1(string):
    ans = 0
    for chr in string:
        ans += ord(chr)
    return ans


def hash_str2(string):
    ans = 0
    for chr in string:
        ans = ans ^ ord(chr)
    return ans


def hash_str3(string):
    ans = 0
    for chr in string:
        ans = ans * 128 + ord(chr)
    return ans


def hash_str4(string):
    random.seed(ord(string[0]))
    return random.getrandbits(32)

#1.Create 100,000 words of 10 characters each.
data=[]
for i in range(100000):
    data.append(randomword(10))
    
#2.Create four chained hash-tables with 5000 slots.
h1=empty_hash_table(5000)
h2=empty_hash_table(5000)
h3=empty_hash_table(5000)
h4=empty_hash_table(5000)

#3.Store all the words in each chained hash table using each of the different hash functions.
for i in data:
    add_to_hash_table(h1, i, hash_str1)
    
for i in data:
    add_to_hash_table(h2, i, hash_str2)
    
for i in data:
    add_to_hash_table(h3, i, hash_str3)
    
for i in data:
    add_to_hash_table(h4, i, hash_str4)
    
#4.Measure the number of collisions for each hash function.
def collision_count(hash_table): 
    #I assume the number of collisions means the total number of elements taking up the same slot,
    #instead of the total number of slots that have collisions
    #so the maximum number of collisions would be 99999 (all elements in the same slot)
    have_data = 0
    for j in hash_table:
        if len(j)>0:
            have_data += 1
    return 100000-have_data
    
print(collision_count(h1))
print(collision_count(h2))
print(collision_count(h3))
print(collision_count(h4))

#5.For each of the hash functions, how many elements are in a bucket on average (if it is not empty)?
def avg_ele(hash_table):
    have_data = [j for j in hash_table if len(j)>0] #find the slots that have data
    total = 0
    for i in have_data:
        total += len(i) #find the total number of elements in each slot that has data
    return total/len(have_data)            

#6.Time how long it takes to find elements that are in each hash table.
word_choice = data[random.randrange(100000)] #randomly choose a word in the generated data
time_h1=timeit.timeit(stmt="contains(h1, word_choice, hash_str1)",setup="from __main__ import contains,h1,word_choice,hash_str1",number=1000)
time_h2=timeit.timeit(stmt="contains(h2, word_choice, hash_str2)",setup="from __main__ import contains,h2,word_choice,hash_str2",number=1000)
time_h3=timeit.timeit(stmt="contains(h3, word_choice, hash_str3)",setup="from __main__ import contains,h3,word_choice,hash_str3",number=1000)    
time_h4=timeit.timeit(stmt="contains(h4, word_choice, hash_str4)",setup="from __main__ import contains,h4,word_choice,hash_str4",number=1000)
#we can generate more test cases (word choices) using for loop
   
#7.For each hash table, time how long it takes to find 10,000 elements that have not been stored.
def find_not_stored10000(hash_table,hash_function): 
    found = 0
    not_in_table = []
    while found<10000: #continue to find until we found 10000 elements
        item = randomword(10) #generate a new element
        if not contains(hash_table, item, hash_function): #look for it in the table, if find it, append it to the list
            found +=1
            not_in_table.append(item)
    return not_in_table

time_find_h1=timeit.timeit(stmt="find_not_stored10000(h1,hash_str1)",setup="from __main__ import find_not_stored10000,h1,hash_str1",number=1)
time_find_h2=timeit.timeit(stmt="find_not_stored10000(h2,hash_str2)",setup="from __main__ import find_not_stored10000,h2,hash_str2",number=1)
time_find_h3=timeit.timeit(stmt="find_not_stored10000(h3,hash_str3)",setup="from __main__ import find_not_stored10000,h3,hash_str3",number=1)
time_find_h4=timeit.timeit(stmt="find_not_stored10000(h4,hash_str4)",setup="from __main__ import find_not_stored10000,h4,hash_str4",number=1)
            
    