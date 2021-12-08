#!/usr/bin/env python3

def solution(a, k):
    n=len(a)
    if(n>0):
        for x in range(k):
            temp=a[n-1]
            for i in range(n-1,-1,-1):
                a[i]=a[i-1]
            a[0]=temp
    return a
    
#print(solution([1,2,3,0,5],8))
