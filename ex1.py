def square(x):
    return x ** 2


def factorial(x):
    result = 1
    while x > 0:
        result *= x
        x -= 1
    return result


def quadratic_function(a, b, c):
    delta = b ** 2 * 4 * (a * c)
    if delta > 0:
        x1 = (-b - delta * 1 / 2) / (2 * a)
        x2 = (-b + delta * 1 / 2) / (2 * a)
        if a > 0:
            return f'Funkcja ma dwa miejsca zerowe x1 = {x1}, x2 = {x2} oraz ramiona są skierowane do góry'
        else:
            return f'Funkcja ma dwa miejsca zerowe x1 = {x1}, x2 = {x2} oraz ramiona są skierowane do dołu'
    elif delta == 0:
        x0 = -b / (2 * a)
        if a > 0:
            return f'Funkcja ma jedno miejsce zerowe x0 = {x0} oraz ramiona są skierowane do góry'
        else:
            return f'Funkcja ma jedno miejsce zerowe x0 = {x0} oraz ramiona są skierowane do dołu'
    else:
        f'Funkcja nie ma rozwiązania'
