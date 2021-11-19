#!/usr/bin/env python3
from collections import Counter

def solution(A):
    if(len(A)==0):
        return -1
    elif len(A)==1:
        return A[0]
    else:
        a_dic=Counter(A)
        print(a_dic)
        n=[x for x in a_dic if a_dic[x]%2==1]
        return n[0]

def solution2(A):
    dic={}
    n=0
    for x in A:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1
    for x in dic:
        if(dic[x]%2==1):
            n=x
            break
    return n
        

print("final result:",solution([]))
print("final result:",solution2([9,3,9,3,9,7,9]))
