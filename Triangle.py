# Determine whether a triangle can be built from a given set of edges.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    n=len(A)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                P,Q,R=A[i],A[j],A[k]
                
                if(P+Q>R and P+R>Q and Q+R>P):
                    return 1
    
                
    
    return 0

#A=[10,2,5,1,8,20]
A=[10,50,5,1]
print(solution(A))