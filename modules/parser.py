#!/usr/bin/env

from constant import FONCTION, OPERATION, PRECEDENCE

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
    expression = expression.replace(" ","")
    expression = expression.lower()
    result = []
    temp = ""

    for i in expression:
        if(i not in OPERATION and i != '(' and i !=')' and i != 'x'):
            temp += i
        elif(i=='x' and check_reel(temp)==False):
            temp += i
        else:
            if check_fonction(temp):
                result.append(temp)
                temp = ""
            
            if(check_reel(temp) and temp!=""):
                result.append(temp)
                temp = ""
                
            if i in OPERATION:
                result.append(i)
                temp=""

            if i == '(':
                result.append("(")
                temp=""

            if i == ')':
                result.append(")")
                temp=""

            if (i == 'x' and temp == ""):
                result.append("x")
                temp=""

    if(check_reel(temp) and temp!=""):
        result.append(temp)
    #print(result)
    return result

def toPostfix(expression):
    output = []
    operator = []
    for x in expression:
        if x == '(':
            operator.append(x)
        elif x == ')':
            while operator[-1]!='(':
                output.append(operator.pop())
            operator.pop()

        elif x not in OPERATION and x not in FONCTION : 
            output.append(x)
        elif x in OPERATION or x in FONCTION:
            if not operator or PRECEDENCE[x] > PRECEDENCE[operator[-1]] :
                operator.append(x)
            else : 
                while PRECEDENCE[operator[-1]] >= PRECEDENCE[x] and operator[-1] != '(' and operator[-1] != ')':
                    output.append(operator.pop())
                operator.append(x)

        #print(f'Output {output}')
        #print(f'Operator {operator}')
    while operator :
        output.append(operator.pop())
    return output