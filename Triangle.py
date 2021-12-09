# Determine whether a triangle can be built from a given set of edges.

def solution(A):
    n=len(A)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                P,Q,R=A[i],A[j],A[k]
                if(P+Q>R and P+R>Q and Q+R>P):
                    return 1
    return 0

def solution2(A):
    n=len(A)
    A.sort()
    for i in range(n-2):
        P,Q,R=A[i],A[i+1],A[i+2]
        if(P+Q>R and P+R>Q and Q+R>P):
            return 1
        
    
    return 0


A=[10,2,5,1,8,20]
#A=[10,50,5,1]
print(solution2(A))
