'''
    * Descripción: 
    * documentos relacionados: paquetes
    * autores: kevin javier gonzalez luna, ivan felipe maluche, david Montes
'''
import time
from paquetes.Enjambre import Swarm

inicio_programa = time.time()
enjambre = Swarm(50, [-5.12, 5.12], maximice= False)
enjambre.inicialize_each_particle()
listillas = list(enjambre.iterations(200, 2, 1))
enjambre.graphs(listillas, True, inicio_programa)  # Corregido: record=True, luego tiempo