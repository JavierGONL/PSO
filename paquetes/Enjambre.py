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

from paquetes.Funciones_objetivo import *
from paquetes.vector import Point, Vector

class Particle: # particula
    """
    Cada partícula está definida por una posición, 
    velocidad y valor que varían a medida que la partícula se mueve. 
    Además, también almacena la mejor posición en la que ha estado hasta el momento. 
    Cuando se crea una nueva partícula, 
    únicamente se dispone de información sobre su posición y velocidad 
    (normalmente iniciada como cero), el resto de valores no se conocen hasta que 
    la partícula es evaluada.
    """
    def __init__(self,  dimension = 2, ):
        self.p_position= Point(0,0)
        self.speed = Vector(0,0)
        self.value: float = 0
        self.p_best_value: float = 0
        self.p_best_position = Point(0,0)
        self.historial_positions  = []
        self.initialize = False
        self.dimension = dimension
        self.maximice : bool = False


    def initialize_particle(self, maximice, dominio):
        """definirle una posicion y velocidad inicial aleatoria"""
        random_para_V = [random.uniform(-1, 1) for _ in range(self.dimension)] # usando list comprehension
        random_para_p = [random.uniform(dominio[0], dominio[1]) for _ in range(self.dimension)]
        self.speed = Vector(*random_para_V)
        self.p_position = Point(*random_para_p)
        self.initialize : bool = True
        self.maximice = maximice
        self.value = self.calculate_value()

    def calculate_value(self):
        if self.initialize:
            self.historial_positions.append(self.p_position)
            self.value = himmelblaus_function(self.p_position.comp_to_list) #! de ejempo toca ver como variar la funcion 
            if self.value < self.p_best_value and not self.maximice: # minimizar
                self.p_best_value = self.value
                self.p_best_position = self.p_position
            elif self.value > self.p_best_value and self.maximice: # maximizar
                self.p_best_value = self.value
                self.p_best_position = self.p_position
            return self.value
        else:
            return "hay que inicializar la particula antes"

class Swarm: #enjambre 
    def __init__(self, 
                number_of_particles = 0, 
                dominio = [], 
                maximice = False, 
                dimension = 2
                ): 
        self.number_of_particles = number_of_particles
        self.dominio : list = dominio #! para el dominio solo pasamos como si fuera de una variable, pero en verdad seria un rectangulo
        self.particulas = [Particle(dimension) for _ in range(number_of_particles)]
        self.g_best_value : float = float("inf")
        self.g_best_position = Point(0,0)  # Inicializa como Point
        self.maximice = maximice 
        self.dimension : int = dimension
        
    def inicialize_each_particle(self): #! falta revisar si funciona D:
        for i in self.particulas:
            i.initialize_particle(self.maximice, self.dominio)

    def update_gbestv_and_gbestpos(self):
        for i in self.particulas:
            if i.value < self.g_best_value and not self.maximice:
                self.g_best_value = i.value
                self.g_best_position = i.p_position
            elif i.value > self.g_best_value and self.maximice:
                self.g_best_value = i.value
                self.g_best_position = i.p_position

    def update_particles(self, w, c1, c2): #! creo que esto si va en swarm, la velocidad es un vector
        """
        Mover una partícula implica actualizar su velocidad y posición. 
        Este paso es el más importante ya que otorga al algoritmo la capacidad de optimizar.
        
        vi(t+1)= wvi(t)+c1r1[^xi(t)- xi(t)]+c2r2[g(t) - xi(t)] 
        
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
        valores_randoms_1 = [random.uniform(0,1) for _ in range(self.dimension)]
        valores_randoms_2 = [random.uniform(0,1) for _ in range(self.dimension)]
        r1 = Vector(*valores_randoms_1)
        r2 = Vector(*valores_randoms_2)
        for i in self.particulas:
            # Termino de inercia
            primer_termino = w * i.speed
            # Termino cognitivo
            segundo_termino = c1 * r1 * (i.p_best_position - i.p_position)
            # Termino social
            tercer_termino = c2 * r2 * (self.g_best_position - i.p_position)
            # Actualiza la velocidad
            i.speed = primer_termino + segundo_termino + tercer_termino

            #! Limita la velocidad (opcional pero mejora convergencia)
            #! esta horrible, luego lo mejoro
            speed_limit = (self.dominio[1] - self.dominio[0]) * 0.2
            if i.speed.x > speed_limit:
                i.speed.x = speed_limit
            elif i.speed.x < -speed_limit:
                i.speed.x = -speed_limit
            if i.speed.y > speed_limit:
                i.speed.y = speed_limit
            elif i.speed.y < -speed_limit:
                i.speed.y = -speed_limit

            # Actualiza la posición
            i.p_position = i.p_position + i.speed

            #! Restringe la posición al dominio
            if i.p_position.x < self.dominio[0]:
                i.p_position.x = self.dominio[0]
            elif i.p_position.x > self.dominio[1]:
                i.p_position.x = self.dominio[1]
            if i.p_position.y < self.dominio[0]:
                i.p_position.y = self.dominio[0]
            elif i.p_position.y > self.dominio[1]:
                i.p_position.y = self.dominio[1]

            # calcula el valor y actualiza las best globales
            i.calculate_value()
            self.update_gbestv_and_gbestpos()

    def iterations(self, number_iterations, w,c1,c2):
        while number_iterations > 0:
            self.update_particles(w, c1, c2)
            # for i in self.particulas:
            #     print(f"P: {i.p_position},   V: {i.speed}, Value: {i.value}")
            number_iterations -= 1
            self.listas_para_david() 
        return print(f"la mejor posicion es {round(self.g_best_position, 5)}, con valor de {round(self.g_best_value, 5)}")
    
    def listas_para_david(self):
        lista_x = []
        lista_y = []
        lista_z = []
        lista_de_listas = []
        for i in self.particulas:
            lista_x.append(i.p_position.x)
            lista_y.append(i.p_position.y)
            lista_z.append(i.value)
        lista_de_listas.append(lista_x)
        lista_de_listas.append(lista_y)
        lista_de_listas.append(lista_z)
        return lista_de_listas
