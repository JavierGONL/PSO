'''
    * Descripción: se definen una serie de funciones de ejemplo que permitiran demostrar el funcionamiento del pso 
    * documentos relacionados: paquetes
    * autores: Kevin Javier Gonzalez, Ivan Felipe Maluche, David Alejandro Montes
'''
from numpy import pi, cos, exp, sqrt

def rastrigin_function(posicion:list, A_constante = 10)-> float: # le entra la posicion y calcula el valor
    # where A=10 (generalmente and posicion ∈ [-5.12,5.12]
    n = len(posicion) # dimension
    A = A_constante
    suma = 0
    for i in posicion:
        suma += i**2 - A * cos(2*pi*i)
    return A*n + suma #! revisar si esta bien implementada

def himmelblaus_function(posicion):
    primer_termino = (posicion[0]**2 + posicion[1] - 11)**2
    segundo_termino = (posicion[0] + posicion[1]**2 - 7)**2
    return primer_termino + segundo_termino

def shekel_function_maximizar(posicion):
    m = 10
    n = 2
    c1 = [0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5]
    c2 = [
        [4, 1, 8, 6, 3, 2, 5, 8, 6, 7],
        [4, 1, 8, 6, 7, 9, 3, 1, 2, 3.6]
    ]
    total = 0
    for i in range(m):
        suma = 0
        for j in range(n):
            suma += (posicion[j] - c2[j][i]) ** 2
        total += 1 / (suma + c1[i])
    return total

def shekel_function(posicion):
    m = 10
    n = 2
    c1 = [0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5]
    c2 = [
        [4, 1, 8, 6, 3, 2, 5, 8, 6, 7],
        [4, 1, 8, 6, 7, 9, 3, 1, 2, 3.6]
    ]
    total = 0
    for i in range(m):
        suma = 0
        for j in range(n):
            suma += (posicion[j] - c2[j][i]) ** 2
        total += 1 / (suma + c1[i])
    return -total
#APARENTEMENTE ya esta ;)

def ackley_function_invertida(posicion): # algo de ejemplo para maximizar
    a = 20
    b = 0.2
    c = 2 * pi
    n = len(posicion)
    primer_termino = sum(x**2 for x in posicion)
    segundo_termino = sum(cos(c*x) for x in posicion)
    ackley = (-a * exp(-b * sqrt(primer_termino / n)) 
            - exp(segundo_termino / n) + a + exp(1)
            )
    return -ackley 