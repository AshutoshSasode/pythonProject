timeList=[[0,30],[5,10],[15,20]]
starts=[]
ends=[]
counter,result,s,e=0,0,0,0
for i in range(0,len(timeList)):
    starts.append(timeList[i][0])
    ends.append(timeList[i][1])

while s<len(timeList):
    if starts[s]<ends[e]:
        print(f'{starts[s]}...{ends[e]}')
        s+=1
        counter+=1
    else:
        print(f'{starts[s]}...{ends[e]}')
        e+=1
        counter-=1
    result=max(result,counter)
print(result)
