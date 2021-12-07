from collections import  deque

def s(ops):
    q=deque()
    sum=0
    for i in ops:
        if(i.isdigit()):
            q.append(int(i))
            sum+=int(i)
        else:
            if(i=="D"):
                q.append(2*q[-1])
                sum+=q[-1]
            if(i=="C"):
                x=q.pop()
                sum-=x
            if(i=="+"):
                q.append(q[-1]+q[-2])
                sum+=q[-1]
    return sum

print(s(["5","2","C","D","+"]))
    