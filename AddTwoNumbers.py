def addTwoNumbers(l1: [int], l2: [int]):
    i = 10**(len(l1)-1)
    j = len(l1)-1
    ex=0
    #print(j)
    temp1,temp2,temp5=0,0,0
    print(f'{l1}, {l2}')
    while j >= 0:
        print(f'{l1[j]},{l2[j]}')
        temp3=l1[j]+l2[j]+ex
        print(f'temp3== {temp3}')
        if temp3>=10:
            temp5=temp3%10
            print(f'temp5** {temp5}')
            ex=int(temp3/10)
            print(f'ex--- {ex}')
            temp3 = temp5

        temp1 = int(i * temp3)
        temp2=temp1+temp2
        j = j - 1
        i = i/10

        print(f'temp1-- {temp1}')
        print(f'temp2-- {temp2}')
    print(f'final amount {temp2}')

    #while j>=0
l1=[1,7,3]
l2=[3,5,5]

if __name__ == '__main__':addTwoNumbers(l1,l2)
