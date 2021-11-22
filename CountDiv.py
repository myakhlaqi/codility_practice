# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(A, B, K):
    result=0
    result=((B-A)//K)+1
    if(A%K!=0):
        result-=1
    return result


print(solution(6,12,2))
print(solution(6,13,2))
print(solution(7,13,2))