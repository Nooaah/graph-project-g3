from constant import FONCTION, OPERATION

class Node:
    def __init__(self, value, leftChild=None, rightChild=None):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild

def makeTree(postfixExpression):
    stack = []

    for x in postfixExpression:
        if x in FONCTION: 
            stack.append(Node(x, stack.pop()))
        elif x in OPERATION:
            left = stack.pop()
            right = stack.pop()
            stack.append(Node(x, left, right))
        else:
            stack.append(Node(x))
            
    return stack.pop()