x=-123
sign =0
if x<0:
    x=x*(-1)
    sign=-1
numlen=str(x)

temp1,temp2=0,0
for i in range (1,len(numlen)+1):
    temp=x%(10)
    x=x//(10)
    temp1=temp*(10**(len(numlen)-i))
    temp2=temp1+temp2
if temp2.bit_length()<32:
    if sign ==-1:
        print(temp2*(-1))
    else:
        print(temp2)
else:
    print(0)
#print(temp)