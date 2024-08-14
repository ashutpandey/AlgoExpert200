class BinaryTree:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def splitBinaryTree(tree):
    desiredSubtreeSum=getTreeSum(tree)/2
    canBeSplit=trySubtrees(tree,desiredSubtreeSum)[1]
    return desiredSubtreeSum if canBeSplit else 0

def trySubtrees(tree,desiredSubtreeSum):
    if tree is None:
        return (0,False)
    leftSum,leftCanBeSplit=trySubtrees(tree.left,desiredSubtreeSum)
    rightSum,rightCanBeSplit=trySubtrees(tree.right,desiredSubtreeSum)
    currrentTreeSum=tree.value+leftSum+rightSum
    canBeSplit=leftCanBeSplit or rightCanBeSplit or currrentTreeSum==desiredSubtreeSum
    return (currrentTreeSum,canBeSplit)

def getTreeSum(tree):
    if tree is None:
        return 0
    
    return tree.value+getTreeSum(tree.left)+getTreeSum(tree.right)
