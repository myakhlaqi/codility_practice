# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    counters=[0]*N
    #print("counters_dic", counters)
    max_value=0
    update=0
    for item in A:
        if(item>=1 and item <=N):
            counters[item-1]=max([update,counters[item-1]])
            counters[item-1]+=1
            if(counters[item-1]>max_value):
                max_value=counters[item-1]
        elif item==N+1:
            update=max_value
    for i in range(N):
        counters[i] = max(counters[i],update)
            
    return counters
