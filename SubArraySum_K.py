
nums=[1,1,1]
k=2
#nums.sort()
print(nums)
counter,sum = 0,0
for num in range(len(nums)):
    sum = sum + nums[num]
    print(sum)
    if sum == k:
        counter = counter + 1
        sum=0
        sum=nums[num]
    if nums[num]==k:
        counter=counter+1
        sum=0
    print(f'counter..{counter}')