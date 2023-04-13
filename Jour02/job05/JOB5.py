def calcul(num1,operator,num2):
    if operator == "*":
        return num1*num2
    elif operator == "+":
        return num1+num2
    elif operator == "/":
        return num1/num2
    elif operator == "%":
        return num1%num2
    elif operator == "-":
        return num1-num2
    else: 
        return "Pas d'opération"
    
print(calcul(70,"*",10))

