
A = [64, 25, 12, 22, 11]
for i in range(len(A)):

    # Find the minimum element in remaining
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]

print ("Sorted array")
for i in range(len(A)):
    print("%d" % A[i]),

   '''
   Time execution - .78 sec(s)
   time complexity :
   worst-case space complexity = O(1)
   Best-Case performance = O(n^2)
   Worst-Case performance  =O(n^2)
   
   '''