#!/usr/bin/env python3

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S, P, Q):
    dic_if={'A':1,'C':2,'G':3,'T':4}
    result=[]
    for i in range(len(Q)):
        dna=S[P[i]:Q[i]+1]
        min=dic_if[dna[0]]
        for ch in dna:
            if(dic_if[ch]<min):
                min=dic_if[ch]
        result.append(min)
        
        
    return result

print(solution("CAGCCTA",[2,5,0],[4,5,6]))