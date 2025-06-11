from Enjambre import *

enjambre = Swarm(50, [-5.12, 5.12],2)
enjambre.inicialize_each_particle()

# for i in enjambre.particulas:
#     print(i.p_position)  
#     print(f"V :{i.speed}")

enjambre.update_particles(0.7, 1.5, 1.5)
    
#* por ahora crea las particulas bien y les da un valor de la funcion bien, 
#* me falta ver la iteracion y comprobar la speed
