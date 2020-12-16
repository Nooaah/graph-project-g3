from constant import FONCTION, OPERATION
import parser


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


def inOrder(tree):
    if tree.leftChild:
        inOrder(tree.leftChild)
    if tree.rightChild:
        inOrder(tree.rightChild)
    print(tree.value)

'''
exp = "("
exp += input() + ")"
exp = parser.toPostfix(parser.parse(exp))
tree = makeTree(exp)
inOrder(tree)
'''