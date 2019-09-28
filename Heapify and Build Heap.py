def Max_Heapify(arr,i):
    left = 2*i+1 #getting the index of the left child
    right= 2*i+2 #getting the index of the right child
    #check if the left child satisfy the heap property, if not, denote the left child as largest
    if left < len(arr) and arr[left]>arr[i]:
        largest = left
    else:
        largest = i
    #check if the right child satisfy the heap property, if not, denote the right child as largest
    if right < len(arr) and arr[right]>arr[left]:
        largest = right
    #if the heap property is violated, swap the largest with the current parent
    if largest != i:
        swap = arr[i]
        arr[i] = arr[largest]
        arr[largest] = swap
        Max_Heapify(arr,largest) #continue checking for the new child

def Build_Max_Heap(arr):
    for i in range((len(arr)//2,0,-1): #do for any non-leaf nodes (any node that has child(ren))
        Max_Heapify(arr,i) #heapify for max-heap structure