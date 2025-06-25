'''
    * Descripción: 
    * documentos relacionados: paquetes
    * autores: kevin javier gonzalez luna, ivan felipe maluche, david Montes
    * --------------------------------- TODO -------------------------------------------------
    * Lista de feature por hacer:
    * - que funcione con prueba vector
    *
    * --------------------------------- ISSUES -----------------------------------------------
    * Lista de problemas conocidos:
    * - prueba vector no sirve como con vector
    *
    * ----------------------------------------------------------------------------------------
'''

from paquetes.Enjambre import Swarm

enjambre = Swarm(100, [-5.12, 5.12],True)
enjambre.inicialize_each_particle()
enjambre.iterations(25, 1.5, 1.5) # el problemas es que las particulas se salen del domino
