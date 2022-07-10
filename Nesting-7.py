from collections import deque 

def get_open(ch): 
    if(ch=="}"):
        return "{"
    elif(ch==")"):
        return "("
    elif(ch=="]"):
        return "["
    
def solution(S): 
    q=deque()
    for i in S:
        if i in "{[(":
            q.append(i)
        else:
            if(len(q)==0):
                return 0
            if(q[-1]==get_open(i)):
                q.pop()
            else:
                return 0
    
    if(len(q)!=0):
        return 0
    return 1

#print(solution("(()(())())"))
#print(solution("(()())())"))
print(solution("())"))
