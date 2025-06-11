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
if __name__ == "__main__":
    # Dominio de ejemplo para cada dimensión (por ejemplo, [-5, 5])
    dominio = [-5, 5]
    dimension = 2
    swarm = Swarm(number_of_particles=5, dominio=dominio, dimension=dimension)
    swarm.inicialize_each_particle()
    # Mostrar posiciones iniciales de las partículas
    for idx, p in enumerate(swarm.particulas):
        print(f"Partícula {idx+1}: posición = {p.p_position}, velocidad = {p.speed}")
        #* este es el ejemplo de matplotlib
    
    fig, axs = plt.subplots(2)
    fig.suptitle("2 subplots verticales")
    # Primer subplot
    ax = axs[0][0]
    ax.plot(np.arange(0, 1e6, 1000))
    ax.set_title('Title0 0')
    ax.set_ylabel('YLabel0 0')
    # Puntos aleatorios en el mismo rango
    x_rand = np.random.uniform(0, 1e6, 20)
    y_rand = np.random.uniform(ax.get_ylim()[0], ax.get_ylim()[1], 20)
    ax.scatter(x_rand, y_rand, color='r', label='Puntos aleatorios')
    ax.legend()

    # Segundo subplot
    ax = fig.add_subplot(projection='3d')

    # Plot a sin curve using the x and y axes.
    x = np.linspace(0, 1, 1000)
    y = np.sin(x * 2 * np.pi) / 2 + 0.5 #!Función 
    ax.plot(x, y, zs=0, zdir='z', label='curve in (x, y)')

    # Plot scatterplot data (20 2D points per colour) on the x and z axes.
    colors = ('r', 'g', 'b', 'k')

    # Fixing random state for reproducibility
    #np.random.seed(19680801) #* ya ví que hace esta vuelta, genera los puntos siempre en la misma posición
    x = np.random.sample(20)
    y = np.random.sample(20)
    # By using zdir='y', the y value of these points is fixed to the zs value 0
    # and the (x, y) points are plotted on the x and z axes.
    ax.scatter(x, y, zs=0, zdir='y', c='r', label='points in (x, z)')

    # Make legend, set axes limits and labels
    ax.legend()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Customize the view angle so it's easier to see that the scatter points lie
    # on the plane y=0
    ax.view_init(elev=20., azim=-35, roll=0)
    # Puntos aleatorios en el mismo rango
    x_rand = np.random.uniform(x.min(), x.max(), 20) #!! aquí va un arreglo que entregue enjambre
    y_rand = np.random.uniform(y.min(), y.max(), 20) #!! aquí va un arreglo
    ax.scatter(x_rand, y_rand, color='r', label='Puntos aleatorios')
    ax.legend()

    plt.show()
    
#este código de abajo funciona
"""
    ax = plt.figure().add_subplot(projection='3d')

    # Plot a sin curve using the x and y axes.
    x = np.linspace(0, 1, 1000)
    y = np.sin(x * 2 * np.pi) / 2 + 0.5
    ax.plot(x, y, zs=0, zdir='z', label='curve in (x, y)')

    # Plot scatterplot data (20 2D points per colour) on the x and z axes.
    colors = ('r', 'g', 'b', 'k')

    # Fixing random state for reproducibility
    #np.random.seed(19680801)
    #* ya ví que hace esta vuelta, genera los puntos siempre en la misma posición
    x = np.random.sample(20)
    y = np.random.sample(20)
    # By using zdir='y', the y value of these points is fixed to the zs value 0
    # and the (x, y) points are plotted on the x and z axes.
    ax.scatter(x, y, zs=0, zdir='y', c='r', label='points in (x, z)')

    # Make legend, set axes limits and labels
    ax.legend()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Customize the view angle so it's easier to see that the scatter points lie
    # on the plane y=0
    ax.view_init(elev=20., azim=-35, roll=0)
"""
    #plt.show() von dem 3D object
    
    