import numpy as np

FONCTION = ["sin", "cos", "tan", "abs", "log", "exp","sqrt","entier","val_neg","sinc"]
OPERATION = ["+","-","*","/","^"]
PRECEDENCE = {
    "+":1,
    "-":1,
    "*":2,
    "/":2,
    "^":3,
    "(":4,
}

correspondance = {

    "+" : np.add,
    "-" : np.subtract,
    "*" : np.multiply,
    "/" : np.divide,  
    "^" : np.power,
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "abs": np.abs,
    "log": np.log,
    "exp": np.exp,
    "sqrt": np.sqrt,
    "entier" : int,
    "val_neg": lambda a : -a,
    "sinc" : np.arcsin

}
for x in FONCTION : 
    PRECEDENCE.update({x:3})