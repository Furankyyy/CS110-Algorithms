def find_max_subarray(A):
    if len(A)==1: #base case
        return A[0],[A[0]],A[0],[A[0]] 
        #return the four elements, basically max_subarray == max_endarray because there is only one element
    else: #in other cases
        #initializing the variables (inheriting the values from the lower level in the recursion)
        max_sub=find_max_subarray(A[0:-1])[0]
        max_subarray=find_max_subarray(A[0:-1])[1]               
        max_end=find_max_subarray(A[0:-1])[2]
        max_endarray=find_max_subarray(A[0:-1])[3]  
        #start the comparison, first add the last element (the element of interest in this level to the max_end)
        max_end += A[-1]
        #when the last element itself is larger than max_end, it means the endarray before it has a negative value, so itself now becomes the max_endarray
        if A[-1] >= max_end:
            max_end = A[-1]
            max_endarray=[A[-1]]
        else:
            max_endarray.append(A[-1])
        #when max_end > max_sub, it means that the subarray contains the last element is larger than the current maximum subarray, so we need to update the maximum subarray
        if max_end > max_sub:
            max_sub=max_end
            max_subarray=max_endarray
        #returning four variables, because we need to inherit all of them to the upper level    
        return max_sub,max_subarray,max_end,max_endarray


test1=[1,7,3,-5,-7,10,-1,0]
test2=[1,7,3,-5,-7,10,-1,6]

print("The maximum subarray of test1 is",find_max_subarray(test1)[1],"and the maximum value is",find_max_subarray(test1)[0])
print("The maximum subarray of test2 is",find_max_subarray(test2)[1],"and the maximum value is",find_max_subarray(test2)[0])

        