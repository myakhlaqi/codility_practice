

def solution(A, B, K):
    b = (B//K) + 1  
    a = (A//K) + 1  
    if (A%K == 0) :#// "A" is inclusive; if divisible by K then
        a-=1        #//   remove 1 from "a"
        
    return b-a     #// return integers in rang


print(solution(6,12,2))
print(solution(6,13,2))
print(solution(7,13,2))
