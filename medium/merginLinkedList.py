#O(m+n) time | O(1) space
def mergingLinkedList(linkedListOne,linkedListTwo):
    listOneNodes=set()
    currentNodeOne=linkedListOne
    while currentNodeOne is not None:
        listOneNodes.add(currentNodeOne)
        currentNodeOne=currentNodeOne.next
    currentNodeTwo=linkedListTwo
    while currentNodeTwo is not None:
        if currentNodeTwo in listOneNodes:
            return currentNodeTwo
        currentNodeTwo=currentNodeTwo.next
    return None

def mergingLinkedLists(linkedListOne,linkedListTwo):
    currentNodeOne=linkedListOne
    countOne=0
    while currentNodeOne is not None:
        countOne+=1
        currentNodeOne=currentNodeOne.next
    currentNodeTwo=linkedListTwo
    countTwo=0
    while currentNodeTwo is not None:
        countTwo+=1
        currentNodeTwo=currentNodeTwo.next
    diff =abs(countOne-countTwo)
    biggerCurrentNode= linkedListOne if countOne >countTwo else linkedListTwo
    smallerCurrentNode=linkedListTwo if countOne>countTwo else linkedListOne


    for _ in range(diff):
        biggerCurrentNode=biggerCurrentNode.next
    while biggerCurrentNode is not smallerCurrentNode:
        biggerCurrentNode=biggerCurrentNode.next
        smallerCurrentNode=smallerCurrentNode.next
    return biggerCurrentNode



def mergeLinkedLists(linkedListOne,linkedListTwo):
    currentNodeOne=linkedListOne
    currentNodeTwo=linkedListTwo
    while currentNodeOne is not currentNodeTwo:
        if not currentNodeOne:
            

