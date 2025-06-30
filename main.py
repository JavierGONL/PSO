'''
    * Descripción: 
    * documentos relacionados: paquetes
    * autores: kevin javier gonzalez luna, ivan felipe maluche, david Montes
'''
from paquetes.Enjambre import Swarm

enjambre = Swarm(10, [-5.12, 5.12])
enjambre.inicialize_each_particle()
listillas = enjambre.iterations(20, 2, 1.5)
#enjambre.graphs()
print(listillas)
print(listillas)