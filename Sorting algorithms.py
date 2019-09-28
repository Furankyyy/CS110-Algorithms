import timeit
import numpy as np
import matplotlib.pyplot as plt

def insertion_sort(inputlist):
    j=1    
    while j<len(inputlist):        
        key = inputlist[j]        
        i=j-1       
        while i>=0 and key<inputlist[i]:           
            inputlist[i+1]=inputlist[i]           
            inputlist[i]=key
            i=i-1                  
        j=j+1
    return inputlist

#insertion sort - count for step.
def insertion_sort_step(inputlist):
    step_insertion = 0
    j=1
    step_insertion += 1
    while j<len(inputlist):
        step_insertion += 1
        key = inputlist[j]
        step_insertion += 1
        i=j-1
        step_insertion += 1
        while i>=0 and key<inputlist[i]:
            step_insertion += 1
            inputlist[i+1]=inputlist[i]
            step_insertion += 1
            inputlist[i]=key
            step_insertion += 1
            i=i-1
            step_insertion += 1
        step_insertion += 1
        j=j+1
        step_insertion += 1
    step_insertion += 1
    return inputlist,step_insertion

def selection_sort(inputlist):
    for i in range(len(inputlist)-1):
        current_min=inputlist[i]
        min_index=i
        j=i+1
        while j<len(inputlist):
            if current_min > inputlist[j]:
                current_min = inputlist[j]
                min_index = j  
            j=j+1
        inputlist[min_index]=inputlist[i]
        inputlist[i]=current_min   
    return inputlist

def bubble_sort(inputlist):
    for i in range(len(inputlist)-1):
        j=0
        while j < len(inputlist)-1-i:
            larger = inputlist[j]
            if inputlist[j]>inputlist[j+1]:
                inputlist[j]=inputlist[j+1]
                inputlist[j+1]=larger
            j=j+1
    return inputlist  


#random tests
test_list1=np.random.permutation(10)
test_list2=np.random.permutation(100)
test_list3=np.random.permutation(1000)
test_worst=[10,9,8,7,6,5,4,3,2,1]
test_best=[1,2,3,4,5,6,7,8,9,10]
test_avg=[1,2,3,4,5,10,9,8,7,6]

print("insertion sort time No.1",timeit.timeit(stmt="insertion_sort(test_list1)",setup="from __main__ import insertion_sort,test_list1",number=100))
print("insertion sort time No.2",timeit.timeit(stmt="insertion_sort(test_list2)",setup="from __main__ import insertion_sort,test_list2",number=100))
print("insertion sort time No.3",timeit.timeit(stmt="insertion_sort(test_list3)",setup="from __main__ import insertion_sort,test_list3",number=100))

print("selection sort time No.1",timeit.timeit(stmt="selection_sort(test_list1)",setup="from __main__ import selection_sort,test_list1",number=1000))
print("selection sort time No.2",timeit.timeit(stmt="selection_sort(test_list2)",setup="from __main__ import selection_sort,test_list2",number=1000))
print("selection sort time No.3",timeit.timeit(stmt="selection_sort(test_list3)",setup="from __main__ import selection_sort,test_list3",number=1000))

print("bubble sort time No.1",timeit.timeit(stmt="bubble_sort(test_list1)",setup="from __main__ import bubble_sort,test_list1",number=1000))
print("bubble sort time No.2",timeit.timeit(stmt="bubble_sort(test_list2)",setup="from __main__ import bubble_sort,test_list2",number=1000))
print("bubble sort time No.3",timeit.timeit(stmt="bubble_sort(test_list3)",setup="from __main__ import bubble_sort,test_list3",number=1000))

time_insertion=[0.003,0.0396,1.1902]
time_selection=[0.122,9.390,897.381]
time_bubble=[0.179,17.784,1987.832]
n=[10,100,1000]

time_insertion=np.array([time_insertion,n])
time_selection=np.array([time_selection,n])
time_bubble=np.array([time_bubble,n])

plt.figure()
plt.scatter(y=time_insertion[0],x=time_insertion[1])
plt.scatter(y=time_selection[0],x=time_selection[1])
plt.scatter(y=time_bubble[0],x=time_bubble[1])

#Running time figure for insertion sort
data_insertion=np.empty((1,2))
for i in range(10,200,10):   
    testlist=np.random.permutation(i)
    time=timeit.timeit(stmt="insertion_sort(testlist)",setup="from __main__ import insertion_sort,testlist",number=10)
    time=time/10
    stack=np.array((time,i))
    data_insertion=np.vstack((data_insertion,stack))

data_insertion=data_insertion[1:len(data_insertion)]

plt.figure()
plt.ylim(0,0.0004)
plt.scatter(x=data_insertion[:,1],y=data_insertion[:,0])
plt.xlabel('Input size')
plt.ylabel('Running time')
    
#Running time figure for bubble sort
data_bubble=np.empty((1,2))
for i in range(10,200,10):   
    testlist=np.random.permutation(i)
    time=timeit.timeit(stmt="bubble_sort(testlist)",setup="from __main__ import bubble_sort,testlist",number=10)
    time=time/10
    stack=np.array((time,i))
    data_bubble=np.vstack((data_bubble,stack))

data_bubble=data_bubble[1:len(data_bubble)]

plt.figure()
plt.ylim(0,0.008)
plt.scatter(x=data_bubble[:,1],y=data_bubble[:,0])
plt.xlabel('Input size')
plt.ylabel('Running time')