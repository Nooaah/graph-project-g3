import constant
import numpy as np

def eval(tree, x):

    print(tree.value, tree.leftChild, tree.rightChild)
    left = None
    right = None

    if not tree.leftChild and not tree.rightChild:
        if tree.value == 'x': 
            tree.value = x
        return tree.value

    else:
        
        if tree.leftChild:
            left = eval(tree.leftChild, x)

        if tree.rightChild:
            right = eval(tree.rightChild, x)
        
        if right:
            return constant.correspondance[tree.value](float(left), float(right))

        else : 
            return constant.correspondance[f"{tree.value}"](float(left))

def calcCoordinates(t, tree):
    y = np.zeros(len(t))
    for i in range(len(t)):
        y[i] = eval(tree, i)
    return y