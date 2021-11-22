# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#Count the number of passing cars on the road.


def solution1(A):
    """O(N*2)"""
    counter=0
    if(len(A)>1000000000):
        return -1
    else:
        for i in range(len(A)):
            if A[i]==0:
                for j in range(i+1,len(A)):
                    if(A[j]==1):
                        print("({},{}),".format(i,j))
                        counter+=1
    return counter

def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def count_total(P, x, y):
    return P[y + 1] - P[x]

def solution(A):
    """O(N)"""
    counter=0
    P=prefix_sums(A)
    #print("P", P)
    for i in range(len(A)):
        if(A[i]==0):
            counter+=count_total(P,i,len(A)-1)
    if(counter>1000000000):
        return -1
    else:
        return counter


print(solution([0,1,0,1,1]))