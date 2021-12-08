list1=[1,2]
list2=[3,4]
list3=list1+list2
print(list3)
list3.sort()
numLen=len(list3)
if numLen%2==0:
    temp=numLen//2
    median=float((list3[temp-1]+list3[temp])/2)
    print(median)
else:
    temp=(numLen)//2
    print(temp)
    median=float(list3[temp])
    print(median)