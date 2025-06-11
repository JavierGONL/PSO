 # a chambear :v
import random
from Enjambre import *
from Funciones_objetivo import *
from vector import *

import numpy as np

import matplotlib.pyplot as plt

# me traeré la clase para tener una referencia 
#creo que esta vuelta toca rehacerla


def Rastrigin_function(posicion, A_constante = 10): # le entra la posicion y calcula el valor
    # where A=10 (generalmente and posicion ∈ [-5.12,5.12]
    n = len(posicion) # dimension
    A = A_constante
    suma = 0
    for i in posicion:
        suma += i**2 - A * cos(2*pi*i)
    return A*n + suma #! revisar si esta bien implementada

# Test para verificar la función Rastrigin
if __name__ == "__main__":
    print("[0,0] =", Rastrigin_function([0,0]))  # Debe dar 0
    print("[1,1] =", Rastrigin_function([1,1])) # 2
    print("[5.12,5.12] =", Rastrigin_function([5.12,5.12]))
    # Dominio de ejemplo para cada dimensión (por ejemplo, [-5, 5])
    dominio = [-5, 5]
    dimension = 2
    swarm = Swarm(number_of_particles=5, dominio=dominio, dimension=dimension)
    swarm.inicialize_each_particle()
    # Mostrar posiciones iniciales de las partículas
    for idx, p in enumerate(swarm.particulas):
        print(f"Partícula {idx+1}: posición = {p.p_position}, velocidad = {p.speed}")
        #* este es el ejemplo de matplotlib

    x = np.linspace(-5, 5,100)
    y = np.linspace(-5, 5,100)
    x, y = np.meshgrid(x,y) #hace el sistema de coordenadas
    z = x*y #funcion de X,Y
    
    fig = plt.figure(figsize=(14,16))
    ax = fig.add_subplot(111,projection = '3d')
    ax.plot_surface(x,y,z, cmap ='viridis')
    ax.set_title("gráfica 3D")
    plt.show()