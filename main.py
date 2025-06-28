'''
    * Descripción: 
    * documentos relacionados: paquetes
    * autores: kevin javier gonzalez luna, ivan felipe maluche, david Montes
'''
from paquetes.Enjambre import Swarm

enjambre = Swarm(100, [-5.12, 5.12], True)
enjambre.inicialize_each_particle()
enjambre.iterations(20, 2, 1.5)
