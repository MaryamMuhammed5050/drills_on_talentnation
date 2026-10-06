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



