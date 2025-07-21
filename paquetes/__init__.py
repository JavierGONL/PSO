'''
	* Descripción: Paquete PSO - Particle Swarm Optimization
	* documentos relacionados: 
	* autores: kevin javier gonzalez luna, ivan felipe maluche, david Montes
'''

# Importaciones del paquete
from .Enjambre import Swarm, Particle
from .Vector_v2 import Point, Vector
from .Funciones_objetivo import (rastrigin_function, shekel_function,
								himmelblaus_function, sphere_function,
								ackley_function_invertida)

__version__ = "1.0.0"
__author__ = "kevin javier gonzalez luna, ivan felipe maluche, david Montes"