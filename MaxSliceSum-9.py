#Find a maximum sum of a compact subsequence of array elements.
import sys
def solution(A):
    max_ending = max_slice = -sys.maxsize
    if(len(A)==1):
        return A[0]
    else:
        for a in A:
            max_ending =max(a,max_ending + a)
            max_slice = max(max_slice, max_ending)
        return max_slice

print(solution([5,-7,3,5,-2,4,-1]))
print(solution([3,2,-6,4,0]))
print(solution([3,2,-6,4,0]))
