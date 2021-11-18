#!/usr/bin/env python3

def to_binary(n):
    list=[]
    while n!=0:
        list.insert(0,n%2)
        n=n//2
    return list
def solution(N):
    binary=to_binary(N)
    j=0
    max=0
    j=0
    i=1
    zero=0
    while(j<len(binary)):
        while(binary[i]!=1):
            zero=zero+1
            i=i+1
        print("zero count", zero)
        if(zero>max):
            max=zero
        zero=0
        i=i+1
        j=i
    return max
            
    
print(to_binary(529))
print("max is ", solution(529))