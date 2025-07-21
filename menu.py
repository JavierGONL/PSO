# aqui es donde me arrepiento D:

import time
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import TKinterModernThemes as TKMT
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
		self.funcion_seleccionada = tk.StringVar(value="rastrigin_function")
		self.dominio = None
		self.maximizar_minimizar = tk.BooleanVar(value=True)
		self.particulas = tk.IntVar(value=10)
		self.iteraciones = tk.IntVar(value=100) # esto al final no lo vamos a usar
		self.c1 = tk.IntVar(value=1) # coeficiente cognitivo !acordarse
		self.c2 = tk.IntVar(value=1) # coeficiente social
		self.grabar = tk.BooleanVar(value=False)
		self.ejecutar_pso = tk.BooleanVar(value=True)
		self.crear_interfaz()
    
	def crear_interfaz(self):
		# titulo de la aplicación
		titulo = tk.Label(self.root, text = "PSO",
						  font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#2c3e50')
		titulo.pack(pady=10)  # .pack() organiza el elemento en la ventana con margen vertical
		
		# frame principal
		main_frame = tk.Frame(self.root, bg="#f0f0f0")
		main_frame.pack(fill="both", expand=True, padx=20, pady=10)
		
		# subs frames
		self.seleccionar_funcion(main_frame)
		self.max_min_coeficientes(main_frame)
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
			rb = ttk.Radiobutton(
				frame_funcion, text=descripcion, 
				variable=self.funcion_seleccionada, 
				value=func_name
				)
			rb.pack(anchor="w", pady=2)

	def max_min_coeficientes(self, parent):
		# Frame para parametros optimizacion
		frame_optimizacion_parametros = ttk.LabelFrame(
			parent, text="tipo de Optimizacion y parametros", padding="10"
			)
		frame_optimizacion_parametros.pack(fill="x", padx=20, pady=10)

		# maximizar o minimizar
		info_label_1  = ttk.Label(
			frame_optimizacion_parametros, 
			text="Objetivo optimizacion", 
			font=("Arial", 9), 
			foreground="gray"
			)
		info_label_1.pack(anchor="w", pady=2)
		ttk.Radiobutton( 
			frame_optimizacion_parametros, text="Minimizar", 
			variable=self.maximizar_minimizar,
			value=False).pack(anchor="w", pady=2
			)
		ttk.Radiobutton(
			frame_optimizacion_parametros, 
			text="Maximizar", 
			variable=self.maximizar_minimizar, 
			value=True).pack(anchor="w", pady=2)
		
		# parametros
		info_label_2 = ttk.Label(
			frame_optimizacion_parametros, 
			text="seleccion de parametros optimizacion", 
			font=("Arial", 9), 
			foreground="gray"
			)
		info_label_2.pack(anchor="w", pady=2)

			# Particulas
		frame_iter = tk.Frame(frame_optimizacion_parametros)
		frame_iter.pack(fill="x", padx=10, pady=5)
		tk.Label(frame_iter, text="Particulas:", font=("Arial", 9)).pack(side="left")
		tk.Spinbox(
			frame_iter, from_=10, to=1000,increment=10, width=10, 
			textvariable=self.particulas).pack(side="right")
		
			# Iteraciones
		frame_iter = tk.Frame(frame_optimizacion_parametros)
		frame_iter.pack(fill="x", padx=10, pady=5)
		tk.Label(frame_iter, text="Iteraciones:", font=("Arial", 9)).pack(side="left")
		tk.Spinbox(
			frame_iter, from_=100, to=1000,increment=10, width=10, 
			textvariable=self.iteraciones).pack(side="right")
		
			# C1
		frame_c1 = tk.Frame(frame_optimizacion_parametros)
		frame_c1.pack(fill="x", padx=10, pady=5)
		tk.Label(frame_c1, text="C1 (cognitivo):", font=("Arial",9)).pack(side="left")
		tk.Spinbox(
			frame_c1, from_=0.1, to=5.0, increment=0.1, width=10, 
			textvariable=self.c1, format="%.1f").pack(side="right")
		
			# C2
		frame_c2 = tk.Frame(frame_optimizacion_parametros)
		frame_c2.pack(fill="x", padx=10, pady=5)
		tk.Label(frame_c2, text="C2 (social):", font=("Arial", 9)).pack(side="left")

		tk.Spinbox(
			frame_c2, from_=0.1, to=5.0, increment=0.1, width=10, 
			textvariable=self.c2, format="%.1f").pack(side="right")
		
		# Grabar
		info_label_3 = ttk.Label(
			frame_optimizacion_parametros, 
			text="Desea grabar?", 
			font=("Arial", 9), 
			foreground="gray"
			)
		info_label_3.pack(anchor="w", pady=2)
		ttk.Checkbutton(
			frame_optimizacion_parametros, text="grabar", 
			variable=self.grabar).pack(anchor="w", pady=5)

	def ejecutar_boton(self, parent):
		"""
		Crea botón de ejecutar y muestra valores seleccionados
		"""
		frame_botones = tk.Frame(parent)
		frame_botones.pack(fill="x", padx=20, pady=20)
		
		# Botón ejecutar
		boton_ejecutar = tk.Button(
			frame_botones, 
			text="Ejecutar PSO", 
			command=self.ejecutar_pso, 
			bg="#4CAF50", fg="white", 
			font=("Arial", 10, "bold")
			)
		boton_ejecutar.pack(side="left", padx=5)
		

def main():
	"""
	Función principal que lanza la GUI
	"""
	root = tk.Tk()
	menu = MenuPso(root)
	
	# Centrar ventana
	root.update_idletasks()
	x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
	y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
	root.geometry(f"+{x}+{y}")
	
	# Iniciar loop principal
	root.mainloop()
	print(menu.funcion_seleccionada.get())
if __name__ == "__main__":
	main()
