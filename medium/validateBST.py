def validateBst(tree):
    return validateBstHelper(tree,float('-inf'),float('inf'))
def validateBstHelper(tree,minValue,maxValue):
    if tree is None:
        return True
    if tree.value<minValue or tree.value>=maxValue:
        return False
    return validateBstHelper(tree.left,minValue,tree.value) and validateBstHelper(tree.right,tree.value,maxValue)