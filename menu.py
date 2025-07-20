# aqui es donde me arrepiento D:

import time
import tkinter as tk
from tkinter import ttk, messagebox
import threading
from paquetes.Funciones_objetivo import (rastrigin_function, shekel_function,
                                        himmelblaus_function, sphere_function,
                                        ackley_function_invertida)

class MenuPso:
	def __init__(self,root):
		# Crear la ventana principal
		self.root = root

		# funciones
		self.funciones = {
			"rastrigin_function": (rastrigin_function, [-5.12, 5.12]),
			"shekel_function": (shekel_function, [0, 10]),
			"himmelblaus_function": (himmelblaus_function, [-5, 5]),
			"sphere_function": (sphere_function, [-5, 5]),
			"ackley_function_invertida": (ackley_function_invertida, [-5, 5])
		}
		# opciones a colocar en la interfaz
		self.funcion_seleccionada = None
		self.dominio = None
		self.maximizar_minimizar = False
		self.particulas = 50
		self.iteraciones = 200 # esto al final no lo vamos a usar
		self.c1 = 2.0 # coeficiente cognitivo !acordarse
		self.c2 = 1.0 # coeficiente social
		self.grabar = True
		self.crear_interfaz()
    
	def crear_interfaz(self):
		# titulo de la aplicación
		titulo = tk.Label(self.root, text = "PSO",
						  font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#2c3e50')
		titulo.pack(pady=10)  # .pack() organiza el elemento en la ventana con margen vertical
		
		# CONTENEDOR PRINCIPAL
		main_frame = tk.Frame(self.root, bg="#242222")
		main_frame.pack(fill="both", expand=True, padx=20, pady=10)
		
		self.seleccionar_funcion(main_frame)
		
		self.max_min_coeficientes(main_frame)

		self.record_boton(main_frame)

		self.ejecutar_boton(main_frame)

	def seleccionar_funcion(self,parent):
		# Frame para función objetivo
		frame_funcion = ttk.LabelFrame(parent, text="Funcion Objetivo", padding="10")
		frame_funcion.pack(fill="x", padx=20, pady=10)
		
		funciones_info = {
			"rastrigin_function": "Rastrigin - la funcion que menos consume si se quere grabar",
			"shekel_function": "Shekel - funcion con multiples minimos",
			"himmelblaus_function": "Himmelblaus - otra funcion con multiples minimos",
			"sphere_function": "Sphere - idk, esta de mas",
			"ackley_function_invertida": "Ackley invertida - para probar la maximizacion"
		}

		for func_name, descripcion in funciones_info.items():
			rb = ttk.Radiobutton(frame_funcion, text=descripcion, 
								variable=self.funcion_seleccionada, value=func_name)
			rb.pack(anchor="w", pady=2)

	def max_min_coeficientes(self, parent):
		# Frame para parametros optimizacion
		frame_optimizacion_parametros = ttk.LabelFrame(parent, text="ipo de Optimizacion y parametros", padding="10")
		frame_optimizacion_parametros.pack(fill="x", padx=20, pady=10)
		
		# maximizar o minimizar
		ttk.Radiobutton(frame_optimizacion_parametros, text="Minimizar", 
						variable=self.funcion_seleccionada, value="minimizar").pack(anchor="w", pady=2)
		ttk.Radiobutton(frame_optimizacion_parametros, text="Maximizar", 
						variable=self.funcion_seleccionada, value="maximizar").pack(anchor="w", pady=2)
		
		# Numero de iteraciones
		frame_iter = ttk.Frame(frame_optimizacion_parametros)
		frame_iter.pack(fill="x", pady=5)
		ttk.Label(frame_iter, text="🔄 Número de iteraciones:").pack(side="left")
		spinbox_iter = tk.Spinbox(frame_iter, from_=50, to=1000, width=10, 
								 textvariable=self.funcion_seleccionada)
		spinbox_iter.pack(side="right")
		
		# Coeficientes
		frame_c1 = ttk.Frame(frame_optimizacion_parametros)
		frame_c1.pack(fill="x", pady=5)
		ttk.Label(frame_c1, text="Coeficiente cognitivo (c1):").pack(side="left")
		spinbox_c1 = tk.Spinbox(frame_c1, from_=1, to=2.0, increment=0.1, 
							   width=10, textvariable=self.c1, format="%.1f")
		spinbox_c1.pack(side="right")

		frame_c2 = ttk.Frame(frame_optimizacion_parametros)
		frame_c2.pack(fill="x", pady=5)
		ttk.Label(frame_c2, text="Coeficiente social (c2):").pack(side="left")
		spinbox_c2 = tk.Spinbox(frame_c2, from_=1 , to=2.0, increment=0.1, 
							   width=10, textvariable=self.c2, format="%.1f")
		spinbox_c2.pack(side="right")

	def record_boton(self, parent):
		pass

	def ejecutar_boton(self, parent):
		pass

def main():
	"""Función principal que lanza la GUI"""
	root = tk.Tk()
	root.title("PSO")
	# Configurar estilo
	style = ttk.Style()
	style.theme_use('clam')  # Tema moderno
	
	# Crear aplicación
	app = MenuPso(root)
	
	# Centrar ventana
	root.update_idletasks()
	x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
	y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
	root.geometry(f"+{x}+{y}")
	
	# Iniciar loop principal
	root.mainloop()

if __name__ == "__main__":
	main()
