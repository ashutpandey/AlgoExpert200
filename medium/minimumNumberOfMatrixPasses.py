def minimumPassesOfMatrix(matrix):
    passes=convertNegatives(matrix)
    return passes-1 if not containsNegative(matrix) else -1

def convertNegatives(matrix):
    queue=getAllPositivePositions(matrix)
    passes=0

    while len(queue)>0:
        currentSize=queue
        

        while currentSize>0:
            currentRow,currentCol=queue.pop(0)

            adjacentPositions=getAdjacentPositions(currentRow,currentCol,matrix)

            for position in adjacentPositions:
                row,col=position
                value=matrix[row][col]
                if value<0:
                    matrix[row][col]*=-1
                    queue.append([row,col])
            
            currentSize-=1
        passes+=1
    return passes

def getAllPositivePositions(matrix):
    positivePositions=[]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col]>0:
                positivePositions.append([row,col])
    return positivePositions

def getAdjacentPositions(row,col,matrix):
    adjacentPostions=[]
    if row>0:
        adjacentPostions.append([row-1,col])
    if row<len(matrix)-1:
        adjacentPostions.append([row+1,col])
    if col>0:
        adjacentPostions.append([row,col-1])
    if col<len(matrix[0])-1:
        adjacentPostions.append([row,col+1])
    return adjacentPostions


def containsNegative(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]<0:
                return True
    return False