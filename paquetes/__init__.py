"""
esto es para pruebas
"""

from Enjambre import *

enjambre = Swarm(50, [-5.12, 5.12])
enjambre.inicialize_each_particle()
for i in enjambre.particulas:
    print(i.p_position)