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

def Himmelblaus_function(posicion):
    primer_termino = (posicion[0]**2 + posicion[1] - 11)**2
    segundo_termino = (posicion[0] + posicion[1]**2 - 7)**2
    return primer_termino + segundo_termino


def funcion_objetivo_3():
    pass

def shekel_function(x,y):
    vinc : list = [x,y]
    m : int = 10
    n : int = 2
    c1 = [0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5] #arreglo de constantes 1
    c2 = [[4 ,1, 8, 6, 3, 2, 5, 8, 6, 7],[4, 1, 8, 6, 7, 9, 3, 1, 2, 3.6]] #matriz de constantes 2
    nj = 0
    mi = 0
    pr = 0
    r = 0
    while mi <= m-1:
        while nj <= n-1:
            pr = pr + ((vinc[nj]-((c2[nj])[mi]))**2 + c1[mi])
            nj = nj + 1
        print(1/pr)
        r = r + (1/pr)
        mi = mi +1 
        pr= 0
        nj = 0
    return -r
#APARENTEMENTE ya esta ;)


# Test para verificar la función Rastrigin
if __name__ == "__main__":
    print("[0,0] =", Himmelblaus_function([3,2]))  # Debe dar 0
    #print("[1,1] =", Rastrigin_function([4.5,4.5])) # 2
#print("[5.12,5.12] =", Rastrigin_function([5.12,5.12]))
    #print( shekel_function(1,2))