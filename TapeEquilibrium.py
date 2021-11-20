
def solution(A):
    dif_list=[]
    for part in range(1,len(A)):
        p1=A[:part]
        p2=A[part:]
        dif_list.append(abs(sum(p1)-sum(p2)))
    
    return  min(dif_list,default=0)
        

print(solution([3,1,2,4,3]))
# for i in range(1,5):
#     print(dif([3,1,2,4,3],i))
