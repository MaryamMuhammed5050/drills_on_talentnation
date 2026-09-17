def arithmetic(a, b):
    dic = {"sum" : a+b, "product" : a * b, "power" : a**b}
    return dic

def division_details(a,b):
    dic = {"true_division" : round(a/b, 2), "floor_division" : a//b, "remainder" : a%b}
    return dic