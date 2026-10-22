# Implement count_up(n). Return a list of numbers from 1 to n inclusive. 
# If n is less than 1,
#  return an empty list. Use a loop and range

def count_up(n):
    num = []
    if n < 1:
        return num
    for n in range(1, n+1):
        num.append(n)
    return num 


# Implement sum_multiples(limit, divisor). Return the sum of all positive numbers 
# from 1 to limit inclusive that are divisible by divisor. 
# If divisor is zero, return Invalid divisor. Do not use the built-in sum function.
def sum_multiples(limit, divisor):
    if divisor == 0:
        return "Invalid divisor"
    total = 0
    for number in range(1, limit + 1):
        if number % divisor == 0:
        total = total + number
    return total


 