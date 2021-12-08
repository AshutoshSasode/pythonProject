def maximumUnits( boxTypes, truckSize):
    """
    :type boxTypes: List[List[int]]
    :type truckSize: int
    :rtype: int
    """
    load = 0
    print(f'len----- {len(boxTypes)}....trucksize {truckSize}')
    if len(boxTypes)<=truckSize:
        truckSize=len(boxTypes)
    for i in range(1, truckSize):
        if len(boxTypes[i]) > 0:
            temp = boxTypes[i][0] * boxTypes[i][1]
            load = temp + load
        else:
            temp = boxTypes[i]
            load = temp + load
    print(load)

l1=[[1,2],[5,4],[2,3],[1,1],[1,1],[1,1],[1,1]]
l2=5
if __name__ == '__main__':maximumUnits(l1,l2)
