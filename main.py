'''
    * Descripción: 
    * documentos relacionados: paquetes
    * autores: kevin javier gonzalez luna, ivan felipe maluche, david Montes
'''
import tkinter as tk

from paquetes.menu import  MenuPso

def main():
	"""
	Funcion principal que se ejecuta en el main.py
	"""
	root = tk.Tk()
	menu = MenuPso(root)
	# Pantalla completa por defecto
	root.state('zoomed')
	# Iniciar loop principal
	root.mainloop()
	
if __name__ == "__main__":
  main() 