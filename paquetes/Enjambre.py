'''
    * Descripcion: clase particula y enjambre
    * documentos relacionados:  
    * autores: kevin javier gonzalez luna, ivan felipe maluche, david Montes
'''
import random
import time

from paquetes.Funciones_objetivo import (rastrigin_function, shekel_function,
                                        himmelblaus_function, sphere_function)
from paquetes.Vector_v2 import Point, Vector

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d #! esto para que esta?

funcion = rastrigin_function

class Particle:  # particula
    """
    Cada particula esta definida por una posicion,
    velocidad y valor que varian a medida que la particula se mueve.
    Ademas, tambien almacena la mejor posicion en la que ha estado hasta
    el momento. Cuando se crea una nueva particula,
    unicamente se dispone de informacion sobre su posicion y velocidad
    (normalmente iniciada como cero), el resto de valores no se conocen hasta
    que la particula es evaluada.
    """

    def __init__(self, dimension: int = 2):
        self.p_position = Point(0, 0)
        self.speed = Vector(0, 0)
        self.value: float = 0
        self.p_best_value: float = 0
        self.p_best_position = Point(0, 0)
        self.historial_positions: list = []
        self.initialize: bool = False
        self.dimension = dimension
        self.maximice: bool = False
        self.poco_movimiento: int = 0

    def initialize_particle(self, maximice, dominio):
        """
        Definirle una posicion y velocidad inicial aleatoria
        """
        # Usando list comprehension para generar los randoms
        random_para_V = [random.uniform(-1, 1) for _ in range(self.dimension)]
        random_para_p = [random.uniform(dominio[1], dominio[0])
                         for _ in range(self.dimension)]
        self.speed = Vector(*random_para_V)
        self.p_position = Point(*random_para_p)
        self.initialize: bool = True
        self.maximice = maximice
        self.value = self.calculate_value()

    def calculate_value(self):
        if self.initialize:
            self.historial_positions.append(self.p_position)
            # De ejemplo toca ver como variar la funcion
            self.value = funcion(self.p_position.comp_to_list)
            if self.value < self.p_best_value and not self.maximice:  # minimizar
                self.p_best_value = self.value
                self.p_best_position = self.p_position
            elif self.value > self.p_best_value and self.maximice:  # maximizar
                self.p_best_value = self.value
                self.p_best_position = self.p_position
            return self.value
        else:
            return "hay que inicializar la particula antes"

