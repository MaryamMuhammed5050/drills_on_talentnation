def fix_greeting(name):
    greeting = "Hello, " + name + "."
    return greeting

    new = fix_greeting("Ada")
    return new


def next-age(next_age):
        age = int(next_age)
        age = age + 1
        return age

def safe-divide(a, b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            return round(a/b, 2)


def get_item(items, index):
    if index < 0 or index >= len(items):
        return "Index out of range"
    else:
        return items[index]

def grade_label(score):
    # Bug to fix: branch order and boundary checks must be correct.
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
   
    else:
        return "F"