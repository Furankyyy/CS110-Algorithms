import timeit
import numpy as np
import matplotlib.pyplot as plt

def mergesort(inputlist):
    if len(inputlist)>1:
        mid=len(inputlist)//2
        leftside=inputlist[:mid]
        rightside=inputlist[mid:]
    
        leftside=mergesort(leftside)
        rightside=mergesort(rightside)
    
        leftside.append(float('inf'))
        rightside.append(float('inf'))
    
        outputlist=[]
        i=0
        j=0
    
        while i<len(leftside) and j<len(rightside):
            if leftside[i]<=rightside[j]:
                outputlist.append(leftside[i])
                i=i+1
            else:
                outputlist.append(rightside[j])
                j=j+1
            
        outputlist.pop()
    
        return(outputlist)
    else:  
        return(inputlist)

Numbers = [41, 33, 17, 80, 61, 5, 55]

print(mergesort(Numbers))


data_merge=np.empty((1,2))
for i in range(10,200,10):   
    testlist=list(np.random.permutation(i))
    time=timeit.timeit(stmt="mergesort(testlist)",setup="from __main__ import mergesort,testlist",number=10)
    time=time/10
    stack=np.array((time,i))
    data_merge=np.vstack((data_merge,stack))

data_merge=data_merge[1:len(data_merge)]

plt.figure()
plt.ylim(0,0.002)
plt.scatter(x=data_merge[:,1],y=data_merge[:,0])
plt.xlabel('Input size')
plt.ylabel('Running time')