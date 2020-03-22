"""
Practical Algorithms, 2019-2020
Coursework 1
1a: Implement the following algorithms in Python:
a)	QUICKSORT, based on the pseudocode for QUICKSORT introduced in topic A4, 
    including procedure PARTITION implementing right-most element pivot selection.
SAMPLE SOLUTION    
"""

#%% A convenience SWAP function
def SWAP(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp


#%% The PARTITION function used by QUICK SORT
# The last element is the "Pivot"
def PARTITION(A,p,r):
    q = r     #pivot index "q" is the last index "r"
    x = A[q]  #read pivot value
    i = p-1   #i marks the boundary between < and > pivot regions, starts at -1 (if p is 0)
    
    #recall, python range goes up to but excludes the ending index, 
    #so range(p,r) this will iterate from p to r-1, as indicated in the pseudo code
    for j in range (p, r):
        #swap into the "i" (or left) region any element less then pivot
        if A[j] <= x:
            i = i + 1
            SWAP(A,i,j)
        #no else branch, nothing do (except increment j)
        
    #final swapping in of pivot at its appropriate location, identified
    #by the boundary marker "i" (note this is outside the loop now)
    SWAP(A,i+1,r) 
    return i + 1

#%% Quick sort
def QUICK_SORT(A,p,r):
    #print message for viewing call trace
    #print ("QUICK_SORT called on A with p = ", p, ", and r = ", r, end = "")
    
    #keep partitioning and calling the sort recursively until you get 
    #so single elements (identified by p no longer being less than r)
    if p < r:
        q = PARTITION(A,p,r) #A[p:r] partitioned, and the position of pivot returned
        #print (": pivot with value ", A[q]," placed at q = ", q)
        #now that pivot's position is known (and it is in the correct location)
        #recursively call PARTITION_SORT on all elements on its left, and then on its right
        #but excluse the pivot itself as it is already in its correct location
        QUICK_SORT(A,p,q-1)
        QUICK_SORT(A,q+1,r)
    #else:
        #just printing end of line
        #print("")
        