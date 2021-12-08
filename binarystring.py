def binarystring(s: str):# -> int:          #11001100
    print(s)
    s2=[]
    c1, c2,j = 0, 0,0
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i]=='1':
                c1=c1+1
            if s[i]=='0':
                c2=c2+1
            if c1==c2:
                #a=(c1+c2-j)
                s2.append(s[len(s2):i+1])
                c1,c2=0,0
            print(f'....{c1}...{c2}..{i}....{i-c1+1}')
        print(f'your final string.. {s2}')

if __name__ == '__main__':binarystring('11001100')

