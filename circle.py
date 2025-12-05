def circle_S(r):
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 3.14 * r ** 2

def circle_P(r):
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * 3.14 * r
