#O(n) time | #O(n) space

def reversePolishNotation(tokens):
    stack=[]
    for token in tokens:
        if token=='+':
            stack.append(stack.pop()+stack.pop())
        elif token=='-':
            firstNumber=stack.pop()
            stack.append(stack.pop()-firstNumber)
        elif token=='*':
            stack.append(stack.pop()*stack.pop())
        elif token=='/':
            firstNumber=stack.pop()
            stack.append(stack.pop()/firstNumber)
        else:
            stack.append(int(token))
    return stack.pop()