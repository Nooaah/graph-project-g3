from constant import correspondance

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
            return correspondance[tree.value](float(left), float(right))

        else : 
            return correspondance[f"{tree.value}"](float(left))
'''
expression = "(3*x+5)+exp(2)"

par = parser.parse(expression)
print(par)
pst = parser.toPostfix(par)
print(pst)
tree = tree.makeTree(parser.toPostfix(parser.parse(expression)))
print(eval(tree, 2))
'''