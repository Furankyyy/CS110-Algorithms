#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 04:26:11 2019

@author: Furankyyy
"""
import numpy as np
import matplotlib.pyplot as plt

###Hiring-Assistant

def hiring_assistant(num_days):
    best=0 #initialize the current best assistant
    hired=0 #initialize the number of hirings
    for i in range(num_days): #simulate for every day
        applicant = np.random.random() #sample the new applicant from the uniform random distribution
        if applicant > best: #if the applicant is better than current assistant, change
            best = applicant
            hired += 1
    return hired,best

#test cases, sampling 100 and 1000 times
print(hiring_assistant(100))
print(hiring_assistant(1000))


#suppose we have num_days = k (i.e. we sample k applicants from the uniform distribution)
#then the probability of one applicant being the best is 1/k
#so the probability of we hiring exact one applicant = Pr(the first applicant is the best) = 1/k



from statistics import mean

def hiring_count(n):
    data=[]
    for j in range(10,n,10):
        hire=[]
        for i in range(20):
            hire.append(hiring_assistant(j)[0])
        avg_hire = mean(hire)
        data.append([j,avg_hire])
    return data

data=np.array(hiring_count(500))

theo_data=[]
for j in range(10,500,10):
    theo_hire=0
    for i in range(j):
        theo_hire += 1/(i+1)
    theo_data.append([j,theo_hire])

theo_data=np.array(theo_data)

plt.figure()
plt.scatter(x=data[:,0],y=data[:,1],c="blue",label="Empirical data")
plt.scatter(x=theo_data[:,0],y=theo_data[:,1],c="red",label="Theoretical data")
plt.legend(loc="upper left")
plt.xlabel("Total number of applicants")
plt.ylabel("Average hired applicants")
plt.title('Average number of hiring based on total number of applicants')



###Hat-check

def hat_check(n): #hat-check for n person
    match=0 #initialize number of matches
    customer_order=np.random.permutation(n) #the correct order of hats (each hat is represented by an integer)
    attendant_order=np.random.permutation(n) #the giving-away order of hats
    for i in range(n): #check the order
        if customer_order[i] == attendant_order[i]: #match if the corresponding number(hat) in the two array are the same
            match+=1
    return match

#test cases
print(hat_check(100))
print(hat_check(1000))  


#each customer has 1/n chance of getting the correct hat
#Xi =I{getting the correct hat}
#the average number of correct hat is E[x]=E[X1]+E[X2]+...+E[Xn]=n*1/n=1
        

    