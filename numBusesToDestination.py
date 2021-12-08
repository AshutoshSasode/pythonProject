busStops=[[3,4],[5,6,7],[1,2,3,4,9],[11,10,9]]
source,destination=3,9
g=graph

def checkdfs(i,busStops,source,destination):
    for idx,busstop in enumerate(busStops[i]):
        if busstop!=source:







if destination not in busStops:
    print("-1")
for i in range(0,len(busStops)):
    if source in busStops[i] and destination in busStops[i]:
        print(f"1     {busStops[i]}")
    elif source in busStops[i] and destination not in busStops[i]:

        checkdfs(i,busStops,source,destination)
