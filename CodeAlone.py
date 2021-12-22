from collections import Counter
import re
import copy

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
        a_max_index=B.index(['a',a_max_length])
        
        b_max_length=max([x[1] for x in B if x[0]=="b"])
        b_max_index=B.index(['b',b_max_length])

        if(a_max_length<3):
            while(a_max_length<3):
                a_replace_ix=-1
                for i in range(a_max_index+1,len(B)):
                    if(B[i][0]=="a" and B[i][1]>0):
                        a_replace_ix=i
                        break
                if(a_replace_ix==-1):#didn't find, so search other side
                    for i in range(a_max_index-1,-1,-1):
                        if(B[i][0]=="a" and B[i][1]>0):
                            a_replace_ix=i
                            break
                gap_size=sum([x[1] for x in B[min(a_replace_ix,a_max_index)+1:max(a_replace_ix,a_max_index)]])
                B[a_max_index][1]+=1
                a_max_length+=1
                B[a_replace_ix][1]-=1
                swap_count+=gap_size
                print("{}\tcount: {}\tB[{}]=>B[{}]".format("".join([x[0]*x[1] for x in B]),swap_count,a_replace_ix,a_max_index))
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
                    
        print("B_stack", B_stack)
        B=B_stack
        b_max_length=max([x[1] for x in B if x[0]=="b"])
        b_max_index=B.index(['b',b_max_length])
        print("=====================b {}=>{}=================".format(b_max_index,b_max_length))

        if(b_max_length<3):
            while(b_max_length<3):
                b_replace_ix=-1
                for i in range(b_max_index+1,len(B)):
                    if(B[i][0]=="b" and B[i][1]>0):
                        b_replace_ix=i

                        break
                if(b_replace_ix==-1):#didn't find, so search other side
                    for i in range(b_max_index-1,-1,-1):
                        if(B[i][0]=="b" and B[i][1]>0):
                            b_replace_ix=i
                            break
                print("b_replace_ix", b_replace_ix)
                gap_size=sum([x[1] for x in B[min(b_replace_ix,b_max_index)+1:max(b_replace_ix,b_max_index)]])
                B[b_max_index][1]+=1
                b_max_length+=1
                B[b_replace_ix][1]-=1
                swap_count+=gap_size
                print("{}\tcount: {}\tB[{}]=>B[{}]".format("".join([x[0]*x[1] for x in B]),swap_count,b_replace_ix,b_max_index))
                B=[x for x in B if x[1]>0]
                
    return swap_count

print(solution("baabaabaabaababaab"))
#print(solution("abbbbaa"))
#print(solution("bbbababaaab"))
#print(solution("abbabb"))
