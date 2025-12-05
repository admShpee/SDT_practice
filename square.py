def square_S(a):
    if a < 0:
        raise ValueError("Длина стороны не может быть отрицательной")
    return a * a


def square_P(a):
    if a < 0:
        raise ValueError("Длина стороны не может быть отрицательной")
    return 4 * a