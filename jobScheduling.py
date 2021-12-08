startTime = [1,  2,  3,  3]
endTime =   [3,  4,  5,  6]
profit =    [50, 10, 40, 70]
jobs=list(zip(startTime,endTime,profit))
temprofit=0
jobs.sort()
def chckr(i):
    if i==len(jobs): return 0
    j=i+1
    while j<len(jobs) and jobs[i][1]>jobs[j][0]:
        j+=1
    temp1=jobs[i][2]+chckr(j)
    temp2=chckr(i+1)
    return max(temp1,temp2)
print(chckr(0))
