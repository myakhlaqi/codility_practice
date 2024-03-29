from collections import Counter
import re
import copy
import sys
from typing import MappingView


def reversChar(ch):
    return "a" if ch == "b" else "b"


def count_letters(S):
    result = re.finditer(r'(a+|b+)', S)
    #print("result", result)
    B = []
    for m in result:
        B.append([m.group()[0], m.end()-m.start()])
    return B


def solution(S):
    B = count_letters(S)
    #print("B", B)
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
        current_char = "a" if a_max_length > b_max_length else "b"
        while(a_max_length < 3 or b_max_length < 3):
            gapA = getGap1("a", B)
            gapB = getGap1("b", B)
            if(a_max_length < 3 and b_max_length < 3):
                if(gapA > gapB):
                    current_char = "a"
                elif(gapB > gapA):
                    current_char = "b"
            elif(a_max_length < 3):
                current_char = "a"
            else:
                current_char = "b"
            candidate_ix = -1
            neighbor_ix = -1
            min_swap_sofar = 0
            min_total_swap = sys.maxsize
            C = [x[0] for x in B]
            ops_char_start_ix = C.index(reversChar(current_char))
            ops_char_end_ix = len(C)-1-C[::-1].index(reversChar(current_char))
            ops_char_gap = gapA if current_char == "b" else gapB
            i=0
            while(i<len(B)):
                current_neighbor_ix = -1
                if(B[i][0] == current_char):
                    if(i <= 1):
                        if(B[i][1] == 2):
                            min_swap_sofar = B[i+1][1]
                            current_neighbor_ix = i+2
                        else:
                            min_swap_sofar = sys.maxsize
                    elif(i >= len(B)-2):
                        if B[i][1] == 2:
                            min_swap_sofar = B[i-1][1]
                            current_neighbor_ix = i-2
                        else:
                            min_swap_sofar = sys.maxsize
                    else:  # if in the middle not at first and end
                        min_swap_sofar = min(
                            B[i-1][1], B[i+1][1]) if B[i][1] == 2 else (B[i-1][1]+B[i+1][1])
                        if B[i+1][1] < B[i-1][1]:
                            current_neighbor_ix = i+2
                        elif(B[i+1][1] > B[i-1][1]):
                            current_neighbor_ix = i-2
                        else:
                            if(B[i-2][1] < B[i+2][1]):  # select the based on the size
                                current_neighbor_ix = i-2
                            elif B[i-2][1] > B[i+2][1]:
                                current_neighbor_ix = i+2
                            else:  # if they are equal in size
                                if(B[i][1] == 2):  # if two aa or bb
                                    if(i+2 < len(B)-1):
                                        current_neighbor_ix = i+2
                                    else:
                                        current_neighbor_ix = i-2
                                else:  # if just one a or b
                                    if(i+2 < len(B)-1):
                                        current_neighbor_ix = i+2
                                    elif(i-2 > 0):
                                        current_neighbor_ix = i-2
                                    else:  # if both are move candidate to one side
                                        current_neighbor_ix = i
                    if(min_swap_sofar < min_total_swap):
                        candidate_ix = i
                        neighbor_ix = current_neighbor_ix
                    elif min_swap_sofar == min_total_swap and min_swap_sofar != sys.maxsize:
                        if(B[neighbor_ix][1] > B[current_neighbor_ix][1]):
                            candidate_ix = i
                            neighbor_ix = current_neighbor_ix
                        else:
                            pre_gap = getGap2(
                                current_char, B, candidate_ix, neighbor_ix, ops_char_start_ix, ops_char_end_ix, ops_char_gap)
                            cur_gap = getGap2(
                                current_char, B, i, current_neighbor_ix, ops_char_start_ix, ops_char_end_ix, ops_char_gap)
                            if(cur_gap < pre_gap):
                                candidate_ix = i
                                neighbor_ix = current_neighbor_ix
                    min_total_swap = min(min_swap_sofar, min_total_swap)
                i=max(neighbor_ix-1,candidate_ix+1,i)
                i+=1
                #print("i", i)

            #print("{} {} {}".format(candidate_ix,"<==" if candidate_ix<neighbor_ix else "= or ==>" ,neighbor_ix))

            if(B[candidate_ix][1] == 2):  # if two a : aa
                B[candidate_ix][1] += 1
                B[neighbor_ix][1] -= 1
                swap_count += B[candidate_ix+1][1] if (
                    candidate_ix < neighbor_ix) else B[candidate_ix-1][1]
            else:  # if jus one a
                if(candidate_ix == neighbor_ix):
                    B[candidate_ix-1][1] -= 1
                    B[candidate_ix+1][1] += 1
                else:
                    B[neighbor_ix][1] -= 1
                    if(candidate_ix < neighbor_ix):  # change the right side
                        B[candidate_ix+1][1] -= 1
                        B.insert(candidate_ix+2, [current_char, 1])
                        B.insert(candidate_ix+3, [reversChar(current_char), 1])
                    else:  # change the left side
                        B[candidate_ix-1][1] -= 1
                        B.insert(neighbor_ix+1, [reversChar(current_char), 1])
                        B.insert(neighbor_ix+2, [current_char, 1])
                swap_count += 1
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

            #print("B", B)

    return swap_count


