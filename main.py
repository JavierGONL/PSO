'''
    * Descripción: 
    * documentos relacionados: paquetes
    * autores: kevin javier gonzalez luna, ivan felipe maluche, david Montes
'''
from paquetes.Enjambre import Swarm

enjambre = Swarm(100, [-5.12, 5.12], maximice= True)
enjambre.inicialize_each_particle()
listillas = list(enjambre.iterations(100, 1.5, 2))
enjambre.graphs(listillas)
