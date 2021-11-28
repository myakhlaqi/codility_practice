#Given a log of stock prices compute the maximum possible earning.
import sys

def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice

def solution1(A):
    n=len(A)
    max_profit=-sys.maxsize
    for i in range(n-1):
        for j in range(i+1,n):
            profit=A[j]-A[i]
            print("({}-{}) => profit:{}".format(i,j,profit))
            if(max_profit<profit):
                max_profit=profit
                
    return max_profit
A=[0]*6
A[0] = 23171
A[1] = 21011
A[2] = 21123
A[3] = 21366
A[4] = 21013
A[5] = 21367
print(solution1(A))