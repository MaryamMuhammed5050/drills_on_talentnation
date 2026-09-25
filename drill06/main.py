def receipt_formatter(name, quantity, price):
    customer = name
    quantity = float(quantity)
    price = float(price)
    subtotal = float(quantity * price)
    # subtotal = float(subtotal)
    tax = subtotal * 0.075 
    total = subtotal + tax
    
    f_sub = round(subtotal,2)
    f_tax = round(tax,2)
    f_tot = round(total,2)
    
    return f"Customer: {customer}\nSubtotal: {f_sub}\nTax: {f_tax}\nTotal: {f_tot}"



    def smart_temperature(value):
    try:
        celsius = float(value)
    except ValueError:
        return "Invalid temperature"
    fahrenheit = (celsius * 1.8) + 32
    if celsius <= 0:
        status = "freezing"
    elif celsius < 20:
        status = "cold"
    elif celsius <= 30:
        status = "warm"
    else:
        status = "hot"
    line1 = f"Celsius: {celsius}"
    line2 = f"Fahrenheit: {fahrenheit}"
    line3 = f"Status: {status}"
    return f"{line1}\n{line2}\n{line3}"


    def slug_maker(title):
    slug = title.strip()
    slug = slug.lower()
    slug = slug.replace(",", "")
    slug = slug.replace(".", "")
    slug = slug.replace(" ", "-")
    return slug

    

def manual_palindrome(text):
    cleaned = text.lower()
    cleaned = cleaned.replace(" ", "")
    backward = ""

    for letter in cleaned:
        backward = letter + backward
    if cleaned == backward:
        return True
    else:
        return False

     
    



