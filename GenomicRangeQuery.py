#!/usr/bin/env python3
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


def solution1(S, P, Q):
    n=len(S)
    m=len(P)
    dna_matrix=[[0 for col in range(n+1)] for row in range(3)]
    
    for i,ch in enumerate(S):
        dna_matrix[0][i+1]=dna_matrix[0][i]+( ch =='A')
        dna_matrix[1][i+1]=dna_matrix[1][i]+( ch =='C')
        dna_matrix[2][i+1]=dna_matrix[2][i]+( ch =='G')
    print("dna_matrix", dna_matrix)
    
    result=[]
    for i in range(m):
        start=P[i]
        end=Q[i]+1
        if(dna_matrix[0][end]-dna_matrix[0][start]>0):
            result.append(1)
        elif (dna_matrix[1][end]-dna_matrix[1][start]>0):
            result.append(2)
        elif (dna_matrix[2][end]-dna_matrix[2][start]>0):
            result.append(3)
        else:
            result.append(4)

    return result

print(solution1("CAGCCTA",[2,5,0],[4,5,6]))
