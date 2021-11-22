def mushrooms(A, k, m):
    n = len(A)
    result = 0
    pref = prefix_sums(A)
    print(31*" ", [*range(0,len(A))])
    print(31*" ", A)
    for p in range(min(m, k) + 1):
        left_pos = k - p
        right_pos = min(n - 1, max(k, k + m - 2 * p))
        #print("\tmax({},{}):{}\t min({},{}):{}".format(k,k + m - 2 * p,max(k, k + m - 2 * p),n-1,max(k, k + m - 2 * p), min(n - 1, max(k, k + m - 2 * p)) ))
        result = max(result, count_total(pref, left_pos, right_pos))
        print("1- P:{0:<4d}({1:^5d}-{2:^5d})=>{3:4d}".format(\
            p,left_pos,right_pos,count_total(pref, left_pos, right_pos)),end="   ")
        print((left_pos)*"   ",A[left_pos:right_pos+1])
    print()
    print(31*" ", [*range(0,len(A))])
    print(31*" ", A)

    for p in range(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2 * p)))
        result = max(result, count_total(pref, left_pos, right_pos))
        print("1- P:{0:<4d}({1:^5d}-{2:^5d})=>{3:4d}".format(\
            p,left_pos,right_pos,count_total(pref, left_pos, right_pos)),end="   ")
        print((left_pos)*"   ",A[left_pos:right_pos+1])

    return result

def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def count_total(P, x, y):
    return P[y + 1] - P[x]


A= [20,30,17,5,1,3,9,\
     2,3,7,5,1,5,1,3,2,3,1,5,1]
print(A.sort())

print(len(A))
#A= [2,3,7,5,1,3,9]

print(mushrooms(A,4,6))
