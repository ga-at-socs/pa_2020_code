"""
Practical Algorithms, 2019-2020
Coursework 1
Tester script for Part 1
"""

import time
"""
t0 = time.clock()
my_result = do_my_sum(testdata)
t1 = time.clock()
print("my_result    = {0} (time taken = {1:.4f} seconds)"
        .format(my_result, t1-t0))
"""
import random as rand
import sys

import solution_1a as sol

#%%Random input array for testing functionality of sorting algos
N = 10      # size of input array
K = 1000    # range of numbers in input array
print(f"Creating random list of {N} integers in the range 1 - {K}")
a_unsorted = rand.sample(range(1,K),N)
print(f"Unsorted list is : ", a_unsorted)

# golden sort for comparison
a_sorted_gold = sorted(a_unsorted)  #sort in place using list object's
                                    #built-in function
print(f"Sorted list (golden reference for testing) is : ", a_unsorted)
print("")

#%%Testing QUICK_SORT functionality(1a)
print(f"Testing solution to 1a, QUICK_SORT... ", end = "")

#sort using QUICK_SORT imported from solution
a_sorted_testing = a_unsorted.copy()
try:
    sol.QUICK_SORT(a_sorted_testing,0,len(a_sorted_testing)-1)
except:
    print(f"Testing not carried out."
          "Unable to import the required function QUICK_SORT from module OR"
          "imported function has runtime errors"
          )    

#test result 
if a_sorted_gold == a_sorted_testing:
    print("TEST PASSED")
else:
    print("TEST FAILED!")


