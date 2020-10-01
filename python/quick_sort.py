"""
Quick Sort
-  It picks an element as pivot and partitions the given array around the picked pivot.
   It's a Divide and Conquer algorithm
"""

# This function takes last element as pivot
def partition(arr, low, high):

    # index of smaller element
    i = (low - 1)

    pivot = arr[high] 
  
    for j in range(low, high): 
  
        # If current element is smaller than the pivot 
        if arr[j] < pivot:

            # increment index of smaller element 
            i = i + 1 
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    return (i + 1)
  
# Function to do Quick sort 
def quickSort(arr, low, high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now at right place 
        pi = partition(arr, low, high)
  
        # Separately sorting the elements before and after partition 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high) 


arr = [10, 7, 8, 9, 1, 5, 55, 6, 46, 52, 21, 22, 11, 70] 
n = len(arr) 
quickSort(arr, 0, n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print (arr[i])
