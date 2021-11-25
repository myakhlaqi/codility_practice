
# Compute the number of intersections in a sequence of discs.
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter
import operator

def solution(A):
    intersects=0
    n=len(A)
    for i in range(n-1):
        for j in range(i+1,n):
            if( abs(j-i)<=A[i]+A[j] ):
                intersects+=1
    
    
    if(intersects>10000000):
        return -1
    return intersects


def solution2(A):
    intersects=0
    n=len(A)
    points=[]
    for i in range(n):
        points.append((i-A[i],"open"))
        points.append((A[i]+i,"close"))
    points.sort(key=operator.itemgetter(1),reverse=True)
    points.sort(key=operator.itemgetter(0))
    
    total_open=0
    for i in points:
        
        #print("points", points)    
        if (i[1]=="open"):
            intersects+=total_open
            total_open+=1
        if(i[1]=="close"):
            total_open-=1
        print("intersects", intersects,"\t Total:",total_open)
        
    
    if(intersects>10000000):
        return -1
    return intersects

print(solution2([1,5,2,1,4,0]))