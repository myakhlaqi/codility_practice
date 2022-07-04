#Find the maximal sum of any double slices.
#https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/ 

import sys

def solution(A):
    
    n=len(A)
    max_sum_endingat=[0]*n
    max_sum_startat=[0]*n

    if(n<=3):
        return 0
    else:

        for i in range(1,n-1):
            max_sum_endingat[i] =max(0,max_sum_endingat[i-1] + A[i])
        max_ending = max_slice = -sys.maxsize
        for i in range(n-2,0,-1):
            max_sum_startat[i] =max(0,max_sum_startat[i+1] + A[i])
        max_double=-sys.maxsize
        for k in range(1,n-1):
            max_double=max(max_double,max_sum_endingat[k-1]+max_sum_startat[k+1])

        
        return max_double

#print(solution([-10,-20]))
A=[3,2,6,-1,4,5,-1,2]
#A=[3,2,-6,4,0]
#A=[1,1,2,-3,-2,-1,9,9,8,-8,10,11,12]
#A=[1,2,-5,-1,8,8,8,-3]
A=[5, 17, 0, 3]
print(solution(A))
