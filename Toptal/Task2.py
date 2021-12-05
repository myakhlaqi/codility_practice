
def solution(P,Q):
    n=len(P)
    Q_empty=[(Q[i]-P[i]) for i in range(n)]
    print("Q_empty", Q_empty)
    Q_empty.sort(reverse=True)
    print("Q_empty", Q_empty)
    car_count=0
    i=sum(P)
    j=0
    while(i>0):
        i-=Q_empty[j]
        car_count+=1
    return car_count

P=[1,1,3,2,1]
Q=[2,1,4,2,6]
print(solution(P,Q))