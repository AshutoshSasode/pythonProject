def mainfunc(base:float,expo:float)->float:
    if base==0:return 0
    if expo==0:return 1
    if expo<0:
        base=1/base
        expo=expo*-1
    result=1.0
    halfexpo=expo//2
    while halfexpo:
        result=result*base
        halfexpo=halfexpo-1
    print(result*result if expo%2==0 else result*base*result)
    return result*result if expo%2==0 else result*result*base

if __name__ == '__main__':mainfunc(2,-4)






