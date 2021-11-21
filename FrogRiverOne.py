# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    path={}
    print("path", path)
    counter=0
    for i,x in enumerate(A):
        if x in path:
            path[x]=min(path[x],i)  
        else:
            path[x]=i
            counter+=1
        print("path", path)        
        if(counter==X):
            break
    if(counter==X):
        result=max(path,key=path.get)
        return path[result]
    else:
        return -1
    
print(solution(5,[1,1,1,4,2,1,5,3,4]))