# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter
def solution(A):
    dic_a= dict(Counter(A))
    print("dic_a", dic_a)
    for i in range(1,len(A)+1):
        if not i in dic_a:
            return 0
        
    return 1


print(solution(([4,1,3])))