import sys
import math

def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def count_total(P, x, y):
    return P[y + 1] - P[x]
def solution(A):
    half_pollution=sum(A)/2
    A.sort(reverse=True)
    n=len(A)
    last_sum=0
    i=0
    filter_count=0
    P=prefix_sums(A)
    last_pollution=max(A,default=0)
    while i<n-1:
        while(A[i]>=A[i+1]):
            A[i]/=2
            filter_count+=1
            last_pollution=count_total(P,i+1,n-1)+last_sum+A[i]
            if(last_pollution<=half_pollution):
                return filter_count
        last_sum+=A[i]
        i+=1
    if(last_pollution<half_pollution):
        return filter_count
    else:
        while(last_pollution>half_pollution):
            A[i]/=2
            filter_count+=1
            last_pollution=last_sum+A[i]
    return filter_count



#A=[5,19,8,1]
#A=[10,10]
#A=[5,3,0]
A=[]
print(solution(A))
A=[1]
print(solution(A))
A=[10,20,30,40]
print(solution(A))
A=[0,0,10,0]
print(solution(A))

