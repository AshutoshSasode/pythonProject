#s="A man, a plan, a canal: Panama"
x=-1221
if x<0:x=x*(-1)
print(x)
s=[x]
print(s)
l,r=0,len(s)-1
print(len(s))
while l<r:
    print(f'{s[l]}...{s[r]}')
    if s[l].isalnum():
        if s[r].isalnum():
            if s[l].lower()==s[r].lower():
                l+=1
                r-=1
            else:
                print("no match")
                exit(0)
        else:
            r-=1
    else:
        l+=1
print("matched")
