# Hypothesis class is a set of rectangles
# We have access to 2 attributes of car like the power and price

def isFamilyCar(power, price):
    if (100 < power < 200) and (10000 < price < 20000):  # This line is the discriminant
        return True
    return False
