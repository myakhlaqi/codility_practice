#Find the maximal sum of any double slice.
#https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/

import sys
def solution(A):
    max_ending = max_slice = -sys.maxsize
    sub_list=[]
    flag=True
    if(len(A)==0):
        return 0
    elif(len(A)==3):
        return sum(A)
    else:
        for a in A:
            if(max_ending+a>=a):
                sub_list.append(a)

            max_ending =max(a,max_ending + a)
            max_slice = max(max_slice, max_ending)


            print("{}, sum: {}, max_slice: {}".format(sub_list,max_ending,max_slice))
        return max_slice

#print(solution([-10,-20]))
#A=[3,2,6,-1,4,5,-1,2]
#A=[3,2,-6,4,0]
#A=[1,1,2,-3,-2,-1,9,9,8,-8,10,11,12]
A=[1,2,-5,-1,8,8,8,-3]
print(solution(A))
