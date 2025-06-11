 # a chambear :v
import random

from Funciones_objetivo import *
from vector import *

import numpy as np

import matplotlib.pyplot as plt

# me traeré la clase para tener una referencia 
#creo que esta vuelta toca rehacerla
class Particle:
    """
    Cada partícula está definida por una posición, 
    velocidad y valor que varían a medida que la partícula se mueve. 
    Además, también almacena la mejor posición en la que ha estado hasta el momento. 
    Cuando se crea aun nueva partícula, 
    únicamente se dispone de información sobre su posición y velocidad (normalmente iniciada como cero), 
    el resto de valores no se conocen hasta que la partícula es evaluada.
    """

    def __init__(self, posicion = [Point], velocidad_inicial = [Vector], dimension = 2): # la dimencion es del dominio
        self.p_position : Point = posicion # hay que acmbiarlo a point #este Point se hereda de vector
        self.speed : Vector = velocidad_inicial
        self.value : float = 0 #! no se si calcular esto aca en el enjambre, btw seria el rango?
        self.p_best_value : float = 0
        self.p_best_position : Point = Point(0,0)  # Inicializa como Point
        self.historial_positions = []
        self.initialize : bool = False
        self.dimension = dimension

    def initialize_particle(self,dominio):
        """definir su posicion y velocidad inicial para cualquier dimension"""
        random_para_V = [random.uniform(-1, 1) for _ in range(self.dimension)] # list comprehension
        random_para_p = [random.uniform(dominio[0], dominio[1]) for _ in range(self.dimension)]
        self.speed = Vector(*random_para_V)
        self.p_position = Point(*random_para_p)
        self.initialize = True

    def calculate_value(self):
        if self.initialize:
            self.historial_positions.append(self.p_position) #! toca inicializar la particula antes
            self.value = Rastrigin_function(self.p_position.comp_to_list) # de ejempo toca ver como variar la funcion 
            if self.value > self.p_best_value:
                self.p_best_value = self.value
                self.p_best_position = self.p_position
        else:
            return "hay que inicializar la particula antes"



# me pregunto si el enjambre podría no requerir la partícula, y que las partículas sean arreglos de numpy
class Swarm: #enjambre 
    def __init__(self,  number_of_particles = 0, dominio = [float], dimension = 2,): #! para el dominio solo pasamos como si fuera una variable, pero en verdad seria un rectangulo
        self.number_of_particles : int = number_of_particles
        self.dominio : list = dominio
        self.particulas = [Particle() for _ in range(number_of_particles)]
        self.g_best_value : float = 0
        self.g_best_position : Point = Point(0,0)  # Inicializa como Point
        self.maximice : bool = False # min por defecto
        self.dimension : list = dimension
        
    def inicialize_each_particle(self): #! falta revisar si funciona D:
        for i in self.particulas:
            i.initialize_particle(self.dominio)

    def update_gbest(self):
        g_best = 0
        for i in self.particulas:
            if i.value > g_best:
                g_best = i.value

    def update_particles(self, w, c1, c2): #! creo que esto si va en swarm, la velocidad es un vector
        """
        Mover una partícula implica actualizar su velocidad y posición. 
        Este paso es el más importante ya que otorga al algoritmo la capacidad de optimizar.
        
        vi(t+1)=wvi(t)+c1r1[^xi(t)- xi(t)]+c2r2[g(t) - xi(t)] 
        
        donde:
        vi(t+1): velocidad de la partícula i en el momento  t+1, es decir, la nueva velocidad.
        vi(t): velocidad de la partícula  i en el momento  t, es decir, la velocidad actual.
        w: coeficiente de inercia, reduce o aumenta a la velocidad de la partícula.
        c1: coeficiente cognitivo.
        r1: vector de valores aleatorios entre 0 y 1 de longitud igual a la del vector velocidad.
        ^xi(t): mejor posición en la que ha estado la partícula i hasta el momento.
        xi(t): posición de la partícula  i en el momento  t.
        c2: coeficiente social.
        r2: vector de valores aleatorios entre 0 y 1 de longitud igual a la del vector velocidad.
        g(t): posición de todo el enjambre en el momento t, el mejor valor global.
        """
        valores_randoms_1 = [random.uniform(-1, 1) for _ in range(self.dimension)]
        valores_randoms_2 = [random.uniform(-1, 1) for _ in range(self.dimension)]
        r1 : "Vector" = Vector(*valores_randoms_1)  # debe ser de longitud del vector velocidad, con longitud se refierea la dim, el *valores_random desempaqueta la lista
        r2 : "Vector" = Vector(*valores_randoms_2)
        for i in self.particulas:
            i.calculate_value()
            primer_termino = w*i.speed #* es speed en la iteracion / T actual, nercia
            segundo_termino = (c1*r1)*(i.p_best_position - i.p_position) #* cognitivo
            tercer_termino = (c2*r2)*(self.g_best_position - i.p_position) #* social
            i.speed = primer_termino + segundo_termino + tercer_termino #! aca se actualiza la velocidad y debe ser un vector?
            # aca se actualiza la posicion 
            # Actualiza la posición de la partícula sumando la velocidad actual a la posición anterior.
            #* Fórmula: x_i(t+1) = x_i(t) + v_i(t+1) !!! esto es un vector
            #! asi?? abajo, creo que si dado que ambos son vectores(deberia ser un vector y un punto) y esta definido la suma aunque creo que hay que definir una clase punto con el metodo de sumar definido para que sume bien entre un vector y un punto
            i.p_position = Point(i.p_position.x + i.speed.x, i.p_position.y + i.speed.y)

    def next_iteration(self, number_iterations):
        # debe permitirte avanzar o retroceder, esto serviria para debugear llegado el caso
        pass
    


#* este es el ejemplo de matplotlib


ax = plt.figure().add_subplot(projection='3d')

# Plot a sin curve using the x and y axes.
x = np.linspace(0, 1, 1000)
y = np.sin(x * 2 * np.pi) / 2 + 0.5
ax.plot(x, y, zs=0, zdir='z', label='curve in (x, y)')

# Plot scatterplot data (20 2D points per colour) on the x and z axes.
colors = ('r', 'g', 'b', 'k')

# Fixing random state for reproducibility
np.random.seed(19680801) #*ni idea esto que hace, pero está en el ejemplo de matplotlib

x = np.random.sample(20 * len(colors))
y = np.random.sample(20 * len(colors))
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

#plt.show() von dem 3D object



fig, axs = plt.subplots(2, 2, layout='constrained')

ax = axs[0][0]
ax.plot(np.arange(0, 1e6, 1000))
ax.set_title('Title0 0')
ax.set_ylabel('YLabel0 0')

ax = axs[0][1]
ax.plot(np.arange(1., 0., -0.1) * 2000., np.arange(1., 0., -0.1))
ax.set_title('Title0 1')
ax.xaxis.tick_top()
ax.tick_params(axis='x', rotation=55)


for i in range(2):
    ax = axs[1][i]
    ax.plot(np.arange(1., 0., -0.1) * 2000., np.arange(1., 0., -0.1))
    ax.set_ylabel('YLabel1 %d' % i)
    ax.set_xlabel('XLabel1 %d' % i)
    if i == 0:
        ax.tick_params(axis='x', rotation=55)
    x_rand = np.random.rand(20)
    y_rand = np.random.rand(20)
    ax.scatter(x_rand, y_rand, color='r', label='Puntos aleatorios')
    ax.legend()
fig.align_labels()  # same as fig.align_xlabels(); fig.align_ylabels()
fig.align_titles()

plt.show()