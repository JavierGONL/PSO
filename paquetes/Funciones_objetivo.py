from numpy import pi, cos

def rastrigin_function(posicion, A_constante = 10)-> float: # le entra la posicion y calcula el valor
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

def sphere_function(posicion):
    suma = 0
    for i in posicion:
        suma += i**2
    return suma

def shekel_function(posicion):
    vinc : list = posicion
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
        #print(1/pr)
        r = r + (1/pr)
        mi = mi +1 
        pr= 0
        nj = 0
    return -r
#APARENTEMENTE ya esta ;)