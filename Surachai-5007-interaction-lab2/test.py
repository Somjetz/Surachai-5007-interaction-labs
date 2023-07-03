import math

def hypotenuse(a, b):
    try:
        return float(math.sqrt(a ** 2 + b ** 2))
    except TypeError:
        return None

output = hypotenuse(3, 4)
print(f"hypotenuse(3, 4) is {output}")
print(f"hypotenuse(3, 4) is {hypotenuse('3', '4')}")
print(f"hypotenuse(3, 4) is {hypotenuse(3, '4.0')}")