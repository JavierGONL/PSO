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
    * - speed devuelve 4 componentes, deben ser 2
    *
    * ----------------------------------------------------------------------------------------
'''

from Enjambre import *

enjambre = Swarm(50, [-5.12, 5.12])
enjambre.inicialize_each_particle()
for i in enjambre.particulas:
    print(f"P: {i.speed},   V: {i.speed}, Value: {i.value}")
    break

enjambre.update_particles(0.7, 1.5, 1.5)

for i in enjambre.particulas:
    print(f"P: {i.speed},   V: {i.speed}, Value: {i.value}")
    break

enjambre.update_particles(0.7, 1.5, 1.5)

for i in enjambre.particulas:
    print(f"P: {i.speed},   V: {i.speed}, Value: {i.value}")
    break
    
#* por ahora crea las particulas bien y les da un valor de la funcion bien, 
#* me falta ver la iteracion y comprobar la speed
"Esta parte del codigo esta generando problemas, no me deja debuggear en el main porque suelta un error"