#!/usr/bin/env python3

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter
def solution(A):
    m=max(A,default=0)
    #print(m)
    result=1
    for x in range(1,m):
        if (not (x in A)):
            result=x
            return x;
    if m<=0:
        result=1
    else:
        result=m+1
    return result
    """Best performance 
    """
def solution2(A):
    dic=dict(Counter(A))
    max_item=max(A)
    
    for x in range(1,max_item):
        if not x in dic:
            return x
    
    if(max_item<=0):
        result=1
    else:
        result=max_item+1
    return result

def solution3(A):
    set_a=set(A)
    max_item=max(set_a,default=0)
    if max_item<=0:
        return 1
    else:
        set_b={*range(1,max_item+2)}
        set_result=set_b - set_a
        print(set_result)
        return min(set_result)
    

print(solution3([1, 3, 6, 4, 1, 2]))