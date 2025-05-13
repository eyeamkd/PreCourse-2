# Python program for implementation of MergeSort 
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    return merge(left, right)

# Test the implementation
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
sorted_arr = mergeSort(arr)
print("Sorted array:", sorted_arr)

#write your code here
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
  
# driver code to test the above code 
    if __name__ == '__main__': 
        arr = [12, 11, 13, 5, 6, 7]  
        print ("Given array is", end="\n")  
        printList(arr) 
        sorted_arr = mergeSort(arr)
        print("Sorted array is: ", end="\n") 
        printList(sorted_arr) 
