def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print ("Let's do some math with functions.")

age = add(20,8)
height = subtract(80,6)
weight = multiply(39,2)
iq = divide(500,5)

print(f"""Age: {age}, \nHeight: {height}, \nWeight: {weight}, \nIQ: {iq}.""")

# A puzzle for extra credit.
print("Here's a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print(f"That becomes: {what}. Can you do it in your head?")
