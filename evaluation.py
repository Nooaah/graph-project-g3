import constant
import numpy as np
import tree, parser

def eval(tree, x):

    #print(tree.value, tree.leftChild, tree.rightChild)
    left = None
    right = None

    if not tree.leftChild and not tree.rightChild:
        if tree.value == 'x': 
            return x
        return tree.value

    else:
        
        if tree.leftChild:
            left = eval(tree.leftChild, x)

        if tree.rightChild:
            right = eval(tree.rightChild, x)
        
        if right:
            return constant.correspondance[tree.value](float(right), float(left))

        else : 
            return constant.correspondance[f"{tree.value}"](float(left))

def calcCoordinates(t, tree):
    y = np.zeros(len(t))
    for i in range(len(t)):
        y[i] = eval(tree, i)
    return y
'''
exp = "("
exp += input() + ")"
exp = parser.toPostfix(parser.parse(exp))
#print(exp)
tree = tree.makeTree(exp)
print(eval(tree, 99.98000000010231))'''