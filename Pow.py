def mainfunc(base:float,expo:float)->float:
    print(pow(base,expo))
    result = calc(abs(expo), base)
    print (result if expo>0 else 1/result)
    print ((result*base)  if expo >0 & expo%2==0 else (1/(result*base)))
    if base==0:return 0
    if expo==0:return 1
def calc(expo,base):
    result=float(1.0)
    halfexpo = abs(expo) // 2
    while halfexpo-1>= 0:
        result = result * base
        halfexpo = halfexpo - 1
    return(result*result) if abs(expo)%2==0 else (result*result*base)

if __name__ == '__main__':mainfunc(8,-4)






