# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    counters_dic=[0]*N
    print("counters_dic", counters_dic)
    
    max=0
    for i,v in enumerate(A):
        if(v>=1 and v <=N):
            counters_dic[v-1]+=1
            if(counters_dic[v-1]>max):
                max=counters_dic[v-1]
        elif v==N+1:
            counters_dic=[max]*N
    return counters_dic

print(solution(5,[3,4,4,6,1,4,4]))