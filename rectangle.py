def rectangle_S(a, b):
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a * b

def rectangle_P(a, b):
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return 2 * (a + b)