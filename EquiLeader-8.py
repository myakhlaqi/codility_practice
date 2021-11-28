#Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.
from collections import deque
def leader_all(A):
    stack=deque()
    counter=0
    leaders=[]
    for i,value in enumerate(A[:-1]):
        if(len(stack)==0):
            stack.append(value)
            counter+=1
        else:
            if(value!=stack[-1]):
                stack.pop()
            else:
                stack.append(value)
                counter+=1
        if(counter>((i+1)//2)):
            leaders.append(stack[0])
        else:
            leaders.append(None)
    return leaders

def solution(A):
    n=len(A)
    left_leaders=leader_all(A[:-1])
    B=A[::-1]
    right_leaders=leader_all(B[:-1])
    counter=0
    for i in range(n-1):
        if(right_leaders[i]==left_leaders[i]):
            counter+=1
    return counter
        
                

def leader(A):
    stack=deque()
    n=len(A)
    leader=-1
    counter=0
    leader_index=-1
    for i in range(n):
        if(len(stack)==0):
            stack.append(A[i])
        else:
            if(stack[-1]!=A[i]):
                stack.pop()
            else:
                stack.append(A[i])
    
    if(len(stack)>=1):
        leader=stack[0]
    for i in range(n):
        if(A[i]==leader):
            counter+=1
            leader_index=i
    if(counter>n//2):
        return leader,leader_index
    else:
        return (-1,-1)

def solution1(A):
    n=len(A)
    counter=0
    for i in range(n):
        L1,i1=leader(A[0:i+1])
        L2,i2=leader(A[i+1:n])
        print("{},{}=> ({},{}) and ({},{})".format(A[0:i+1],A[i+1:n],L1,i1,L2,i2))
        if(i1!=-1 and i2!=-1 and L1==L2):
            counter+=1
            print("find")
    return counter
A=[4,3,4,4,4,2]

#A=[-1, 4, -1, 3, -1]
print(solution(A))

