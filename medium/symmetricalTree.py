# def symmetricalTree(tree):
#     stackLeft=[tree.left]
#     stackRight=[tree.right]

#     while len(stackLeft)>0:
#         left=stackLeft.pop()
#         right=stackRight.pop()
#         if left is None and right is None:
#             continue
#         if left is None or right is None or left.value!=right.value:
#             return False
        
#         stackLeft.append(left.left)
#         stackLeft.append(left.right)
#         stackRight.append(right.right)
#         stackRight.append(right.left)
#     return True

def symmetricalTree(tree):
    return treesAreMirrored(tree.left,tree.right)
def treesAreMirrored(left,right):
    if left is not None and right is not None and left.value==right.value:
        return treesAreMirrored(left.left,right.right) and treesAreMirrored(left.right,right.left)
    return left==right