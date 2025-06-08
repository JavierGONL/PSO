import random

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
        self.position = posicion*dimension
        self.vel_i = velocidad_inicial
        self.valor = 0 #! no se si calcular esto aca en el enjambre / btw seria el rango?
        self.best_position = []
        self.historial_positions = []

    def inicialice_particle():
        """
        definir su posicion y velocidad inicial
        """
        pass

    def calculate_value(self):
        self.position[-1] = None # para esto falta la funcion objetivo

    def update_particle(self, w, c1, r1, c2, r2):
        """
        Mover una partícula implica actualizar su velocidad y posición. 
        Este paso es el más importante ya que otorga al algoritmo la capacidad de optimizar.
        
        vi(t+1)=wvi(t)+c1r1[^xi(t)−xi(t)]+c2r2[g(t)−xi(t)] 
        
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
        primer_termino = w*self.vel_i # es vel_i en la iteracion / T actual
        segundo_termno = c1*r1*(self.best_position - self.position)
        pass

class swarm: #enjambre 
    def __init__(self, dimension = 2, number_of_particles = 0, dominio = []):
        self.number_of_particles = number_of_particles
        self.dominio = dominio
        self.particulas = [0]*dimension
        self.best_value = 0
        self.best_position = [0]*dimension
        self.maximice = False # min por defecto

    def define_initial_vel_to_each_particle(self):
        for i in self.particulas:
            i.vel_i = random.uniform(0,1)
    
    def define_initial_pos_to_each_particle(self, funcion):
        for i in self.particulas:
            for j in i.position:
                i.position[j] = random.uniform(self.dominio[0],self.dominio[1])
            i.position[-1] = i.calculate_value(funcion)

    def next_iteration(self):
        pass
