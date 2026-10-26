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


# Implement collect_until_stop(items). Loop through the list and collect items until an item becomes
# stop after stripping spaces and converting to lowercase. Return the collected items before stop.
# Use break when stop is found.

def collect_until_stop(items):
    container = []

    for item in items:
        if item.strip().lower() == "stop":
            break
        container.append(item)

    return container


# Implement skip_evens(start, end). Return a list of odd numbers from start to end inclusive.
# Use continue to skip even numbers. If start is greater than end, return an empty list.
 
 
def skip_evens(start, end):
    odd_numbers = []

    if start > end:
        return odd_numbers

    for number in range(start, end + 1):
        if number % 2 == 0:
            continue
        odd_numbers.append(number)

    return odd_numbers


# Implement triangle_pattern(n). Return a string containing a left-aligned triangle of asterisks with n rows.
#  Row 1 has one asterisk, row 2 has two asterisks, 
# and so on. Lines should be separated by newline characters. If n is less than 1, return an empty string.


def triangle_pattern(n):
    if n < 1:
        return ""

    pattern = []

    for row in range(1, n + 1):
        pattern.append("*" * row)

    return "\n".join(pattern)




def count_even():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

result = count_even()
print(result)

def count_odd():
    number = [1,2,3,4,5,6,7,8,9,11]
    count = 0
    for numbers in number:
        if numbers % 2:
            count += 1
    return count

total = count_odd()
print(total)