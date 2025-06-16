'''
    * Descripción: 
    * documentos relacionados: paquetes
    * autores: kevin javier gonzalez luna, ivan felipe maluche, david Montes
    * --------------------------------- TODO -------------------------------------------------
    * Lista de feature por hacer:
    * - 
    *
    * --------------------------------- ISSUES -----------------------------------------------
    * Lista de problemas conocidos:
    * - 
    *
    * ----------------------------------------------------------------------------------------
'''

class Point: #este es el punto que me robe de la clase shape, tiene un metodo para rehacerlo en tal caso que lo necesitemos
    def __init__(self, x: float = 0, y: float=0, z:float=0, *args):
        if len(args) > 0:
            raise ValueError(f"Point solo acepta 3 componentes, se recibieron: {3 + len(args)}") 
        self.x = x
        self.y = y
        self.z = z
        self.comp_to_list: list = [self.x, self.y, self.z]

    def redo(self, nx , ny, nz):
        self.x = nx
        self.y = ny
        self.z = nz

    def __add__(self, v):
        if isinstance(v, Point):
            return Point(float(self.x) + float(v.x), float(self.y) + float(v.y), float(self.z) + float(v.z))
        elif isinstance(v, (int, float)):
            return Point(float(self.x) + float(v), float(self.y) + float(v), float(self.z) + float(v))

    def __radd__(self, p):
        return self.__add__(p)
    
    def __sub__(self, v):
        if isinstance(v, Point):
            return Point(float(self.x) - float(v.x), float(self.y) - float(v.y), float(self.z) - float(v.z))
        elif isinstance(v, (int, float)):
            return Point(float(self.x) - float(v), float(self.y) - float(v), float(self.z) - float(v))
    def __rsub__(self, p):
        return self.__sub__(p)
    
    def __mul__(self, k:float):
        if isinstance(k, (int, float)):
         return Point(k*self.x, k*self.y, k*self.z)
        elif isinstance(k, (Point, Vector)):
            return Point(float(self.x)*float(k.x), float(self.y)*float(k.y), float(self.z)*float(k.z))
    
    def __rmul__(self, k):
        return self.__mul__(k)
  
    def __str__(self):
        return (f"({self.x},{self.y},{self.z})")
    def __round__(self, n=0):
        return Point(round(self.x, n), round(self.y, n), round(self.z, n))
  
class Vector(Point):

    def __init__(self, x:float, y:float, z:float = 0):
        super().__init__(x,y,z)
        self.magnitud:float = (x**2 + y**2 + z**2)**0.5

    def get_direction(self):
            if self.magnitud == 0:
                return Vector(0,0,0)
            return Vector((self.x/self.magnitud), (self.y/self.magnitud), (self.z/self.magnitud))
    
    def __str__(self):
        return (f"{self.x}i + {self.y}j + {self.z}k")
    def __round__(self, n=0):
        return Vector(round(self.x, n), round(self.y, n), round(self.z, n))

print(type(Vector(1,2,3).x))