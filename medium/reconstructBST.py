# given the preorder traversal of a BST construct the tree

class BST:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

    
#O(n^2) time | O(h) space

# def reconstructBst(preOrderTraversal):
#     if len(preOrderTraversal)==0:
#         return
    
#     rootIdxValue=preOrderTraversal[0]

#     rightSubtreeIdx=len(preOrderTraversal)

#     for idx in  range(1,preOrderTraversal):
#         value=preOrderTraversal[idx]
#         if value >rootIdxValue:
#             rightSubtreeIdx=idx
#             break
    
#     left=reconstructBst(preOrderTraversal[1:rightSubtreeIdx])
#     right=reconstructBst(preOrderTraversal[rightSubtreeIdx:])

#     return BST(rootIdxValue,left,right)

class TreeInfo:
    def __init__(self,rootIdx) -> None:
        self.rootIdx=rootIdx

def reconstructBST(preOrderTraversal):
    treeInfo=TreeInfo(0)
    return reconstructBSTFromRange(float('-inf'),float('inf'),preOrderTraversal,treeInfo)

def reconstructBSTFromRange(lowerBound,upperBound,preOrderTraversalValues,currentSubtreeInfo):
    if currentSubtreeInfo.rootIdx==len(preOrderTraversalValues):
        return None
    rootValue=preOrderTraversalValues[currentSubtreeInfo.rootIdx]
    if rootValue< lowerBound or rootValue >=upperBound:
        return None
    currentSubtreeInfo.rootIdx+=1
    leftSubtree=reconstructBSTFromRange(lowerBound,upperBound,preOrderTraversalValues,currentSubtreeInfo)
    rightSubtree=reconstructBSTFromRange(rootValue,upperBound,preOrderTraversalValues,currentSubtreeInfo)

    return BST(rootValue,leftSubtree,rightSubtree)
















