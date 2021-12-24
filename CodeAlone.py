from collections import Counter
import re
import copy
import sys
from typing import MappingView
def reversChar(ch):
    return "a" if ch=="b" else "b"

def count_letters(S):
    result = re.finditer(r'(a+|b+)', S)
    #print("result", result)
    B = []
    for m in result:
        B.append([m.group()[0], m.end()-m.start()])
    return B


def solution2(S):
    B = count_letters(S)
    print("B", B)
    S_counter = dict(Counter(S))
    a_count = S_counter["a"] if "a" in S_counter else 0
    b_count = S_counter["b"] if "b" in S_counter else 0

    swap_count = 0

    if(a_count < 3 or b_count < 3):
        return -1
    elif(len(list(filter(lambda x: x[0] == "b" and x[1] >= 3, B))) > 0 and len(list(filter(lambda x: x[0] == "a" and x[1] >= 3, B))) > 0):
        return 0
    else:
        a_max_length = max([x[1] for x in B if x[0] == "a"])
        b_max_length = max([x[1] for x in B if x[0] == "b"])
        current_char = "a" if a_max_length>b_max_length else "b"
        while(a_max_length < 3 or b_max_length < 3):
            if(a_max_length < 3 and b_max_length < 3):
                if(getGap("a", B) > getGap("b", B)):
                    current_char="a"
                elif(getGap("a", B) < getGap("b", B)):
                    current_char="b"
            elif(a_max_length < 3):
                current_char = "a"
            else:
                current_char = "b"
            #sum = 0
            candidate_ix = -1
            next = -1
            pre = -1
            neighbor_ix=-1
            min_total_swap = sys.maxsize
            #total_sum = a_count if current_char == "a" else b_count
            for i in range(len(B)):
                if(B[i][0] == current_char):
                    left_gap = sys.maxsize if i==0 else B[i-1][1]
                    #sum += B[i][1]
                    right_gap = sys.maxsize if i==(len(B)-1) else B[i+1][1]
                    min_swap_sofar = 0
                    if(B[i][1] == 2):  # if aa
                        min_swap_sofar = min(left_gap, right_gap)
                    else:  # if just one a
                        min_swap_sofar = (left_gap+right_gap)
                    if(min_swap_sofar < min_total_swap):
                        candidate_ix = i
                        pre = None if left_gap == sys.maxsize else i-2
                        next = None if right_gap == sys.maxsize else i+2
                    elif(min_swap_sofar == min_total_swap):
                        if(B[candidate_ix][1]==2 and B[i][1]==2):
                            pre_min_size=min(B[candidate_ix-2][1] if pre is not None else sys.maxsize,B[candidate_ix+2][1] if next is not None else sys.maxsize)
                            current_min_size=min(B[i-2][1] if i-2>=0 else sys.maxsize,B[i+2][1] if i+2<len(B) else sys.maxsize)
                            if(current_min_size<pre_min_size):
                                candidate_ix = i
                                pre = None if left_gap == sys.maxsize else i-2
                                next = None if right_gap == sys.maxsize else i+2
                        if(B[candidate_ix][1]==1 and B[i][1]==2):
                                candidate_ix = i
                                pre = None if left_gap == sys.maxsize else i-2
                                next = None if right_gap == sys.maxsize else i+2                            
                    min_total_swap = min(min_swap_sofar, min_total_swap)
            if(B[candidate_ix][1] == 1):
                B_right = copy.deepcopy(B)
                B_right[next][1] -= 1
                B_right[candidate_ix+1][1]-=1
                B_right.insert(candidate_ix+2,[current_char,1])
                B_right.insert(candidate_ix+3,[reversChar(current_char),1])

                B_left = copy.deepcopy(B)
                B_left[pre][1] -= 1
                B_left[candidate_ix-1][1]-=1
                B_left.insert(pre,[reversChar(current_char),1])
                B_left.insert(pre+1,[current_char,1])
                current_gap=getGap(reversChar(current_char),B)
                if(a_max_length<3 and b_max_length<3):
                    if(getGap(reversChar(current_char), B_right) <= current_gap ):
                        B = B_right
                    elif(getGap(reversChar(current_char), B_left) <= current_gap):
                        B = B_left
                    else:
                        if(B[candidate_ix+1][1]<=B[candidate_ix-1][1]):
                            B[candidate_ix-1][1]+=1
                            B[candidate_ix+1][1]-=1
                        else:
                            B[candidate_ix+1][1]+=1
                            B[candidate_ix-1][1]-=1
                else:
                    if(B[candidate_ix+1][1]<=B[candidate_ix-1][1]):
                        B=B_right
                    else:
                        B=B_left
                swap_count += 1
            elif(B[candidate_ix][1] == 2):
                # B[current][1]+=1
                if(pre is not None and next is not None):
                    if(B[candidate_ix-1][1]<B[candidate_ix+1][1]):
                        B[candidate_ix][1]+=1
                        B[pre][1]-=1
                        swap_count+=B[candidate_ix-1][1]
                    elif(B[candidate_ix-1][1]>B[candidate_ix+1][1]):
                        B[candidate_ix][1]+=1
                        B[next][1]-=1
                        swap_count+=B[candidate_ix+1][1]
                    else:
                        if(pre>0):
                            B[candidate_ix][1]+=1
                            B[pre][1]-=1
                            swap_count+=B[candidate_ix-1][1]
                        elif(next<len(B)-1):
                            B[candidate_ix][1]+=1
                            B[next][1]-=1
                            swap_count+=B[candidate_ix+1][1]
                elif(pre is None):
                    B[candidate_ix][1]+=1
                    B[next][1]-=1
                    swap_count+=B[candidate_ix+1][1]
                    pass
                elif(next is None):
                    B[candidate_ix][1]+=1
                    B[pre][1]-=1
                    swap_count+=B[candidate_ix-1][1]

            B = [x for x in B if x[1] > 0]
            B_stack = []
            for i in B:
                if(len(B_stack) == 0):
                    B_stack.append(i)
                else:
                    if(B_stack[-1][0] == i[0]):
                        B_stack[-1][1] += i[1]
                    else:
                        B_stack.append(i)
            B = B_stack

            a_max_length = max([x[1] for x in B if x[0] == "a"])
            b_max_length = max([x[1] for x in B if x[0] == "b"])

            print("B", B)

    return swap_count



def getGap(chr, B):
    C = [x[0] for x in B]
    start = C.index(chr)
    end = len(C)-1-C[::-1].index(chr)
    return sum([x[1] for x in B[start:end] if x[0] != chr])


#print(getGap("b",count_letters("bbab")))
#print(solution2("aabbbbababa"))
# print(solution2("abbbbaa"))
#print(solution2("baabaab"))
#print(solution2("ababab"))
#print(solution2("abaabaaba"))
#print(solution2("abaabaaba"))#4
#print(solution2("ababbaabba"))#2
print(solution2("bbabbaababaababb"))#1
