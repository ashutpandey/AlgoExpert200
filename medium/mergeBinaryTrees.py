# def mergeBinaryTree(tree1,tree2):
#     if tree1 is None:
#         return tree2
#     if tree2 is None:
#         return tree1
#     tree1.value+=tree2.value
#     tree1.left=mergeBinaryTree(tree1.left,tree2.right)
#     tree1.right=mergeBinaryTree(tree1.right,tree2.right)
#     return tree1


def mergeBinaryTree(tree1,tree2):
    if tree1 is None:
        return tree2
    tree1Stack=[tree1]
    tree2Stack=[tree2]

    while len(tree1Stack)>0:
        tree1Node=tree1Stack.pop()
        tree2Node=tree2Stack.pop()

        if tree2Node is None:
            continue
        tree1Node.value+=tree2Node.value
        if tree1Node.left is None:
            tree1Node.left=tree2Node.left
        else:
            tree1Stack.append(tree1Node.left)
            tree2Stack.append(tree2Node.left)
        if tree1Node.right is None:
            tree1Node.right=tree2Node.right
        else:
            tree1Stack.append(tree1Node.right)
            tree2Stack.append(tree2Node.right)
        
    return tree1
