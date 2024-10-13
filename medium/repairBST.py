# def repiarBst(tree):
#     nodeOne,nodeTwo,previousNode=None

#     def inorderTraversal(node):
#         nonlocal nodeOne,nodeTwo,previousNode
#         if node is None:
#             return
#         inorderTraversal(node.left)
#         if previousNode is not None and previousNode.value>node.value:
#             if nodeOne is None:
#                 nodeOne=previousNode
#             nodeTwo=node
#         previousNode=node
#         inorderTraversal(node.right)

#     inorderTraversal(tree)
#     nodeOne.value,nodeTwo.value=nodeTwo.value,nodeOne.value
#     return tree


def repairBst(tree):
    nodeOne,nodeTwo,previousNode=None
    stack=[]
    currentNode=tree
    while currentNode is not None or len(stack)>0:
        while currentNode is not None:
            stack.append(currentNode)
            currentNode=currentNode.left
        currentNode=stack.pop()
        if previousNode is not None and previousNode.value>currentNode.value:
            if nodeOne is None:
                nodeOne=previousNode
            nodeTwo=currentNode
        previousNode=currentNode
        currentNode=currentNode.right
    nodeOne.value,nodeTwo.value=nodeTwo.value,nodeOne.value
    return tree




