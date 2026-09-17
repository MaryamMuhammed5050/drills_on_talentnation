def arithmetic(a, b):
    dic = {"sum" : a+b, "product" : a * b, "power" : a**b}
    return dic

def division_details(a,b):
    dic = {"true_division" : round(a/b, 2), "floor_division" : a//b, "remainder" : a%b}
    return dic

def eligibility_logic(score,attendance,completed_drill):
    if score >= 70 and attendance >= 80 and completed_drill == True :
        return "Eligible"
    
    else:
        return "Not eligible"


def safe_calculator(a, operator, b):
    if operator not in ["+", "-", "*", "/","%","**"]:
        return "Invalid operator"
    if operator in ["/", "%"] and b == 0:
        return "Cannot divide by zero"

    if operator == "+":
        return a+b
    
    if operator == "-":
        return a-b
    
    if operator == "/":
        return a/b
    
    if operator == "*":
        return a*b
    
    if operator == "%":
        return a%b
    
    if operator == "**":
        return a**b