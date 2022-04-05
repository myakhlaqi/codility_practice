#Find the smallest positive integer that does not occur in a given sequence

from collections import Counter 
def solution(A):
    dic_a=dict(Counter(A))
    if(len(A)==0):
        return 1
    # print("dic_a", dic_a)
    max_value=max(A)
    if(max_value<=0):
        return 1
    else:
        for x in range(1,max_value):
            if not x in dic_a:
                return x
        return max_value+1

# print(solution([1,3,6,4,1,2]))
