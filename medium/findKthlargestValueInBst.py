class BinaryTree:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

# def findKthLargestValueInBst(tree,k):
#     sortedNodeValues=[]

#     inOrderTraverse(tree,sortedNodeValues)
#     return sortedNodeValues[len(sortedNodeValues)-k]

# def inOrderTraverse(node,sortedNodeValues):
#     if node==None:
#         return
#     inOrderTraverse(node.left,sortedNodeValues)
#     sortedNodeValues.append(node.value)
#     inOrderTraverse(node.right,sortedNodeValues)


class TreeInfo:
    def __init__(self,numberOfNodesVisited,latestValueVisited) -> None:
        self.numberOfNodesVisited=numberOfNodesVisited
        self.latestVisitedNodeValue=latestValueVisited

def findKthLargestValueInBst(tree,k):
    treeInfo=TreeInfo(0,-1)

def reverseInOrderTraverse(node,k,treeInfo):
    if node==None or treeInfo.numberOfNodesVisited>=k:
        return
    if treeInfo.numberOfNodesVisited<k:
        treeInfo.numberOfNodesVisited+=1
        treeInfo.latestVisitedNodeValue=node.value
        reverseInOrderTraverse(node.left,k,treeInfo)