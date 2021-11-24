#!/usr/bin/env python3

from collections import Counter

"""Sort Algorithms
"""
def selection_sort(A):
    pass
def countingSort(A):
    c=dict(Counter(A))
    max_value=max(A)
    sorted_A=[]
    for i in range(max_value+1):
        if(i in c):
            for j in range(c[i]):
                sorted_A.append(i) 
            
    return sorted_A
    
A=[8,9,7,5,2,1,3,4]
print(countingSort(A))
