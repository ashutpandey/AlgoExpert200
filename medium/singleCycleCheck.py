def singleCycleCheck(array):
    numOfElementsVisited=0
    currentIdx=0
    while currentIdx<len(array):
        if numOfElementsVisited>0 and currentIdx==0:
            return False
        numOfElementsVisited+=1
        currentIdx=getNextIdx(currentIdx,array)
        
    return currentIdx==0

def getNextIdx(currentIdx,array):
    jump=array[currentIdx]
    nextIdx=(jump+currentIdx)%len(array)
    return nextIdx if nextIdx >=0 else (nextIdx+len(array))

