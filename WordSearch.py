board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
ToSearch = "ABCCED"
row,col=len(board),len(board[0])
path=set()

def checkDFS(i,r,c):
    if r<0 or c<0 or r>=row or c>=col or board[r][c]!=ToSearch[i] or (r,c) in path:
        return False
    if i==len(ToSearch):
        return True
    path.add((r,c))
    res=(checkDFS(i+1, r + 1, c) or
    checkDFS(i+1, r - 1, c) or
    checkDFS(i+1, r, c + 1) or
    checkDFS(i+1, r, c - 1) )
    path.remove((r,c))
    return res
    for r in range(row):
        for c in range(col):
            if checkDFS(0,r,c): return True
    return False


