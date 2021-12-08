inputNum=445
multiply=1
SumOfNum=0
diffOfNum=0
inputNumStr=str(inputNum)
for c in range(0,len(inputNumStr)):
    multiply=multiply*int((inputNumStr[c]))
    SumOfNum=SumOfNum+int((inputNumStr[c]))
print(multiply-SumOfNum)
