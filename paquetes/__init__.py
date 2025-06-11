from Enjambre import *

enjambre = Swarm(50, [-5.12, 5.12])
enjambre.inicialize_each_particle()
enjambre.update_particles(0.7, 1.5, 1.5)
for i in enjambre.particulas:
    print(i.value)
