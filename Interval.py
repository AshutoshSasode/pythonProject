intervals=[[2,5],[1,6],[4,5],[2,7],[2,5],[7,8],[10,12]]
merged=[]
counter=0
intervals.sort()
for interval in intervals:
    if not merged or merged[-1][1]<interval[0]:
        merged.append(interval)
        print(f'{merged[-1][1]}..bb...{interval[0]}')
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])
        print(f'{merged[-1][1]}..aa...{interval[0]}')
        print(f'{merged[-1][1]}..cc...{interval[1]}')
    print(merged)
