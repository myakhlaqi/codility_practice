from collections import Counter
import re
import copy
import sys
from typing import MappingView

def solution(S):
    S_counter=dict(Counter(S))
    result=re.finditer(r'(a+|b+)',S)
    print("result", result)
    B=[]
    for m in result:
        B.append([m.group()[0],m.end()-m.start()])
    print("B", B)  

    a_count= S_counter["a"] if "a" in S_counter else 0
    b_count= S_counter["b"] if "b" in S_counter else 0
    
    swap_count=0
    
    if(a_count<3 or b_count<3):
        return -1
    elif( len(list(filter(lambda x: x[0]=="b" and x[1]>=3, B)))>0 and   len(list(filter(lambda x: x[0]=="a" and x[1]>=3, B)))>0):
        return 0
    else:
        a_max_length=max([x[1] for x in B if x[0]=="a"])
        b_max_length=max([x[1] for x in B if x[0]=="b"])
        
        a_sum=0
        pre,main,next=0,0,0
        min_total=sys.maxsize
        if(a_max_length<3):
            for i in range(len(B)):
                if(B[i][0]=="a"):
                    left_a_gap= sys.maxsize if a_sum==0 else B[i-1][1]
                    a_sum+=B[i][1]
                    right_a_gap= sys.maxsize if a_sum==a_count else B[i+1][1]
                    
                    min_swap=0
                    if(B[i][1]==2):#if aa 
                        min_swap=min(left_a_gap,right_a_gap)
                    else:# if just one a
                        min_swap=(left_a_gap+right_a_gap)
                    if(min_swap<min_total):
                        main=i
                        pre=None if left_a_gap==sys.maxsize else i-2
                        next=None if right_a_gap==sys.maxsize else i+2
                        print("{},{},{}".format(pre,main,next))
                    min_total=min(min_swap,min_total)
            
            if(B[main][1]==1):
                B[main][1]+=2
                B[pre][1]-=1
                B[next][1]-=1
                swap_count+=(B[main-1][1]+B[main+1][1])
            elif(B[main][1]==2):
                B[main][1]+=1
                if(pre is None and next is None):
                    return -1
                elif(pre is None):
                    B[next][1]-=1
                    swap_count+=B[main+1][1]
                elif(next is None):
                    B[pre][1]-=1
                    swap_count+=B[main-1][1]
        B=[x for x in B if x[1]>0]
        B_stack=[]
        for i in B:
            if(len(B_stack)==0):
                B_stack.append(i)
            else:
                if(B_stack[-1][0]==i[0]):
                    B_stack[-1][1]+=i[1]
                else:
                    B_stack.append(i)
        B=B_stack
        b_max_length=max([x[1] for x in B if x[0]=="b"])
        print("=====================b=================")
        b_sum=0
        min_total=sys.maxsize
        if(b_max_length<3):
            for i in range(len(B)):
                if(B[i][0]=="b"):
                    left_a_gap= sys.maxsize if b_sum==0 else B[i-1][1]
                    b_sum+=B[i][1]
                    right_a_gap= sys.maxsize if b_sum==b_count else B[i+1][1]
                    min_swap=0
                    if(B[i][1]==2):#if aa 
                        min_swap=min(left_a_gap,right_a_gap)
                    else:# if just one a
                        min_swap=(left_a_gap+right_a_gap)
                    if(min_swap<min_total):
                        main=i
                        pre=None if left_a_gap==sys.maxsize else i-2
                        next=None if right_a_gap==sys.maxsize else i+2
                        print("{},{},{}".format(pre,main,next))
                    min_total=min(min_swap,min_total)
            
            if(B[main][1]==1):
                B[main][1]+=2
                B[pre][1]-=1
                B[next][1]-=1
                swap_count+=(B[main-1][1]+B[main+1][1])
            elif(B[main][1]==2):
                B[main][1]+=1
                if(pre is None and next is None):
                    return -1
                elif(pre is None):
                    B[next][1]-=1
                    swap_count+=B[main+1][1]
                elif(next is None):
                    B[pre][1]-=1
                    swap_count+=B[main-1][1]
    print("B", B)          
    return swap_count

#print(solution("aabbbbababa"))
print(solution("ababab"))
#print(solution("abbbbaa"))
#print(solution("bbbababaaab"))
#print(solution("abbabb"))
