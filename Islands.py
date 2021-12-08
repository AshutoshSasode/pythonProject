grid=[["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]]
counter=0
result=0
row,col=len(grid),len(grid[0])
def usingBfs(grid,r,c,row,col):
    if r<0 or c<0 or r>=row or c>=col or grid[r][c] =='0':
        return
    grid[r][c]='0'
    usingBfs(grid,r+1,c,row,col)
    usingBfs(grid,r-1,c,row,col)
    usingBfs(grid,r,c+1,row,col)
    usingBfs(grid,r,c-1,row,col)

for i in range(0,row):
    for j in range(0,col):
        if grid[i][j]=='1':
            counter += 1
            usingBfs(grid,i,j,row,col)
        #print(f'{i}..{j}..{counter}')
print(counter)

