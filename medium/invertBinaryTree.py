# def invertBinaryTree(tree):
#     queue=[tree]

#     while len(queue):
#         current=queue.pop(0)
#         if current is None:
#             continue
        
#         swapLeftAndRight(current)

#         queue.append(current.left,current.right)

# def swapLeftAndRight(tree):
#     tree.left,tree.right=tree.right,tree.left


def invertBinaryTree(tree):
    if tree is None:
        return
    swapLeftAndRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

def swapLeftAndRight(tree):
    tree.left,tree.right=tree.right,tree.left



