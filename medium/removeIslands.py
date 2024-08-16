#O(w*h) time |O(w*h) space
# def removeIslands(matrix):
#     onesConnectedToBorder=[[False for col in matrix[0]]for row in matrix]

#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             rowIsBorder=row==0 or row==len(matrix)-1
#             colIsBorder=col==0 or col==len(matrix[row])-1
#             isBorder=rowIsBorder or colIsBorder

#             if not isBorder:
#                 continue
#             if matrix[row][col]!=1:
#                 continue
#             findOnesConnectedToBorder(matrix,row,col,onesConnectedToBorder)

#     for row in range(1,len(matrix)-1):
#         for col in range(1,len(matrix[row])-1):
#             if onesConnectedToBorder[row][col]:
#                 continue

#             matrix[row][col]=0
#     return matrix
# def findOnesConnectedToBorder(matrix,startRow,startCol,onesConnectedToBorder):
#     stack=[(startRow,startCol)]

#     while len(stack)>0:
#         currentPosition=stack.pop()
#         currentRow,currentCol=currentPosition

#         alreadyVisited=onesConnectedToBorder[currentRow][currentCol]
#         if alreadyVisited:
#             continue
#         onesConnectedToBorder[currentRow][currentCol]=True

#         neighbors=getNeighbors(matrix,currentRow,currentCol)
#         for neighbor in neighbors:
#             row,col=neighbor
#             if matrix[row][col]==1:
#                 continue
#             stack.append(neighbor)

# def getNeighbors(matrix,row,col):
#     neighbors=[]
#     numRows=len(matrix)
#     numCol=len(matrix[row])

#     if row-1>=0:
#         neighbors.append((row-1,col))
#     if row+1 <numRows:
#         neighbors.append(row+1,col)
#     if col-1>=0:
#         neighbors.append((row,col-1))
#     if col+1 <numCol:
#         neighbors.append(row,col+1)
#     return neighbors



#O(w*h) time |O(w*h) space
def removeIslands(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowIsBorder=row==0 or row==len(matrix)-1
            colIsBorder=col==0 or col==len(matrix[row])-1
            isBorder=rowIsBorder or colIsBorder

            if not isBorder:
                continue
            if matrix[row][col]!=1:
                continue
            ChangeOnesConnectedToBorderToTwo(matrix,row,col)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col]==2:
                matrix[row][col]=1
            else: 
                matrix[row][col]=0
    return matrix
def ChangeOnesConnectedToBorderToTwo(matrix,startRow,startCol):
    stack=[(startRow,startCol)]

    while len(stack)>0:
        currentPosition=stack.pop()
        currentRow,currentCol=currentPosition
        matrix[currentRow][currentCol]=2

        neighbors=getNeighbors(matrix,currentRow,currentCol)
        for neighbor in neighbors:
            row,col=neighbor
            if matrix[row][col]!=1:
                continue
            stack.append(neighbor)

def getNeighbors(matrix,row,col):
    neighbors=[]
    numRows=len(matrix)
    numCol=len(matrix[row])

    if row-1>=0:
        neighbors.append((row-1,col))
    if row+1 <numRows:
        neighbors.append(row+1,col)
    if col-1>=0:
        neighbors.append((row,col-1))
    if col+1 <numCol:
        neighbors.append(row,col+1)
    return neighbors