def triangle_S(a, h):
    if a < 0 or h < 0:
        raise ValueError("Основание и высота не могут быть отрицательными")
    return 0.5 * a * h

def triangle_P(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    elif (a + b) <= c or (a + c) <= b or (b + c) <= a:
        raise ValueError("Несоответствие неравенству треугольника")
    return a + b + c