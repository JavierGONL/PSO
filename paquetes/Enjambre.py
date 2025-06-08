import random

from Funciones_objetivo import *

class Vector: # no se si definir una clase vector
    pass

class Particle:
    """
    Cada partícula está definida por una posición, 
    velocidad y valor que varían a medida que la partícula se mueve. 
    Además, también almacena la mejor posición en la que ha estado hasta el momento. 
    Cuando se crea aun nueva partícula, 
    únicamente se dispone de información sobre su posición y velocidad (normalmente iniciada como cero), 
    el resto de valores no se conocen hasta que la partícula es evaluada.
    """

    def __init__(self, posicion = [], velocidad_inicial = [], dimension = 2): # la dimencion es del dominio
        self.p_position = posicion*dimension
        self.speed = velocidad_inicial
        self.value = 0 #! no se si calcular esto aca en el enjambre / btw seria el rango?
        self.p_best_value = 0
        self.p_best_position = []
        self.historial_positions = []

    def inicialice_particle():
        """
        definir su posicion y velocidad inicial
        """
        pass

    def calculate_value(self):
        self.value = funcion_objetivo_1(self.position)
        if self.value > self.best_value:
            self.best_value = self.value
            self.best_position = self.position

class swarm: #enjambre 
    def __init__(self, dimension = 2, number_of_particles = 0, dominio = []):
        self.number_of_particles : int = number_of_particles
        self.dominio = dominio
        self.particulas = [0]*dimension
        self.g_best_value : float = 0
        self.g_best_position = [0]*dimension
        self.maximice = False # min por defecto

    def define_initial_vel_to_each_particle(self): #! falta revisar si funciona D:
        for i in self.particulas:
            i.speed = random.uniform(0,1) # 0 min velocidad, 1 maxima
    
    def define_initial_pos_to_each_particle(self, funcion): #! falta revisar si funciona D:
        for i in self.particulas:
            for j in range(i.position):
                i.position[j] = random.uniform(i.dominio[j]) # en teoria esto funciona

    def update_particles(self, w, c1, c2): #! creo que esto va en swarm
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
        r1 = random.uniform(0,1)
        r2 = random.uniform(0,1)
        for i in self.particulas:
            primer_termino = w*self.speed #* es speed en la iteracion / T actual, nercia
            segundo_termino = c1*r1*(i.p_best_position - i.p_position) #* cognitivo
            tercer_termino = c2*r2*(self.g_best_position - i.p_position) #* social
            i.speed = primer_termino + segundo_termino + tercer_termino #* aca se actualiza la velocidad
            # aca se actualiza la posicion 
            # Actualiza la posición de la partícula sumando la velocidad actual a la posición anterior.
            #* Fórmula: x_i(t+1) = x_i(t) + v_i(t+1)
            i.p_position = i.p_position + i.speed #! asi?? 
        pass

    def next_iteration(self): 
        # debe permitirte avanzar o retroceder, esto serviria para debugear llegado el caso
        pass
