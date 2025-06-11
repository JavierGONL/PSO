from math import cos, pi
from prueba_vector import Point, Vector as Point, Vector
#? creamos una clase para elegir funciones objetivo??? 

def Rastrigin_function(posicion, A_constante = 10)-> float: # le entra la posicion y calcula el valor
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

def shekel_function(x,y):
    pass


# Test para verificar la función Rastrigin
if __name__ == "__main__":
    print("[0,0] =", Rastrigin_function([0,0]))  # Debe dar 0
    print("[1,1] =", Rastrigin_function([4.5,4.5])) # 2
    print("[5.12,5.12] =", Rastrigin_function([5.12,5.12]))