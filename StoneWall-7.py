#Cover "Manhattan skyline" using the minimum number of rectangles. 
from collections import deque
from operator import add
from functools import reduce
def solution(H):
    """O(N)

    Args:
        H ([type]): [description]

    Returns:
        [type]: [description]
    """
    q=deque([0])
    print("q", q)
    counter=0
    i=0
    sum=0
    while(i<len(H)):
        #[sum:=sum+i for i in q]
        diff=H[i]-sum
        if(diff>0):
            q.append(diff)
            sum+=diff
            counter+=1
            i+=1
        elif(diff<0):
            x=q.pop()
            sum-=x
        else:
            i+=1
    return counter


def solution1(H):
    """Time complexity O(N**2)

    Args:
        H ([type]): [description]

    Returns:
        [type]: [description]
    """
    q=deque([0])
    print("q", q)
    counter=0
    i=0
    while(i<len(H)):
        sum=0
        #sum=reduce(lambda x,y: x+y, q)
        #sum=reduce(add,q)
        [sum:=sum+i for i in q]
        diff=H[i]-sum
        if(diff>0):
            q.append(diff)
            counter+=1
            i+=1
        elif(diff<0):
            q.pop()
        else:
            i+=1
    return counter

H=[8,8,5,7,9,8,7,4,8]
print(solution(H))
