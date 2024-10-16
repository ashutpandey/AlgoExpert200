#O(N) time | O(log(N)) space
def maxPathSum(tree):
    _,maxSum=findMaxSum(tree)
    return maxSum
def findMaxSum(tree):
    if tree is None:
        return (0,0)
    leftMaxSumAsBranch,leftMaxPathSum=findMaxSum(tree.left)
    rightMaxSumAsBranch,rightMaxPathSum=findMaxSum(tree.right)
    maxChildSumAsBranch=max(leftMaxSumAsBranch,rightMaxSumAsBranch)
    value=tree.value
    maxSumAsBranch=max(maxChildSumAsBranch,value+maxChildSumAsBranch)
    maxSumAsRootNode=max(leftMaxSumAsBranch+value+rightMaxSumAsBranch,maxSumAsBranch)
    maxPathSum=max(leftMaxPathSum,rightMaxPathSum,maxSumAsRootNode)
    return (maxSumAsBranch,maxPathSum)



