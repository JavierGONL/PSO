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

from Enjambre import *

enjambre = Swarm(50, [-5.12, 5.12])
enjambre.inicialize_each_particle()
enjambre.iterations(200, 0.7, 1.5, 1.5) # el problemas es que las particulas se salen del domino

    
#* por ahora crea las particulas bien y les da un valor de la funcion bien, 
#* me falta ver la iteracion y comprobar la speed
"Esta parte del codigo esta generando problemas, no me deja debuggear en el main porque suelta un error"