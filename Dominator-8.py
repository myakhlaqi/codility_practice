# Find an index of an array such that its value occurs at more than half of indices in the array.

from collections import Counter
import sys
def solution(A):
    dic_A=dict(Counter(A))
    max=-sys.maxsize
    dominant_ixs=0
    B=[]
    for key in dic_A:
        if dic_A[key]>max:
            max=dic_A[key]
            dominant_ixs=key
    if(max>=(len(A)//2+1)):
        B=[i for i in range(len(A)) if A[i]==dominant_ixs]
        return B[0]
    return -1


print(solution([3, 4, 3, 2, 3, -1, 3, 3]))
