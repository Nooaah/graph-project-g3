from enum import Enum
import math 
import copy

class node:
    
    def __init__(self,typejeton, LeftChild, RightChild):
        self.typejeton = typejeton
        self.LeftChild = LeftChild
        self.RightChild = RightChild



class typevaleur :

    def __init__(self, reel, fonction, operateur, erreur):
        self.reel = reel
        self.fonction = fonction
        self.operateur = operateur
        self.erreur = erreur


class typejeton :

    def __init__(self, lexem, valeur):
        self.lexem = lexem
        self.valeur = valeur


#Ex 1 : sin(2 + x) --> fonctionne
valeur1 = typevaleur(None, 'SIN', None, None)
valeur2 = typevaleur(None, None , 'PLUS', None)
valeur3 = typevaleur(2 , None, None, None)
valeur4 = typevaleur('x', None, None, None)

lexem1 = 'FONCTION'
lexem2 = 'OPERATEUR'
lexem3 = 'VARIABLE'
lexem4 = 'REEL'

jeton1 = typejeton(lexem1, valeur1)
jeton2 = typejeton(lexem2, valeur2)
jeton3 = typejeton(lexem3, valeur4)
jeton4 = typejeton(lexem4, valeur3)

x = node(jeton3, None, None)
deux = node(jeton4, None, None)
plus =node(jeton2, x , deux)
racine = node(jeton1, None , plus)

#Ex 2 : 1/x

valeur5 = typevaleur(None, None , 'DIV', None)
valeur7 = typevaleur(1 , None, None, None)
valeur6 = typevaleur('x', None, None, None)

lexem5 = 'OPERATEUR'
lexem6 = 'VARIABLE'
lexem7 = 'REEL'

jeton5 = typejeton(lexem5, valeur5)
jeton6 = typejeton(lexem6, valeur6)
jeton7 = typejeton(lexem7, valeur7)

un = node(jeton7, None, None)
x2 = node(jeton6, None, None)
racine2 = node(jeton5, un ,x2)


def remplacer(node, i) :

    if(node.LeftChild != None) :
        node.LeftChild = remplacer(node.LeftChild,i)
        
    if(node.typejeton.lexem == 'VARIABLE') :
        node.typejeton.lexem = 'REEL'
        node.typejeton.valeur.reel = i

    if(node.RightChild != None) :
        node.RightChild = remplacer(node.RightChild,i)

    return node
    
def calcul(node) : 

    x = 0
    y = 0
    z = 0

    if(node.LeftChild != None ) :
        y = calcul(node.LeftChild)
        
    if(node.RightChild != None) :
        z = calcul (node.RightChild)

    if(y == 'Pas de valeur' or z == 'Pas de valeur') :
        return 'Pas de valeur'


    if(node.typejeton.lexem == 'REEL') : 
        x = node.typejeton.valeur.reel
        
    elif(node.typejeton.lexem == 'OPERATEUR') :
            
        if(node.typejeton.valeur.operateur == 'PLUS') :
            x = y + z
        elif(node.typejeton.valeur.operateur == 'MOINS') :
            x = y - z
        elif(node.typejeton.valeur.operateur == 'FOIS') :
            x = y * z
        elif(node.typejeton.valeur.operateur == 'DIV' and z != 0) :
            x = y/z
        elif(node.typejeton.valeur.operateur == 'PUIS') :
            x = y ** z
        else :
            return 'Pas de valeur'
        
    elif(node.typejeton.lexem == 'FONCTION') :

        if(node.typejeton.valeur.fonction == 'SIN') : 
            x = math.sin(z)
        elif(node.typejeton.valeur.fonction == 'COS') :
            x = math.cos(z)
        elif(node.typejeton.valeur.fonction == 'TAN') :
            x = math.tan(z)
        elif(node.typejeton.valeur.fonction == 'ABS') :
            x = math.fabs(z)
        elif(node.typejeton.valeur.fonction == 'SQRT' and z >= 0) :
            x = math.sqrt(z)
        elif(node.typejeton.valeur.fonction == 'LOG'and z >0) :
            x = math.log10(z)
        elif(node.typejeton.valeur.fonction == 'EXP') :
            x = math.exp(z)
        elif(node.typejeton.valeur.fonction == 'ENTIER') :
            x = int(z)
        elif(node.typejeton.valeur.fonction == 'VAL_NEG') :
            x = 0 - z
        elif(node.typejeton.valeur.fonction == 'SINC') :
            if(z==0) :
                x = 1
            else : 
                x = math.sin(z)/z
        else :
            return 'Pas de valeur'

    else :
        return 'Pas de valeur'
   
    return x


def Evaluateur2 (node, borneinf, bornesup) : #ajout d'un paramètre possible pour écart entre valeurs calculés

    if(borneinf > bornesup) :
       sw = bornesup
       bornesup = borneinf
       borneinf = sw

    i = borneinf
    #modifier 1 par variable passer en paramètre pour déterminer écart de valeur souhaité (ex : toutes les valeurs de 0 à 5 avec 0.5 donne donc f(x) avec
    # x = [0, 0.5, 1, 1.5, 2, 2.5, ..., 5])
    y = 1
    x = []
    fx=[]
        
    while (i <= bornesup) :

        node2 = copy.deepcopy(node)
        remplacer(node2, i)
        resi = 0
        resi = calcul(node2)
        x.append(i)
        fx.append(resi)
        i = i + y

    res = [x,fx]
    return res

ab = Evaluateur2(racine, 0, 5)
print(ab)
