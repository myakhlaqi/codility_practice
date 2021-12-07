#
def solution(P,Q):
    """Find the minimum number of the car for given P and Q and

    Args:
        P (list): list of number of people inside corresponding car in Q
        Q (list): maximum capacity of a car

    Returns:
        int: minimum number of the car reqired for all
    """
    n=len(P)
    Q_empty=[(Q[i]-P[i]) for i in range(n)]
    Q_empty.sort(reverse=True)
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