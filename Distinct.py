# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import Counter
def solution(A):
    dic_a=dict(Counter(A))
    return len(dic_a)
 
