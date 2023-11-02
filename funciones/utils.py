def calcularArea(base, altura):
    areaTotal = None
    areaTotal = base * altura
    return areaTotal

def conteo(hastaNumero):
    """Esto es una funcion que cuenta

    Args:
        hastaNumero (number): hasta donde cuenta la funcion
    """
    for number in range(hastaNumero):
        print(number)

def fibonacci(n):
    """Esta es una funcion recursiva fibonacci

    Args:
        n (number): debe ser un numero >= a 0

    Returns:
        Number: devuelve el calculo de fibonacci
    """
    if (n == 0) or (n == 1):
        return (n)
    else:
        return (fibonacci(n-2)+fibonacci(n-1))