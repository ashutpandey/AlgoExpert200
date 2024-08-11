def inOrderTraversal(tree,array):
    if tree is not None:
        inOrderTraversal(tree.left,array)
        array.apppend(tree.value)
        inOrderTraversal(tree.right,array)
    return array

def preOrderTraverse(tree,array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left,array)
        preOrderTraverse(tree.right,array)

    return array

def postOrderTraverse(tree,array):
    if tree is not None:
        postOrderTraverse(tree.left,array)
        postOrderTraverse(tree.right,array)
        array.append(tree.value)
    return array


