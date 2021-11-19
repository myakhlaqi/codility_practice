#!/usr/bin/env python3

def solution(A):
    n=-1
    if len(A)==0:
        return 0
    elif len(A)==1:
        return A[0]
    else:
        while len(A)>0:
            #indexes= [i for i,x in enumerate(A) if x==A[0]] 
            try:
                index2=A.index(A[0],1)
                print("index2:",index2)
                A.pop(index2)
                A.pop(0)
                print(A)
            except ValueError:
                n=A[0]
                A.pop(0)

    return n

print("final result:",solution([9,3,9,3,9,7,9]))
