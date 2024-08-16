def getYoungestCommonAncestor(topAncestor,descendantOne,descendantTwo):
    depthOne=getDescendentDepth(descendantOne,topAncestor)
    depthTwo=getDescendentDepth(descendantTwo,topAncestor)

    if depthOne>depthTwo:
        return backtrackAncestralTree(descendantOne,descendantTwo,depthOne-depthTwo)
    else:
        return backtrackAncestralTree(descendantTwo,descendantOne,depthTwo-depthOne)
def getDescendentDepth(descendent,topAncestor):
    depth=0
    while descendent!=topAncestor:
        depth+=1
        descendent=descendent.ancestor
    return depth
def backtrackAncestralTree(lowerDescendant,higherDescendant,diff):
    while diff>0:
        lowerDescendant=lowerDescendant.ancestor
        diff-=1
    while lowerDescendant!=higherDescendant:
        lowerDescendant=lowerDescendant.ancestor
        higherDescendant=higherDescendant.ancestor
    return lowerDescendant