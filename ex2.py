def list_function(x):
    result = 0
    for item in x:
        result += item

    average = result / len(x)
    maximum = max(x)
    minimum = min(x)
    return f'Średnia z listy wynosi {average}, największa liczba to {maximum}, a najmniejsza to {minimum}'

