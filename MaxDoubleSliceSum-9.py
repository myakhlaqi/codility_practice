#Find the maximal sum of any double slice.
#https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/

import sys
import copy
def solution(A):
    
    max_sum_endingat=[]
    max_sum_startat=[]
    n=len(A)
    if(n==0):
        return 0
    elif(n==3):
        return sum(A[0]+A[2])
    else:
        max_ending = max_slice = -sys.maxsize
        for i in range(len(A)):
            max_ending =max(A[i],max_ending + A[i])
            max_sum_endingat.append(max_ending)
            max_slice = max(max_slice, max_ending)
            
            x="".join([",{0:>3d}".format(x) for x in max_sum_endingat])
            print("[{1:<{0}s}], sum: {2:^3d}, max_slice: {3:^3d}".format(len(A)*4,x,max_ending,max_slice))
        max_ending = max_slice = -sys.maxsize
        for i in range(n-1,-1,-1):
            max_ending =max(A[i],max_ending + A[i])
            max_sum_startat.append(max_ending)
            max_slice = max(max_slice, max_ending)
            x="".join([",{0:>3d}".format(x) for x in max_sum_startat])
            print("[{1:<{0}s}], sum: {2:^3d}, max_slice: {3:^3d}".format(len(A)*4,x,max_ending,max_slice))
        
        max_double=-sys.maxsize
        for k in range(1,n-1):
            max_double=max(max_double,max_sum_endingat[k-1]+max_sum_startat[(n-1)-(k+1)])

        
        return max_double

#print(solution([-10,-20]))
A=[3,2,6,-1,4,5,-1,2]
#A=[3,2,-6,4,0]
#A=[1,1,2,-3,-2,-1,9,9,8,-8,10,11,12]
#A=[1,2,-5,-1,8,8,8,-3]
print(solution(A))
