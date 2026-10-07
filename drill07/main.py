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


# Implement delivery_fee(order_total, distance_km, is_member). If order_total 
# is below 0 or distance_km is below 0, return Invalid input. If is_member is true 
# and order_total is at least 5000, return 0. If distance_km is less than or equal to 5, 
# return 500. If distance_km is less than or equal to 15, return 1000. Otherwise return 2000.

def delivery_fee(order_total, distance_km, is_member):
    if order_total < 0 or distance_km < 0:
        return "Invalid input"
    if is_member and order_total >= 5000:
        return 0
    if distance_km <= 5:
        return 500
    if distance_km <= 15:
        return 1000
    return 2000
    