def getGap1(chr, B):
    C = [x[0] for x in B]
    start = C.index(chr)
    end = len(C)-1-C[::-1].index(chr)
    return sum([x[1] for x in B[start:end] if x[0] != chr])


def getGap2(current_char, D, candidate_ix, neighbor_ix, ops_char_start_ix, ops_char_end_ix, ops_char_gap):
    D = copy.deepcopy(D)
    if(D[candidate_ix][1] == 2):  # if two a : aa
        D[candidate_ix][1] += 1
        D[neighbor_ix][1] -= 1
    else:  # if jus one a
        if(candidate_ix == neighbor_ix):
            D[candidate_ix-1][1] -= 1
            D[candidate_ix+1][1] += 1
        else:
            D[neighbor_ix][1] -= 1
            if(candidate_ix < neighbor_ix):  # change the right side
                D[candidate_ix+1][1] -= 1
                D.insert(candidate_ix+2, [current_char, 1])
                D.insert(candidate_ix+3, [reversChar(current_char), 1])

            else:  # change the left side
                D[candidate_ix-1][1] -= 1
                D.insert(neighbor_ix+1, [reversChar(current_char), 1])
                D.insert(neighbor_ix+2, [current_char, 1])
    if(not (ops_char_start_ix < candidate_ix and candidate_ix < ops_char_end_ix)
       and (ops_char_start_ix < neighbor_ix and neighbor_ix < ops_char_end_ix)):
        ops_char_gap -= 1
    elif((ops_char_start_ix < candidate_ix and candidate_ix < ops_char_end_ix, 1) and not(ops_char_start_ix < neighbor_ix and neighbor_ix < ops_char_end_ix)):
        ops_char_gap += 1
    # if(candidate_ix not in range(ops_char_start_ix+1, ops_char_end_ix, 1) and neighbor_ix in range(ops_char_start_ix+1, ops_char_end_ix, 1)):
    #     ops_char_gap -= 1
    # elif(candidate_ix in range(ops_char_start_ix+1, ops_char_end_ix, 1) and neighbor_ix not in range(ops_char_start_ix+1, ops_char_end_ix, 1)):
    #     ops_char_gap += 1

    return ops_char_gap


print(solution("aabbbbababa"),2)  # 2
print( solution("abbbbaa"),4)  # 4
print(solution("baabaab"),5)  # 5
print(solution("ababab"),3)  # 3
print(solution("abaabaaba"),4)  # 4
print(solution("abaabaaba"),4)  # 4
print(solution("ababbaabba"),2)  # 2
print(solution("bbabbaababaababb"),1)  # 1
print(solution("aabaababbbbbabaa"),1)  # 1
print(solution("abbaabba"),5)  # 5
print(solution("ababbababb"),3)  # 3
print(solution("bbabbababb"),3)  # 3
print(solution("bbabbaababaababb"),1)  # 1
print(solution("ababbababb"),3)  # 3
print(solution("aababbababbaabaa"),1)  # 1
print(solution("ababbababb"),3)  # 3
print(solution("aababaabaa"),3)  # 3
print(solution("ababbababb"),3)  # 3
