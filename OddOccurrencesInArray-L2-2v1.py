#!/usr/bin/env python3

def solution(A):
    n=None
    while len(A)>0:
        indexes= [i for i,x in enumerate(A) if x==A[0]] 
        
        print("indexes:",indexes)
        
        if len(indexes)==1:
            n=A[indexes[0]]
        for x in indexes:
            A[x]=-1
        A=list(filter(lambda a: a != -1, A))
        print(A)

    return n

print("final result:",solution([]))
