from math import cos, pi
#? creamos una clase para elegir funciones objetivo??? 

def Rastrigin_function(posicion, A_constante = 10): # le entra la posicion y calcula el valor
    # where A=10 (generalmente and posicion ∈ [-5.12,5.12]
    n = len(posicion) # dimension
    A = A_constante
    suma = 0
    for i in posicion:
          suma += i**2 - A * cos(2*pi*i)
    return A*n + suma #! revisar si esta bien implementada

def funcion_objetivo_2():
    pass

def funcion_objetivo_3():
    pass

def funcion_objetivo_4():
    pass
#hola :)