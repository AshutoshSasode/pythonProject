s="cbbd"
lenOfString=len(s)
resLen=0
res=""
for start in range(len(s)):
    if(len(s)%2)==0:
        l,r=start,start+1
    else:
        l, r = start, start


    while l>=0 and r<len(s) and s[l]==s[r]:
        if(r-l+1)>resLen:
            res=s[l:r+1]
            resLen=r-l+1
        l-=1
        r+=1

print(res)