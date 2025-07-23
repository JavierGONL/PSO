'''
    * Descripcion: clase particula y enjambre
    * documentos relacionados:  
    * autores: kevin javier gonzalez luna, ivan felipe maluche, david Montes
'''
import random
import time
import os
import cv2
from paquetes.Funciones_objetivo import (rastrigin_function, shekel_function,
                                        himmelblaus_function, sphere_function,
                                        ackley_function_invertida
                                        )
from paquetes.Vector_v2 import Point, Vector

import numpy as np
import matplotlib.pyplot as plt

class Particle:  # particula
	"""
	Cada particula esta definida por una posicion,
	velocidad y valor que varian a medida que la particula se mueve.
	Ademas, tambien almacena la mejor posicion en la que ha estado hasta
	el momento. Cuando se crea una nueva particula,
	unicamente se dispone de informacion sobre su posicion y velocidad
	(normalmente iniciada como cero), el resto de valores no se conocen hasta
	que la particula es evaluada.
	"""
	def __init__(self, dimension: int = 2):
		self.p_position = Point(0, 0)
		self.speed = Vector(0, 0)
		self.value: float = 0
		self.p_best_value: float = None  # Cambiado a None para detectar primera evaluación
		self.p_best_position = Point(0, 0)
		self.historial_positions: list = [] # por si acaso
		self.initialize: bool = False
		self.dimension = dimension
		self.maximice: bool = False
		self.poco_movimiento: int = 0

	def initialize_particle(self, maximice, dominio, funcion):
		"""
		Definirle una posicion y velocidad inicial aleatoria 
		"""
		# Usando list comprehension para generar los randoms
		random_para_V = [random.uniform(-1, 1) for _ in range(self.dimension)]
		random_para_p = [
			random.uniform(dominio[0], dominio[1]) for _ in range(self.dimension)
		]
		self.speed = Vector(*random_para_V)
		self.p_position = Point(*random_para_p)
		self.initialize: bool = True
		self.maximice = maximice
		self.value = self.calculate_value(funcion)

	def calculate_value(self, funcion):
		"""
		calcula el valor de la funcion aplicado en la posicion actual 
		y lo compara con el mejor valor, dependiendo de lo que se desee 
		se actualizara la mejor posicion
		"""
		if self.initialize:
			self.historial_positions.append(self.p_position)
			self.value = funcion(self.p_position.comp_to_list)
			
			# Si es la primera vez que se calcula se asigna como mejor valor
			if self.p_best_value is None:  # Para cuando se ejecute por primera vez, si no va a joder en algun momento por algo que aun no se que fue :#
				self.p_best_value = self.value
				self.p_best_position = self.p_position
			elif self.value < self.p_best_value and not self.maximice:  # minimizar
				self.p_best_value = self.value
				self.p_best_position = self.p_position
			elif self.value > self.p_best_value and self.maximice:  # maximizar
				self.p_best_value = self.value
				self.p_best_position = self.p_position
			return self.value
		else:
			return "hay que inicializar la particula antes"