class Swarm:  # enjambre
    def __init__(self,
                 number_of_particles=0,
                 dominio=None,
                 maximice=False,
                 dimension=2):
        if dominio is None:
            dominio = []
        self.number_of_particles = number_of_particles
        # Para el dominio solo pasamos como si fuera de una variable,
        # pero en verdad seria para ambos ejes, como si fuera un rectangulo
        self.dominio: list = dominio
        self.particulas = [Particle(dimension) for _ in range(number_of_particles)]
        self.maximice = maximice
        if self.maximice:
            self.g_best_value = float("-inf")
        else:
            self.g_best_value = float("inf")
        self.g_best_position = Point(0, 0)  # Inicializa como Point
        self.dimension: int = dimension
        self.w = 0.7
        self.particulas_poco_mov: int = 0

    def inicialize_each_particle(self):  # Falta revisar si funciona
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

    def comprobacion_convergencia_por_poco_movimiento(self):
        """
        Si el 3/4 de particulas presentan poco movimiento sale
        """
        for i in self.particulas:
            if i.poco_movimiento > 3:
                self.particulas_poco_mov += 1
        porcentaje_particulas = (self.particulas_poco_mov /
                                 self.number_of_particles)
        porcentaje_salida = ((self.number_of_particles * 3 / 4) /
                             self.number_of_particles)
        return porcentaje_particulas > porcentaje_salida
    
    def correct_position(self, position):
        """
        Restringe la posicion de la particula al dominio definido.
        """
        if position.x < self.dominio[0] or position.x > self.dominio[1]:
            print(f"el componente x de la posicion se salio del domino "
                  f"por {position.x - self.dominio[1]}")
            position.x = self.dominio[0] / 2
        if position.y < self.dominio[0] or position.y > self.dominio[1]:
            print(f"el componente y de la posicion se salio del domino "
                  f"por {position.y - self.dominio[1]}")
            position.y = (self.dominio[0]) / 2
        return position
    
    def correct_speed(self, speed):
        """
        Restringe la velocidad de la particula al dominio definido.
        """
        speed_limit = (self.dominio[1] - self.dominio[0]) * 0.2
        if speed.x > speed_limit:
            speed.x = 0.5 * (speed_limit)
        elif speed.x < -speed_limit:
            speed.x = -0.5 * (speed_limit)
        if speed.y > speed_limit:
            speed.y = 0.5 * (speed_limit)
        elif speed.y < -speed_limit:
            speed.y = -0.5 * (speed_limit)
        return speed
    
    def update_particles(self, c1, c2, iteraciones):
        """
        Mover una particula implica actualizar su velocidad y posicion.
        Este paso es el mas importante ya que otorga al algoritmo la capacidad
        de optimizar.

        vi(t+1)= wvi(t)+c1r1[**xi(t)- xi(t)]+c2r2[g(t) - xi(t)]

        donde:
        vi(t+1): velocidad de la particula i en el momento t+1, es decir,
                 la nueva velocidad.
        vi(t): velocidad de la particula i en el momento t, es decir,
               la velocidad actual.
        w: coeficiente de inercia, reduce o aumenta a la velocidad de
           la particula.
        c1: coeficiente cognitivo.
        r1: vector de valores aleatorios entre 0 y 1 de longitud igual a la
            del vector velocidad.
        **xi(t): mejor posicion en la que ha estado la particula i hasta
                el momento.
        xi(t): posicion de la particula i en el momento t.
        c2: coeficiente social.
        r2: vector de valores aleatorios entre 0 y 1 de longitud igual a la
            del vector velocidad.
        g(t): posicion de todo el enjambre en el momento t, el mejor valor
              global.
        """
        # Para mas exploracion al inicio y convergencia al final
        if self.w > 0.1:
            decaimiento = 0.7 / iteraciones  # decaimiento inercia
            self.w = self.w - decaimiento  # actualiza la inercia
        else:
            self.w = 0.1 # mantener una inercia minima

        valores_randoms_1 = [random.uniform(0, 1)
                             for _ in range(self.dimension)]
        valores_randoms_2 = [random.uniform(0, 1)
                             for _ in range(self.dimension)]
        r1 = Vector(*valores_randoms_1)
        r2 = Vector(*valores_randoms_2)
        for i in self.particulas:
            # Termino de inercia
            primer_termino = self.w * i.speed
            # Termino cognitivo
            segundo_termino = c1 * r1 * (i.p_best_position - i.p_position)
            # Termino social
            tercer_termino = c2 * r2 * (self.g_best_position - i.p_position)
            # Actualiza la velocidad
            i.speed = primer_termino + segundo_termino + tercer_termino

            # Restringe la velocidad al dominio
            i.speed = self.correct_speed(i.speed)

            # Actualizar la posicion y revisar si hay poco movimiento
            next_position = i.p_position + i.speed
            if abs(next_position - i.p_position) < Point(0.1, 0.1):
                i.poco_movimiento += 1
            elif abs(next_position - i.p_position) > Point(1, 1):
                i.poco_movimiento = 0
            i.p_position = next_position

            # Restringe la posicion al dominio
            i.p_position = self.correct_position(i.p_position)

            # calcula el valor y actualiza las best globales
            i.calculate_value()
            self.update_gbestv_and_gbestpos()     
    def iterations(self, number_iterations, c1, c2):
        """
        iterations grafica y pasa la iteracion, comprobando tambien si sale por
        convergencia
        """
        it = int(number_iterations) #it
        fin = 0
        lista_X = []
        lista_Y = []
        lista_Z = []
        lista_iterations = []
        lista_tiempos = []
        inicio = time.time()
        while number_iterations > 0:
            if self.comprobacion_convergencia_por_poco_movimiento():
                print(f"salida por convergencia")
                break
            self.update_particles(c1, c2, it)
            number_iterations -= 1
            listas_1 = np.array(self.listas_para_david())
            lista_X.append(listas_1[0])
            lista_Y.append(listas_1[1])
            lista_Z.append(listas_1[2])
            lista_iterations.append(it - number_iterations)
            fin = round(time.time() - inicio, 6)
            lista_tiempos.append(fin)
        best_position = round(self.g_best_position, 5)
        best_value = round(self.g_best_value, 5)
        lista_retorno = [lista_X,lista_Y,lista_Z,lista_iterations,lista_tiempos,it]
        print(f"la mejor posicion es {best_position}, "
                     f"con valor de {best_value}")
        return lista_retorno
        
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
    
    def graphs(self, lista):
    
        """ graphs tomará los datos entregados por iterations y los graficara
        si el usuario desea ver la representación gráfica"""
        self.lista = lista
        
        x = np.linspace(self.dominio[0], self.dominio[1], 100)
        y = np.linspace(self.dominio[0], self.dominio[1], 100)
        x, y = np.meshgrid(x, y)  # hace el sistema de coordenadas
        plt.ion()
        fig = plt.figure(figsize=(16, 12))
        # graficar la funcion:
        z = []  # funcion de X,Y aun sin valores
        for k in range(0, len(x), 1):
            z_momentaneo = funcion((x[k], y[k]))
            z.append(z_momentaneo)
        z = np.array(z)
        # grafica #1 de la malla 2x2
        ax = fig.add_subplot(1, 2, 1, projection='3d')
        ax_2 = fig.add_subplot(2, 2, 2)
        ax_2.set_xlim(self.dominio[1])
        ax_2.set_ylim(self.dominio[1])
        ax_3 = fig.add_subplot(3, 2, 6)
        contour = ax_2.contourf(x, y, z, cmap="viridis")
        fig.colorbar(contour, ax=ax_2, shrink=0.5, aspect=5)
        #inicio = time.time()
        for i in range(0, len(self.lista[3]),1):
            
            ax.clear()
            ax_2.clear()
            ax_3.clear()
            ax.plot_surface(x, y, z, cmap='viridis', alpha=0.6)
            ax.set_title(f"grafica 3D de la funcion {str(funcion.__name__)}")

            ax.set_xlabel("eje X")
            ax.set_ylabel("eje Y")
            ax.set_zlabel("Eje Z")

            ax.scatter3D(self.lista[0][i], self.lista[1][i], self.lista[2][i], 
                         c='red', s=100, edgecolor='k', linewidth=1.5)

            # se grafica la vista superior
            contour = ax_2.contourf(x, y, z, cmap="viridis")

            ax_2.set_title("vista superior")

            ax_2.set_xlabel("eje X")
            ax_2.set_ylabel("eje Y")

            ax_2.scatter(self.lista[0][i], self.lista[1][i], c='red', s=100,
                         edgecolor='k', linewidth=1.5)

            ax_3.axis('off')
            iteration_text = (f" Hola, estamos en la iteracion "
                             f"{str(self.lista[3][i])} / {self.lista[5]} \n"
                             f"ha pasado {str(self.lista[4][i])} tiempo ")
            ax_3.set_title(iteration_text)
            plt.pause(1/75)
        plt.ioff()
        plt.show()
        return None