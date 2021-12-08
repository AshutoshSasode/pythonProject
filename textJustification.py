words = ["This", "is", "an", "example", "of", "text", "justification."]
k=16
lst=[]
result=[]
counter=0
for w in words:
    while len(w)+counter+len(lst)>k:
        gaps=(len(lst)-1) or 1
        q,r=divmod(k-counter,gaps)
        for i in range(gaps):
            lst[i]+=" "*q+(" " if i<r else"")
        result.append("".join(lst))
        counter,lst=0,[]
    lst.append(w)
    counter+=len(w)
print(result+[" ".join(lst).ljust(k)] if lst else [])