class Swarm:
	def __init__(
			self,
			number_of_particles:int,
			dominio:list,
			maximice:bool =False,
			dimension:int=2,
			funcion = None
			):
		self.number_of_particles = number_of_particles
		# Para el dominio solo pasamos como si fuera de una variable,
		# pero en verdad seria para ambos ejes, como si fuera un rectangulo
		self.dominio: list = dominio
		self.particulas = [Particle(dimension) for _ in range(number_of_particles)]
		self.maximice = maximice
		if self.maximice:
			self.g_best_value = float("-inf")
		else:
			self.g_best_value = float("inf")
		self.g_best_position = Point(0, 0)  # Inicializa como Point
		self.dimension: int = dimension
		self.w = 0.7
		self.particulas_poco_mov: int = 0
		self.funcion = funcion

	def inicialize_each_particle(self):  # Falta revisar si funciona
		for i in self.particulas:
			i.initialize_particle(self.maximice, self.dominio, self.funcion)

	def update_gbestv_and_gbestpos(self):
		"""
		revisa en cada particula si su valor es mejor que el global
		y lo actualiza si es necesario
		"""
		for i in self.particulas:
			if i.value < self.g_best_value and not self.maximice:
				self.g_best_value = i.value
				self.g_best_position = i.p_position
			elif i.value > self.g_best_value and self.maximice:
				self.g_best_value = i.value
				self.g_best_position = i.p_position

	def comprobacion_convergencia_por_poco_movimiento(self):
		"""
		Si el 3/4 de particulas en la iteracion presentan poco movimiento sale
		"""
		self.particulas_poco_mov = 0
		for i in self.particulas:
			if i.poco_movimiento > 3:
				self.particulas_poco_mov += 1
		porcentaje_particulas = (self.particulas_poco_mov /
								self.number_of_particles)
		porcentaje_salida = ((self.number_of_particles * 3 / 4) /
							self.number_of_particles)
		return porcentaje_particulas > porcentaje_salida
	
	def correct_position(self, position):
		"""
		Restringe la posicion de la particula al dominio definido.
		"""
		if position.x < self.dominio[0] or position.x > self.dominio[1]:
			print(f"el componente x de la posicion se salio del domino "
				  f"por {position.x - self.dominio[1]}")
			position.x = self.dominio[0] / 2
		if position.y < self.dominio[0] or position.y > self.dominio[1]:
			print(f"el componente y de la posicion se salio del domino "
				  f"por {position.y - self.dominio[1]}")
			position.y = (self.dominio[0]) / 2
		return position
	
	def limit_speed(self, speed):
		"""
		Restringe la velocidad de la particula al dominio definido.
		"""
		speed_limit = (self.dominio[1] - self.dominio[0]) * 0.4
		if speed.x > speed_limit:
			speed.x = 0.5 * (speed_limit)
		elif speed.x < -speed_limit:
			speed.x = -0.5 * (speed_limit)
		if speed.y > speed_limit:
			speed.y = 0.5 * (speed_limit)
		elif speed.y < -speed_limit:
			speed.y = -0.5 * (speed_limit)
		return speed
	
	def update_particles(self, c1, c2, iteraciones):
		"""
		Mover una particula implica actualizar su velocidad y posicion.
		Este paso es el mas importante ya que otorga al algoritmo la capacidad
		de optimizar.

		vi(t+1) = wvi(t) + 1r1[**xi(t) - xi(t)] + c2r2[g(t) - xi(t)]

		donde:
		vi(t+1): velocidad de la particula i en el momento t+1, es decir,
				 		 la nueva velocidad.
		vi(t): velocidad de la particula i en el momento t, es decir,
			   	 la velocidad actual.
		w: coeficiente de inercia, reduce o aumenta a la velocidad de
		   la particula.
		c1: coeficiente cognitivo.
		r1: vector de valores aleatorios entre 0 y 1 de longitud igual a la
				del vector velocidad.
		**xi(t): mejor posicion en la que ha estado la particula i hasta
						el momento.
		xi(t): posicion de la particula i en el momento t.
					 c2: coeficiente social.
		r2: vector de valores aleatorios entre 0 y 1 de longitud igual a la
				del vector velocidad.
		g(t): posicion de todo el enjambre en el momento t, el mejor valor
			  global.
		"""
		# Para mas exploracion al inicio y convergencia al final
		if self.w > 0.1:
			decaimiento = 1 / iteraciones  # decaimiento inercia
			self.w = self.w - decaimiento  # actualiza la inercia
		else:
			self.w = 0.1 # mantener una inercia minima

		valores_randoms_1 = [
			random.uniform(0, 1) for _ in range(self.dimension)]
		valores_randoms_2 = [
			random.uniform(0, 1) for _ in range(self.dimension)
			]
		r1 = Vector(*valores_randoms_1) 
		r2 = Vector(*valores_randoms_2)
		for i in self.particulas:
			# Termino de inercia
			primer_termino = self.w * i.speed
			# Termino cognitivo
			segundo_termino = c1 * r1 * (i.p_best_position - i.p_position)
			# Termino social
			tercer_termino = c2 * r2 * (self.g_best_position - i.p_position)
			# Actualiza la velocidad
			i.speed = primer_termino + segundo_termino + tercer_termino

			# Restringe la velocidad al dominio
			i.speed = self.limit_speed(i.speed)

			# Actualizar la posicion y revisar si hay poco movimiento
			next_position = i.p_position + i.speed
			if abs(next_position - i.p_position) < Point(0.1, 0.1):
				i.poco_movimiento += 1
			elif abs(next_position - i.p_position) > Point(1, 1):
				i.poco_movimiento = 0
			i.p_position = next_position

			# Restringe la posicion al dominio
			i.p_position = self.correct_position(i.p_position)

			# calcula el valor y actualiza las best globales
			i.calculate_value(self.funcion)
			self.update_gbestv_and_gbestpos()     

	def iterations(self, number_iterations, c1, c2):
		"""
		iterations toma los datos de la iteracion actual, lo pasa a graphs
		y pasa la iteracion, esto comprobando tambien si sale por convergencia
		"""
		it = int(number_iterations) #it
		fin = 0
		lista_X = []
		lista_Y = []
		lista_Z = []
		lista_iterations = []
		lista_tiempos = []
		lista_mejores_posiciones = []
		lista_mejores_valores = []
		inicio = time.time()
		while number_iterations > 0:
			if self.comprobacion_convergencia_por_poco_movimiento():
				print(f"salida por convergencia")
				break
			self.update_particles(c1, c2, it)
			number_iterations -= 1
			listas_1 = np.array(self.listas_para_david())
			lista_X.append(np.array(listas_1[0]))
			lista_Y.append(np.array(listas_1[1]))
			lista_Z.append(np.array(listas_1[2]))
			lista_iterations.append(it - number_iterations)
			lista_mejores_posiciones.append(round(self.g_best_position,7))
			lista_mejores_valores.append(round(self.g_best_value,7))
			fin = round(time.time() - inicio, 6)
			lista_tiempos.append(fin)
			# print(lista_mejores_posiciones)
		best_position = round(self.g_best_position, 5)
		best_value = round(self.g_best_value, 5)
		lista_retorno = [
			np.array(lista_X), 
			np.array(lista_Y),
			np.array(lista_Z),
			np.array(lista_iterations),
			np.array(lista_tiempos),
			it,
			np.array(lista_mejores_posiciones),
			np.array(lista_mejores_valores),
			best_position,
			best_value
			]
		print(f"la mejor posicion es:\n{best_position}\nvalor: {best_value}")
		return lista_retorno
        
	def listas_para_david(self):
		lista_x = []
		lista_y = []
		lista_z = []
		lista_de_listas = []
		for i in self.particulas:
			lista_x.append(i.p_position.x)
			lista_y.append(i.p_position.y)
			lista_z.append(i.value)
		lista_de_listas.append(lista_x)
		lista_de_listas.append(lista_y)
		lista_de_listas.append(lista_z)
		return lista_de_listas
	
	def graphs(self, lista, record:bool, tiempo_inicio_programa=None):
		""" 
		graphs toma los datos entregados por iterations y los grafica con su telemetria
		"""
		self.lista = lista
		self.tiempo_inicio_programa = tiempo_inicio_programa
		self.record = record
		actual_images = os.listdir("images_temp") #lista con los nombres de las imágenes
		#se borran las imagenes existentes en la carpeta images
		for i in actual_images:
			os.remove(f"images_temp/{i}")
		# resolucion
		# linspace de numpy crea un arreglo de n datos a distancia uniforme entre los límites del dominio
		x = np.linspace(self.dominio[0], self.dominio[1], 60) 
		y = np.linspace(self.dominio[0], self.dominio[1], 60)
		x, y = np.meshgrid(x, y)  # hace el sistema de coordenadas
		plt.ion()
		fig = plt.figure(figsize=(16, 12)) # definición inicial tamaño ventana

		# Pantalla completa en Windows
		figManager = plt.get_current_fig_manager()
		try:
			figManager.window.state('zoomed')
		except Exception:
			pass  # Si no esta en Windows o no funciona lo ignora

		z = self.funcion((x, y))  # Calculo vectorizado de la función

		ax = fig.add_subplot(1, 2, 1, projection='3d')
		ax_2 = fig.add_subplot(2, 2, 2)
		ax_2.set_xlim(self.dominio[0], self.dominio[1])
		ax_2.set_ylim(self.dominio[0], self.dominio[1])
		ax_3 = fig.add_subplot(8, 2, 16)
		
		# titulos ejes
		ax.set_xlabel("eje X")
		ax.set_ylabel("eje Y")
		ax.set_zlabel("Eje Z")
		ax_2.set_xlabel("eje X")
		ax_2.set_ylabel("eje Y")
		ax_3.axis('off')
		
		for i in range(0, len(self.lista[3]),1):
			ax.clear()
			ax_2.clear()
			ax_3.clear()
			
			# Superficie 3D
			ax.plot_surface(x, y, z, cmap='viridis', alpha=0.6)
			ax.set_title(f"grafica 3D de la funcion {str(self.funcion.__name__)}")
			ax.set_xlabel("eje X")  # Necesario después de clear()
			ax.set_ylabel("eje Y")
			ax.set_zlabel("Eje Z")

			ax.scatter3D(
				self.lista[0][i], self.lista[1][i], self.lista[2][i], 
				c='red', s=50, edgecolor='k', linewidth=1.5
				)
			
			# Recrear el mapa de calor en cada iteración
			contour = ax_2.contourf(x, y, z, cmap="viridis", levels=20)
			ax_2.set_title("Mapa de Temperatura - Vista Superior")
			ax_2.set_xlabel("eje X")
			ax_2.set_ylabel("eje Y")
			ax_2.set_xlim(self.dominio[0], self.dominio[1])
			ax_2.set_ylim(self.dominio[0], self.dominio[1])

			ax_2.scatter(
				self.lista[0][i], self.lista[1][i], 
				c='red', s=50, edgecolor='black', linewidth=1.5
				)
			tiempo_programa_actual = time.time() - self.tiempo_inicio_programa
			# telemetria de cada iteracion
			telemetria = (
				f"Iteracion: {self.lista[3][i]} \n "
				f"Tiempo de ejecución total del programa: {tiempo_programa_actual:.2f}s \n"
				f"Tiempo ejecución PSO: {self.lista[4][i]} s \n "
				f"Mejor posicion actual: \nX: {self.lista[6][i].x:.4f}\nY: {self.lista[6][i].y:.4f}"
				f"\nValor: {self.lista[7][i]:.5f}"
			)
			ax_3.set_title(telemetria)
			ax_3.axis('off')
			iteration_actual = self.lista[3][i]
			plt.pause(1/5000)
			if self.record == True:
				plt.savefig(f"images_temp/{self.lista[3][i]}",dpi=150, bbox_inches='tight')
			else: 
				pass
			
		if iteration_actual != self.lista[5]: # telemetria final
			ax_3.clear()
			ax_3.axis('off')
			tiempo_total_programa = time.time() - self.tiempo_inicio_programa
			telemetria_final = (
				f"El programa acabo en la iteracion {iteration_actual}\n"
				f"Tiempo Total de ejecucion: {tiempo_total_programa:.2f}s\n"
        f"Tiempo ejecución final PSO: {self.lista[4][i]} s \n "
				f"mejor posición: \nX: {self.lista[8].x:.4f}\nY: {self.lista[8].y:.4f}"
				f"\nvalor: {self.lista[9]:.4f}"
				)
			ax_3.set_title(telemetria_final)
			plt.savefig(f"images_temp/{self.lista[3][i]}",dpi=150, bbox_inches='tight')
		
		plt.ioff()
		plt.show()
		if self.record == True: #aquí se renderiza el video
			# Obtener lista actualizada de imágenes después de guardar todas
			updated_images = os.listdir("images_temp")
			# Ordenar numéricamente en lugar de alfabéticamente 
   			# #esto definitivamente lo hizo copilot
			updated_images.sort(key=lambda x: int(x.split('.')[0]))
			
			images_path = []
			for i in updated_images:
				images_path.append(f"images_temp/{i}")
			num_frames = len(images_path)
			fps_dinamico = len(images_path)/10 #asegura una cantidad de FPS acorde a la cantidad de frames
			print(f"Creando video con {num_frames} frames a {fps_dinamico:.2f} ")
			print(f"Orden de frames: {[img.split('/')[-1] for img in images_path[:5]]}...")  # Mostrar primeros 5
			
			try: 
				str_ultimo_video = os.listdir("videos")[-1]
				nombre_ultimo_video = int(str_ultimo_video[:-4]) #esto borra el .mp4 del nombre del archivo.
			except IndexError: nombre_ultimo_video = 0 #esto evita errores si la lista está vacía
			video_name = nombre_ultimo_video + 1
			cv2_fourcc = cv2.VideoWriter_fourcc(*"mp4v")
			frame = cv2.imread(images_path[0])
			size = list(frame.shape)
			del size[2]
			size.reverse()
			video = cv2.VideoWriter(
				f"videos/{video_name}.mp4", cv2_fourcc,
        fps_dinamico, size
				)
			for i in range(0,len(images_path),1):
				video.write(cv2.imread(images_path[i]))
				print(f"frame {i+1} de {len(images_path)}")
			video.release()
			print(f"Video guardado: videos/{video_name}.mp4")