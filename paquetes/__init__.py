#from Enjambre import *

enjambre = Swarm(50, [-5.12, 5.12])
enjambre.inicialize_each_particle()
enjambre.update_particles(0.7, 1.5, 1.5)
for i in enjambre.particulas:
    print(i.value) 
    
#* por ahora crea las particulas bien y les da un valor de la funcion bien, 
#* me falta ver la iteracion y comprobar la speed
"Esta parte del codigo esta generando problemas, no me deja debuggear en el main porque suelta un error"