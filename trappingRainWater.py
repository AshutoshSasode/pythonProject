elevation=[0,1,0,2,1,0,1,3,2,1,2,1]
#min(max(L),max(R))-elevation[i] >=0 ... else : ignore
maxL,maxR,minElevation,currentWater,resultWater=0,0,0,0,0
maxLlist,maxRList=[],[]
for h in range(0,len(elevation)):
    if h==0:
        maxR=max(elevation)
    else:
        maxLlist=elevation[:h]
        maxRList=elevation[(h-len(elevation)):]
        print(maxLlist)
        print(maxRList)
        maxL=max(maxLlist)
        maxR=max(maxRList)
    minElevation=min(maxL,maxR)
    currentWater=minElevation-elevation[h]
    if currentWater>=0:
        resultWater=currentWater+resultWater
print(resultWater)


