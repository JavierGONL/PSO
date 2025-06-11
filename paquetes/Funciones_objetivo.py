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
    vinc : list = [x,y]
    m : int = 10
    n : int = 2
    c1= [1/10,2/10,2/10,4/10,4/10,6/10,3/10,7/10,5/10,5/10] #arreglo de constantes 1
    c2= [[4 ,1, 8, 6, 3, 2, 5, 8, 6, 7],[4, 1, 8, 6, 7, 9, 3, 1, 2, 3.6]] #matriz de constantes 2
    ni= 0
    mj= 0
    pr = 0
    r = 0
    while mj <= m:
        while ni <= n:
            pr = pr + (vinc[ni-1]-c2[ni-1][mj-1]**2 + c1[mj-1])



# Test para verificar la función Rastrigin
if __name__ == "__main__":
    print("[0,0] =", Rastrigin_function([0,0]))  # Debe dar 0
    print("[1,1] =", Rastrigin_function([4.5,4.5])) # 2
    print("[5.12,5.12] =", Rastrigin_function([5.12,5.12]))