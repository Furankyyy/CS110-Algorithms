#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:55:12 2019

@author: Furankyyy
"""
import numpy as np
import matplotlib.pyplot as plt
import timeit

###worst sort function###

#define the function that checks whether the list is in ascending order
def right_permutation(arr):
    if len(arr)==1: #if there's only one element, then the order is always correct
        return True
    for i in range(len(arr)-1): #check every elements from the first to the second to the last
        if arr[i+1]<arr[i]: #if the i+1th element is smaller than ith, the order is wrong, break the loop and return false
            break
        else:
            if i == len(arr)-2: #if the i+1th element is greater than/equal to ith, check if we have already checked all the elements
                return True #if we've already checked all the elements (i.e. i==len(arr)-2), return true; if not, continue the loop
    return False
            
        
#define the worst sort function
def worstsort(arr):
    sort_arr=[] #initialize output
    check = False #initialize the result of right_permutation()
    while check == False: #while the order is wrong, generate a new permyutation and check if its order is correct
        sort_arr = np.random.permutation(arr)
        check = right_permutation(sort_arr)
    return sort_arr

#test cases
test1=[5,4,3,2,1]
test2=[1,2,3,4,5] #best case
test3=[2,2,2,2,2] #best case as well!
test4=[2] #only one element
print(worstsort(test1))
print(worstsort(test2))
print(worstsort(test3))
print(worstsort(test4))


#the best case is when the input list is already sorted, in this case, we only need to run the right_permutation once
#we have a for loop in right_permutation, so the best case complexity is O(n)


#given a random input of size n, the chance that the input x_k is correctly sorted is Pr(x_k) = 1/P_n = 1/n! 
#since in this worst algorithm, we do not "remember" the permutations that we've already checked
#so each time, the Pr(sorted) remains the same 1/n!
#Then we would expect to have n! times to have the corrected sorted list 
#the reason is that we have E[Pr(x1)+Pr(x2)+...+Pr(x_k)]=1, since Pr(x_k)=1/n!, we would expect k = n!
#this reasoning is the same as the random indicator variable in the book, where we have the pr(I) for each choice (permutation) and we sum them to find the expected value
#so the averaage case complexity is O(n!)


#to calculate what n is best for this function

def factorial(n):
    result=1
    for i in range(n):
        result=result*(i+1)
    return result

x=np.arange(0,7,1)
y_factorial=list(map(factorial,x))
y_compare=x*x

plt.plot(x,y_factorial,label="Factorial of n")
plt.plot(x,y_compare,label="n square")
plt.title("Complexity comparison")
plt.legend()

#from the plot we can see that for algorithms with comlexity of O(n^2) and O(n!), the difference comes when n=5
#when n=4, the two algorithms do not vary that much, but when n=5, they have a >100 times difference
#therefore, this method is feasible when n<=4
#p.s. constants are discounted (they are relatively unimportant)




###median finder###

#the worst case for the median finder is that the elements in the input list are unique
#the best case is that all elements are the same --> no matter which we choose, it is the median

#to consider the times we try before stopping, we need to consider the worst case --> all elements are different
#then the chance to find the exact median is 1/n
#the number of elements lying in the input deviation range x is x//(100/n)+1 for this worst case
#explanation: divide the 100% to n parts, if all elements are different then each element takes the 1 part, the x//(range for 1 part)+1 is the num of elements lying in the range
#therefore, the probability of choosing the element in the range given by x is  (x//(100/n)+1)/n
#I want to try the expected times of choosing the correct element(s) for the worst case

#Pr(failure) for 1 try is 1-(x//(100/n)+1)/n
#Pr(failure) for the first k try is (1-(x//(100/n)+1)/n)^k, which scales with x and n.

#so the Pr(at least one success) for the first k try is 1-Pr(failure)=1-(1-(x//(100/n)+1)/n)^k
#we want to find a k taht makes this Pr large enough
#so we want to find a small k minimizing Pr(failure) for the first k try
#to simplify the problem, we regard x as constant and assume the "//" is "/"
#(1-(x//(100/n)+1)/n)^k = ((n-xn/100-1)/n)^k =(1-x/100-1/n)^k
#x/100 is a constant
#-->(1-1/n)^k
#when n is sufficiently large, (1-1/n) is nearly 1
#it is extremely hard to succeed if n is very large, I set the limit of k at 10000, simply because my laptop's computational ability

def median_finder(arr,x):
    tried = 0 #record the number of times of choosing the random element
    if abs(x) <= 0.5: #when x is valid
        lower=np.percentile(arr,50-x/2)
        upper=np.percentile(arr,50+x/2)
        while tried <10000:
            find = np.random.randint(0,len(arr)) #find a new element
            if lower<=arr[find] and arr[find]<=upper: #if the chosen element is in the range, return it
                return arr[find]
            else: 
                tried += 1 
        return "Tried enough times, still cannot find the value"
    else:
        return "x not in the domain"

#test cases
test1=list(np.random.permutation(200))
test2=[4]*100
test3=[5]*1000
test4=test2+test3

print(median_finder(test1,0.5)) #worst case, exactly 2 elements in the range
print(median_finder(test2,0.5)) #best case
print(median_finder(test2,0))  #best case
print(median_finder(test3,0.5)) #best case
print(median_finder(test4,0)) #1000/1100 probability 
print(median_finder(test4,0.5)) #same as above.


#time complexity

#best case running time is O(1)

#the time complexity of the worst case running time is E[k]=Sum(E[ki])
#E[ki]=Pr(correct)=(x//(100/n)+1)/n
#sum is from 1 to the limit tried k
#since x is between 0 and 0.5, we simply regard it as constant
#we also assume the "//" is "/"
#then the expression becomes: E[k]= k*(xn/100+1)/n
#as n goes to infinity, we can solve this by trying to use L'Hopital's rule
#the result is kx/100, which is a constant
#O(1)


data=np.empty((1,2))

for i in range(200,1200,50):   
    testlist=list(np.random.permutation(i))
    time=timeit.timeit(stmt="median_finder(testlist,0.5)",setup="from __main__ import median_finder,testlist",number=100)
    time=time/100
    stack=np.array((time,i))

    data=np.vstack((data,stack))

data=data[1:]

plt.figure()
plt.ylim(0,0.01)
plt.scatter(x=data[:,1],y=data[:,0])
plt.xlabel("Inputsize")
plt.ylabel("Running time")
plt.title("Median finder running time")

#from the plot we can see that the running time is almost constant --> O(1)


#space complexity is O(n), because each time we just store the (sorted) list of length n