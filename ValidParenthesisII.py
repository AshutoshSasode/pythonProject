
def minRemoveToMakeValid(s: str) -> str:
    stack=[]
    i=0
    while s:
        if s[i] =='[' and len(stack)!=0:
            if stack.pop()==']':
                i+=1
            else:
                stack.append(s[i])
                i+=1
        if s[i]==']' and len(stack)==0:
            if stack.pop()=='[':
                i+=1
            else:
                stack.append(s[i])
                i+=1
    for indexs in stack:
        temp=s.remove(indexs)
        print(temp)
    return temp

minRemoveToMakeValid("a[bc]c[de]f]g]")
