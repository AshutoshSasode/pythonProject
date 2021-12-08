k=[]
a='1010101'
b='10101110'
print(a)
print(b)
c=0
temp=0

if(len(a)<=len(b)):
    c=len(a)
    #print(c)
else:
    c=len(b)
    #print(c)

for d in range(c-1,0,-1):
    print(d)
    if d>len(a)-1:
        t1=0

    else:
        t1=int(a[d])
    if d>len(b)-1:
        t2=0
    else:
        t2=int(b[d])
    temp=int(t1+t2)

    if (temp==2):
        #k[d]=10
        k.append(10)
    else:
        #k[d]=temp
        k.append(temp)
        #print(k[d])
k.reverse()
print(k)
