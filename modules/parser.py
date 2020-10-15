#!/usr/bin/env

TOKENS = ["REEL", "OPERATEUR", "FONCTION", "ERREUR", "FIN", "PAR_OUVR", "PAR_FERM", "VARIABLE", "NO_TOKEN"]
FONCTION = ["sin", "cos", "tan", "abs", "log", "exp","sqrt","entier","val_neg","sinc"]
OPERATION = ["+","-","*","/","^"]

expression = "(3x+5)+exp(2)"

def check_fonction(string): 
    if(string in FONCTION):
        return True
    else: return False

def check_operation(string): 
    if (string in OPERATION):
        return True
    else: return False

def check_reel(string):
    check = 0
    for i in string:
        if (i =='.'):
            check+=1
        if (i.isalpha() and i !='.'):
            return False
    if (check == 1 or check == 0):
        return True

    else : return False

def parse(expression):
    expression = expression.lower()
    result = []
    temp = ""

    for i in expression:
        if(i not in OPERATION and i != '(' and i !=')' and i != 'x'):
            temp += i
            print(temp)
        elif(i=='x' and check_reel(temp)==False):
            temp += i
        else:
            if check_fonction(temp):
                result.append(("FONCTION", temp))
                temp = ""
            
            if(check_reel(temp) and temp!=""):
                result.append(("REEL",float(temp)))
                temp = ""
                
            if i in OPERATION:
                result.append(("OPERATEUR",i))
                temp=""

            if i == '(':
                result.append(("PAR_OUVR"))
                temp=""

            if i == ')':
                result.append("PAR_FERM")
                temp=""

            if (i == 'x' and temp == ""):
                result.append("VARIABLE")
                temp=""

    print(result)
    return result

parse(expression)