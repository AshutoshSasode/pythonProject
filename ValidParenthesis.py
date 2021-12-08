s = '{()}[]()'
print(s)
closeToOpen={")":"(","}":"{","]":"["}
stack=[]
for bracket in s:
    if bracket in closeToOpen:
        if stack and stack[-1]==closeToOpen[bracket]:
            stack.pop()
        else:
            print("Flase")
    else:
        stack.append(bracket)
print("finally") if not stack else print("nope")

