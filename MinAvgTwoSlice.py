#!/usr/bin/env python3
#Find the minimal average of any slice containing at least two elements.
import random

def solution(A):
    # write your code in Python 3.6
    n=len(A)
    P=prefix_sums(A)
    min=max(A)
    min_index=-1
    for i in range(n-1):
        for j in range(i+1,n):
            avg=count_total(P,i,j)/(j-i+1)
            print("({:^5d},{:^5d}) = sum({:^5d}/{:^5d}) =avg {:^5.2f} , min={:^5.2f}, index={:d}"\
                .format(i,j,count_total(P,i,j),j-i+1,avg,min,min_index))
            if(avg<min):
                min=avg
                min_index=i
    
    return min_index


def solution2(A):
    # write your code in Python 3.6
    n=len(A)
    P=prefix_sums(A)
    min=max(A)
    min_index=0
    for i in range(n-1):
        for j in range(i+1,n):
            m=(j-i+1)
            avg=count_total(P,i,j)/m
            if(avg<min):
                min=avg
                min_index=i
            if(j!=n-1):
                print("({:^5d},{:^5d}) = sum({:^5d}/{:^5d}) =avg {:^5.2f} , min={:^5.2f}, index={:d}, A[{:d}]={:d}"\
                    .format(i,j,count_total(P,i,j),m,avg,min,min_index,j+1,A[j+1]))
                if(A[j+1]>avg):
                     break

    
    return min_index

def solution3(A):
    # write your code in Python 3.6
    n=len(A)
    P=prefix_sums(A)
 
    min_val=max(A)
    min_index=0
    for i in range(n-1):
        for j in range(i+1,min(n,i+3)):
            m=(j-i+1)
            avg=count_total(P,i,j)/m
            if(avg<min_val):
                min_val=avg
                min_index=i
            if(j!=n-1):
                print("({:^5d},{:^5d}) = sum({:^5d}/{:^5d}) =avg {:^5.2f} , min={:^5.2f}, index={:d}, A[{:d}]={:d}"\
                    .format(i,j,count_total(P,i,j),m,avg,min_val,min_index,j+1,A[j+1]))

    
    return min_index


def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def count_total(P, x, y):
    return P[y + 1] - P[x]

A=[4,2,2,5,1,5,8]
#A=[4,2,200,1,1,1,5,1,-800,0,-4,8]
P=prefix_sums(A)
print("P", P)

print(solution3(A))
