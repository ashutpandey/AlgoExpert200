def sumBsts(tree):
    return getTreeInfo(tree).totalSumBstNodes
def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(
            True,
            float('-inf'),
            float('inf'),
            0,
            0,
            0
        )
    leftTreeInfo=getTreeInfo(tree.left)
    rightTreeInfo=getTreeInfo(tree.right)
    satisfiesBstProp=tree.value>leftTreeInfo.maxValue and tree.value <=rightTreeInfo.minValue
    isBst=satisfiesBstProp and leftTreeInfo.isBst and rightTreeInfo.isBst
    maxValue=max(tree.value,max(leftTreeInfo.maxValue,rightTreeInfo.maxValue))
    minValue=min(tree.value,min(leftTreeInfo.minValue,rightTreeInfo.minValue))
    bstSum=0
    bstSize=0
    totalSumBstNodes=leftTreeInfo.totalSumBstNodes+rightTreeInfo.totalSumBstNodes
    if isBst:
        bstSum=tree.value+leftTreeInfo.bstSum+rightTreeInfo.bstSum
        bstSize=1+leftTreeInfo.bstSize+rightTreeInfo.bstSize
        if bstSize>=3:
            totalSumBstNodes=bstSum
    return TreeInfo(
        isBst,
        maxValue,
        minValue,
        bstSum,
        bstSize,
        totalSumBstNodes
    )

class TreeInfo:
    def __init__(self,isBst,maxValue,minValue,bstSum,bstSize,totalSumBstNodes):
        self.isBst=isBst
        self.maxValue=maxValue
        self.minValue=minValue
        self.bstSum=bstSum
        self.bstSize=bstSize
        self.totalSumBstNodes=totalSumBstNodes

