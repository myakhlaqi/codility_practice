#Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).

# you can write to stdout for debugging purposes
# print("this is a debug message")

import sys
def solution(A):
    n=len(A)
    A.sort(key= lambda x: abs(x),reverse=True)
    if(n<3):
        return 0
    else:
        max=-sys.maxsize

        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    result=A[i]*A[j]*A[k]
                    # print("{},{},{}={}".format(i,j,k,result))
                    if(result>max):
                        max=result
                    
        return max

def solution2(A):
    A_negative=[]
    n=len(A)
    has_zero= 0 in A
    A_positive=[]
    for i in range(len(A)):
        if(A[i]>=0):
            A_positive.append(A[i])
        elif A[i]<0:
            A_negative.append(A[i])
    
    if(len(A)<3):
        return 0
    elif (len(A)==3):
        return A[0]*A[1]*A[2]
    else:
        A_positive.sort(reverse=True)
        print("A_positive", A_positive)
        A_negative.sort(reverse=True)
        print("A_negative", A_negative)
        if(len(A_negative)==0 ):
            return A_positive[0]*A_positive[1]*A_positive[2]
        elif (len(A_positive)==0):
            return A_negative[0]*A_negative[1]*A_negative[2]
        else:
            if(len(A_negative)>=2):
                r1=A_positive[0]*A_negative[len(A_negative)-1]*A_negative[len(A_negative)-2]
            else:
                r1=-sys.maxsize

            if(len(A_positive)>=3):
                r2=A_positive[0]*A_positive[1]*A_positive[2]
            else:
                r2=-sys.maxsize
            if(r1>r2):
                return r1
            else:
                return r2
        
def solution3(A):
    n=len(A)
    A.sort(reverse=True)
    max1 = (A[0] * A[1] * A[2])
    max2 = (A[0]*A[n-1]*A[n-2])

    return max(max1,max2)
        
A=[-1,-2,-3,9]
print(solution(A))
print(solution2(A))
print(solution3(A))
