'''
    * Descripción: clase particula y enjambre
    * documentos relacionados: paquetes
    * autores: kevin javier gonzalez luna, ivan felipe maluche, david Montes
    * --------------------------------- TODO -------------------------------------------------
    * Lista de feature por hacer:
    * - iteracion en Swarm
    * 
    *
    * --------------------------------- ISSUES -----------------------------------------------
    * Lista de problemas conocidos:
    * - optimizar el codigo y seguir el pep8
    *
    * ----------------------------------------------------------------------------------------
'''

import random

from Funciones_objetivo import *
from prueba_vector import *

class Particle:
    """
    Cada partícula está definida por una posición, 
    velocidad y valor que varían a medida que la partícula se mueve. 
    Además, también almacena la mejor posición en la que ha estado hasta el momento. 
    Cuando se crea aun nueva partícula, 
    únicamente se dispone de información sobre su posición y velocidad (normalmente iniciada como cero), 
    el resto de valores no se conocen hasta que la partícula es evaluada.
    """

    def __init__(self, posicion=None, velocidad_inicial=None, dimension=2):
        if posicion is None:
            posicion = Point(0, 0)
        if velocidad_inicial is None:
            velocidad_inicial = Vector(0, 0)
        self.p_position: Point = posicion
        self.speed: Vector = velocidad_inicial
        self.value: float = 0
        self.p_best_value: float = 0
        self.p_best_position: Point = Point(0,0)
        self.historial_positions = []
        self.initialize: bool = False
        self.dimension: int = dimension

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

class Swarm: #enjambre 
    def __init__(self,  number_of_particles = 0, dominio = [float], dimension = 2): #! para el dominio solo pasamos como si fuera una variable, pero en verdad seria un rectangulo
        self.number_of_particles : int = number_of_particles
        self.dominio : list = dominio
        self.particulas = [Particle(dimension=dimension) for _ in range(number_of_particles)]
        self.g_best_value : float = 0
        self.g_best_position : Point = Point(0,0)  # Inicializa como Point
        self.maximice : bool = False # min por defecto
        self.dimension : int = dimension
        
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
