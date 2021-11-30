#Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.
from collections import deque

def solution3(A):
    """ O(N) and 100 precentage of correctness"""
    stack=deque()
    n=len(A)
    leader=None
    leader_count=0
    for i in range(n):
        if(len(stack)==0):
            stack.append(A[i])
        else:
            if(stack[-1]!=A[i]):
                stack.pop()
            else:
                stack.append(A[i])
    if(len(stack)>0):
        leader=stack[0]
    for i in range(n):
        if(A[i]==leader):
            leader_count+=1
    if(leader_count<=n//2):
        return 0
    else:
        equi_leaders = 0
        leader_count_so_far = 0
        for index in range(n):
            if A[index] == leader:
                leader_count_so_far += 1
            if leader_count_so_far > (index+1)//2 and \
            leader_count-leader_count_so_far > (n-index-1)//2:
                # Both the head and tail have leaders of the same value
                # as "leader"
                equi_leaders += 1
        return equi_leaders

def leader_all(A):
    stack=deque()
    counter=0
    leaders=[]
    for i,value in enumerate(A):
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

def solution2(A):
    """O(N) but error in one case A=[4,1,2,3,4,4,4] expected 0 get 2"""
    n=len(A)
    left_leaders=leader_all(A[:-1])
    #print("left_leaders", left_leaders)
    B=A[::-1]
    right_leaders=leader_all(B[:-1])
    right_leaders=right_leaders[::-1]
    #print("right_leaders", right_leaders)
    counter=0
    for i in range(len(left_leaders)):
        if(right_leaders[i]==left_leaders[i] and right_leaders[i]!=None and left_leaders[i]!=None):
            counter+=1
    return counter

def leader(A):
    stack=deque()
    n=len(A)
    leader=None
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
    if(len(stack)>0):
        leader=stack[0]
    for i in range(n):
        if(A[i]==leader):
            counter+=1
            leader_index=i
    if(counter>n//2):
        return leader_index
    else:
        return None

def solution1(A):
    n=len(A)
    counter=0
    for i in range(n):
        left_leader_index=leader(A[0:i+1])
        right_leader_index=leader(A[i+1:n])
        
        if(left_leader_index!=None and right_leader_index!=None and A[left_leader_index]==A[right_leader_index]):
            #print("{},{}=> ({},{}) and ({},{})".format(A[0:i+1],A[i+1:n],A[left_leader_index],left_leader_index,A[right_leader_index],right_leader_index))
            counter+=1
    return counter
#A=[0]*10

#A=[-1, 4, -1, 3, -1]
#A=random.sample(range(-10000000000,1000000000),300)
#A=[-999999999]*300
#A=[4,1,2,3,4,4,4]
A=[4,3,4,4,4,2]
print("leader :",leader(A))
print(solution1(A))
print(solution2(A))
print(solution3(A))
