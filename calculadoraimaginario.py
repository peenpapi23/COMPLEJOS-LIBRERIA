import math

def sumai(a, b):
    # a y b son tuplas de la forma (parteReal, parteImaginaria)
    parteReal = a[0] + b[0]
    parteImaginaria = a[1] + b[1]
    return (parteReal, parteImaginaria)

def multiplicacion(a, b):
    parteReal = a[0] * b[0] - a[1] * b[1]
    parteImaginaria = a[0] * b[1] + a[1] * b[0]
    return (parteReal, parteImaginaria)

def resta(a, b):
    parteReal = a[0] - b[0]
    parteImaginaria = a[1] - b[1]
    return (parteReal, parteImaginaria)

def division(a, b):
    denominador = b[0]**2 + b[1]**2
    parteReal = (a[0] * b[0] + a[1] * b[1]) / denominador
    parteImaginaria = (a[1] * b[0] - a[0] * b[1]) / denominador
    return (parteReal, parteImaginaria)

def modulo(a):
    # Calcula la magnitud del número complejo
    return math.sqrt(a[0]**2 + a[1]**2)

def conjugado(a):
    # Devuelve el conjugado de un número complejo
    return (a[0], -a[1])

def conversionCartPolar(a):
    # Convierte de cartesiano a polar
    p = math.sqrt(a[0]**2 + a[1]**2)
    angulo = math.atan2(a[1], a[0])  # Nota: atan2 recibe los argumentos (y, x)
    return (p, angulo)

def conversionPolarCart(a):
    # Convierte de polar a cartesiano
    magnitud = a[0]
    angulo = a[1]
    parteReal = magnitud * math.cos(angulo)
    parteImaginaria = magnitud * math.sin(angulo)
    return (parteReal, parteImaginaria)

def fase(a):
    # Calcula la fase (ángulo) de un número complejo
    return math.atan2(a[1], a[0])

