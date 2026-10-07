# Implement age_category(age). Return Child if age is less than 13,
# Teenager if age is less than 18, Adult if age is less than 65, and Senior otherwise.
# Use if, elif, and else.

def age_category(age):
    if age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"


# Implement vote_eligibility(age, country). 
# Return Eligible if age is at least 18 and country is Nigeria. Otherwise return Not eligible. 
# The country check should be case-insensitive 
# and should ignore leading and trailing spaces.

def vote_eligibility(age, country):
    if age >= 18 and country.strip().lower() == "nigeria":
        return "Eligible"
    else:
        return "Not eligible"


# Implement password_strength(password). Return Weak if the password has fewer than 8 characters.
# Return Medium if it has at least 8 characters but does not contain both letters and digits. 
# Return Strong if it has at least 8 characters and 
# contains at least one letter and at least one digit. Students may need to research isalpha and isdigit.

def password_strength(password):
    if len(password) < 8:
        return "Weak"
    
    # This Checks if the password contains at least one letter and at least one digit
    letter = any(char.isalpha() for char in password)
    digit = any(char.isdigit() for char in password)
    
    if letter and digit:
        return "Strong"
    else:
        return "Medium"


# Implement access_gate(age, has_id, is_banned).
# Use guard-clause style. Return Too young if age is less than 18. Return No ID if has_id is false. 
# Return Banned if is_banned is true. Return Allowed only if all checks pass.

def access_gate(age, has_id, is_banned):
    if age < 18:
        return "Too young"
    if has_id == False:
        return "No ID"
    if is_banned == True:
        return "Banned"
    else:
        return "Allowed"

# To use guard-clause, else cannot be used so the better way to check the conditions is

def access_gate(age, has_id, is_banned):
    if age < 18:
        return "Too young"
    if not has_id:
        return "No ID"
    if is_banned:
        return "Banned"
    return "Allowed"