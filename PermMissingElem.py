def solution(A): 
    set_a=set(A)
    set_b={*range(1,len(A)+2)} 
    # print("set_b", set_b)
    result=set_b - set_a
    # print("result", result)
    return list(result)[0]
# print(solution([2,3,1,5]))
