#Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys

def solution(A):
    n=len(A)
    A.sort(key= lambda x: abs(x),reverse=True)
    print("A", A)
    if(n<3):
        return 0
    else:
        max=A[0]
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    result=A[i]*A[j]*A[k]
                    print("{},{},{}={}".format(i,j,k,result))
                    if(result>max):
                        max=result
                    
        return max

A=[1,1,-1]
print(solution(A))