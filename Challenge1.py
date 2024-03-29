import re
import copy
from collections import Counter

def opposite(ch):
    if(ch == "a"):
        return "b"
    else:
        return "a"

def solution(S):
    result=re.finditer(r'(a+|\?+|b+)',S)
    B=[]
    for m in result:
        print("{} = {}, {}".format(m.group()[0],m.span(),(m.end()-m.start())))
        B.append([m.group()[0],m.end()-m.start()])
    # print("B", B)
    C=copy.deepcopy(B)
    for i in range(1,len(B)-1):
        if(B[i][0]=="?"):
            next=B[i+1]
            prev=B[i-1]
            pattern=prev[0]+"?"+next[0]
            replace=""
            if(pattern in ["a?a","b?b"]):
                if(B[i][1]%2==0):
                    if(next[1]>prev[1]):
                        replace=(prev[0]+opposite(prev[0]))*(B[i][1]//2)
                        B[i-1][1]+=1  
                    elif next[1]<prev[1]:
                        replace=(opposite(prev[0])+prev[0])*(B[i][1]//2)
                        B[i+1][1]+=1
                    else:
                        replace=opposite(prev[0])*2+(opposite(prev[0])+prev[0])*((B[i][1]//2)-1)
                        B[i][0]="="
                        B[i][1]=2
                else:
                    replace=opposite(prev[0])+( (prev[0] + opposite(prev[0]) ) * (B[i][1]//2) )
            else:
                if(B[i][1]%2==1):
                    if(next[1]>prev[1]):
                        replace=opposite(next[0])+((next[0]+opposite(next[0]) )*(B[i][1]//2))
                        B[i-1][1]+=1
                    elif next[1]<prev[1]:
                        replace=opposite(prev[0])+(( prev[0]+opposite(prev[0]) )*(B[i][1]//2) )
                        B[i+1][1]+=1
                    else:
                        if(B[i][1]==1):
                            B[i-1][1]+=1
                            C[i]=prev[0]
                        else:
                            replace=opposite(prev[0])+((opposite(prev[0])+prev[0] )*(B[i][1]//2))
                            B[i][0]="="
                            B[i][1]=2
                else:
                    replace=(opposite(prev[0])+prev[0])*(B[i][1]//2)
            #print("replace", replace)
            C[i]=(replace,1)
        # print(B)
    print("".join([x[0]*x[1] for x in C]))

    
    return max([x[1] for x in B if x[0]!="?"],default=1)


def solution2(S):
    result=re.finditer(r'(a+|\?+|b+)',S)
    print("result", result)
    B=[]
    for m in result:
        B.append([m.group()[0],m.end()-m.start()])
        
    for i in range(1,len(B)-1):
        if(B[i][0]=="?"):
            next=B[i+1]
            prev=B[i-1]
            pattern=prev[0]+"?"+next[0]
            if(pattern in ["a?a","b?b"]):
                if(next[1]>prev[1]):
                    B[i-1][1]+=1  
                elif next[1]<prev[1]:
                    B[i+1][1]+=1
                else:
                    B[i][0]="="
                    B[i][1]=2
            else:
                if(B[i][1]%2==1):
                    if(next[1]>prev[1]):
                        B[i-1][1]+=1
                    elif next[1]<prev[1]:
                        B[i+1][1]+=1
                    else:
                        if(B[i][1]==1):
                            B[i-1][1]+=1
                        else:
                            B[i][0]="="
                            B[i][1]=2

    return max([x[1] for x in B if x[0]!="?"],default=1)


s1 = "????aa?bb??aa???bbb??aa??b?bb??"
s2 = "aa??bbb"
s3 = "aa?????bbb"
s4 = "aa?b?aa"
s5= "bb??bb????aa"

print(solution(s5))
# print(solution(s2))
# print(solution(s3))
# print(solution(s4))
