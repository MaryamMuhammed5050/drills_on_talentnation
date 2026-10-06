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
    
    # Check if the password contains at least one letter and at least one digit
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    
    if has_letter and has_digit:
        return "Strong"
    else:
        return "Medium"
