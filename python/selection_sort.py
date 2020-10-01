"""
Selection Sort
- It sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted 
  part and putting it at the beginning.
"""

A = [82, 55, 6, 46, 52, 21, 22, 11, 70] 
length_of_A = len(A)

# Traversing through all array elements 
for i in range(length_of_A):
    # Finding the minimum element in remaining unsorted array 
    min_idx = i
    for j in range(i+1, length_of_A):
        if A[min_idx] > A[j]: 
            min_idx = j 
              
    # Swapping the found minimum element with the first element         
    A[i], A[min_idx] = A[min_idx], A[i] 

print ("Sorted Array: ")
for i in range(len(A)):
    print(A[i])
