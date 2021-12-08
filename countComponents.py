n=10
edges=[[1,2],[3,7],[9,2],[4,3],[5,8],[1,6],[2,5]]
edges.sort()
visitedStack=[]
counter=0
visited=set()
for i in range(0,len(edges)):
    if i==0:
        counter += 1
        visited.add(edges[i][0])
        visited.add(edges[i][1])
    else:
        print(f'{edges[i][0]}....{edges[i][0]}')
        if edges[i][0] not in visited or edges[i][1] not in visited:
            counter+=1
        else:
            visited.add(edges[i][0])
            visited.add(edges[i][1])
    print(visited)
    #print(len(visited))

