nums = [1,3,-1,-3,5,3,6,7]
k=3
output=[]
if len(nums) < k:
    output.append(max(nums))
    print(output)
else:
    for idx in range(0, len(nums)):
        if len(nums) >= k:
            output.append(max(nums[:k]))
            nums.pop(0)
print(output)

