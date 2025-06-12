 # a chambear :v
import random
from Enjambre import *
from Funciones_objetivo import *
from vector import *

import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

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
def primera_funcion(x,y):
    pass
# Test para verificar la función Rastrigin
if __name__ == "__main__":
    print("[0,0] =", Rastrigin_function([0,0]))  # Debe dar 0
    print("[1,1] =", Rastrigin_function([1,1])) # 2
    print("[5.12,5.12] =", Rastrigin_function([5.12,5.12]))
    # Dominio de ejemplo para cada dimensión (por ejemplo, [-5, 5])
    dominio_upper = 10
    dominio_down = -10
    dominio = [dominio_down, dominio_upper]
    dimension = 2
    swarm = Swarm(number_of_particles=500, dominio=dominio, dimension=dimension)
    swarm.inicialize_each_particle()
    # Mostrar posiciones iniciales de las partículas
    for idx, p in enumerate(swarm.particulas):
        print(f"Partícula {idx+1}: posición = {p.p_position}, velocidad = {p.speed}")

    x = np.linspace(dominio_down, dominio_upper,100)
    y = np.linspace(dominio_down, dominio_upper,100)
    x, y = np.meshgrid(x,y) #hace el sistema de coordenadas
    z = np.cos(x) + np.cos(y) #funcion de X,Y 
    #probar poner puntos
    x_particulas = np.array([p.p_position.x for idx,p in enumerate(swarm.particulas)]) #! se consigue el arreglo para los puntos de las partículas
    y_particulas = np.array([p.p_position.y for idx,p in enumerate(swarm.particulas)]) #ni pinche idea por qué no llama a idx, pero si lo quito no funciona
    print(x_particulas)
    #print(y_particulas)
    #print(str(z))
    fig = plt.figure(figsize=(16,12))
    
    ax = fig.add_subplot(2,2,1,projection = '3d') #gráfica #1 de la malla 2x2
    ax.plot_surface(x,y,z, cmap ='viridis', alpha = 0.6)
    ax.scatter3D(x_particulas,y_particulas, np.cos(x_particulas)+np.cos(y_particulas),c = 'red', s = 100, edgecolor = 'k', linewidth = 1.5)
    ax.set_title("gráfica 3D")
    ax.set_xlabel("eje X")
    ax.set_ylabel("eje Y")
    ax.set_zlabel("Eje Z")
    
    
    ax_2 = fig.add_subplot(2,2,2)
    contour = ax_2.contourf(x, y, z, cmap ="viridis")
    ax_2.scatter(x_particulas,y_particulas,c = 'red', s = 100, edgecolor = 'k', linewidth = 1)
    fig.colorbar(contour, ax = ax_2, shrink = 0.5, aspect = 5) #!problema con los colores, luego arreglar
    
    ax_2.set_title("vista superior")
    ax_2.set_xlabel("eje X")
    ax_2.set_ylabel("eje Y")
    
    # segundas gráficas
    z = x**2 +y**2 #funcion de X,Y
    ax_3 = fig.add_subplot(2,2,3,projection = '3d')
    ax_3.plot_surface(x,y,z, cmap ='viridis', alpha = 0.6 )
    ax_3.scatter3D(x_particulas,y_particulas, x_particulas**2 + y_particulas**2,c = 'red', s = 100, edgecolor = 'k', linewidth = 1.5)
    ax_3.set_title("gráfica 3D 2")
    ax_3.set_xlabel("eje X")
    ax_3.set_ylabel("eje Y")
    ax_3.set_zlabel("Eje Z")
    
    ax_4 = fig.add_subplot(2,2,4)
    contour = ax_4.contourf(x, y, z, cmap ="viridis")
    ax_4.scatter(x_particulas,y_particulas, c = 'red', s = 100, edgecolor = 'k', linewidth = 1)
    fig.colorbar(contour, ax = ax_2, shrink = 0.5, aspect = 5)
    
    ax_4.set_title("vista superior 2")
    ax_4.set_xlabel("eje X")
    ax_4.set_ylabel("eje Y")

    plt.tight_layout()
    plt.show()