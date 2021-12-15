#N voracious fish are moving along a river. Calculate how many fish are alive.

from collections import deque
def solution(A, B):
    q=deque()

#    for i in range(len(A)):
    i=0
    while (i<len(A)):
        if(len(q)==0):
            q.append((A[i],B[i]))
        else:
            if(q[-1][1]==1 and B[i]==0):
                if q[-1][0]<A[i]:
                    q.pop()
                    #q.append((A[i],B[i]))
                    continue
            else:
                q.append((A[i],B[i]))
        print("q", q)
        i+=1
        
    return len(q)

A,B=([4, 12, 2, 1, 5,8,6,9], [0, 1, 0, 1, 0,0,1,0])
print(solution(A,B))
