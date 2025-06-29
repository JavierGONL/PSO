'''
    * Descripción: 
    * documentos relacionados: paquetes
    * autores: kevin javier gonzalez luna, ivan felipe maluche, david Montes
'''

class Point: #este es el punto que me robe de la clase shape, tiene un metodo para rehacerlo en tal caso que lo necesitemos
    def __init__(self, x: float = 0, y: float=0, *args):
        if len(args) > 0:
            raise ValueError(f"Point solo acepta 2 componentes, se recibieron: {2 + len(args)}") 
        self.x = x
        self.y = y
        self.comp_to_list: list = [self.x, self.y]

    def redo(self, nx , ny):
        self.x = nx
        self.y = ny

    def __add__(self, v):
        if isinstance(v, Point):
            return Point(float(self.x) + float(v.x), float(self.y) + float(v.y))
        elif isinstance(v, (int, float)):
            return Point(float(self.x) + float(v), float(self.y) + float(v))

    def __radd__(self, p):
        return self.__add__(p)
    
    def __sub__(self, v):
        if isinstance(v, Point):
            return Point(float(self.x) - float(v.x), float(self.y) - float(v.y))
        elif isinstance(v, (int, float)):
            return Point(float(self.x) - float(v), float(self.y) - float(v))
    def __rsub__(self, p):
        return self.__sub__(p)
    
    def __mul__(self, k:float):
        if isinstance(k, (int, float)):
         return Point(k*self.x, k*self.y)
        elif isinstance(k, (Point, Vector)):
            return Point(float(self.x)*float(k.x), float(self.y)*float(k.y))
    
    def __rmul__(self, k):
        return self.__mul__(k)
  
    def __str__(self):
        return (f"({self.x},{self.y})")
    def __round__(self, n=0):
        return Point(round(self.x, n), round(self.y, n))
    def __lt__(self, other):
        if not isinstance(other, (Point, Vector)):
            raise TypeError(f"No se puede comparar con datos del tipo {type(other)}")
        if (self.x**2 + self.y**2)**0.5 < (other.x**2 + other.y**2)**0.5:
            return True
        else:
            return False
    def __le__(self, other):
        if not isinstance(other, (Point, Vector)):
            raise TypeError(f"No se puede comparar con datos del tipo {type(other)}")
        if (self.x**2 + self.y**2)**0.5 <= (other.x**2 + other.y**2)**0.5:
            return True
        else:
            return False
    def __gt__(self, other):
        if not isinstance(other, (Point, Vector)):
            raise TypeError(f"No se puede comparar con datos del tipo {type(other)}")
        if (self.x**2 + self.y**2)**0.5 > (other.x**2 + other.y**2)**0.5:
            return True
        else:
            return False
    def __ge__(self, other):
        if not isinstance(other, (Point, Vector)):
            raise TypeError(f"No se puede comparar con datos del tipo {type(other)}")
        if (self.x**2 + self.y**2)**0.5 >= (other.x**2 + other.y**2)**0.5:
            return True
        else:
            return False
    def __eq__(self, other):
        if not isinstance(other, (Point, Vector)):
            raise TypeError(f"No se puede comparar con datos del tipo {type(other)}")
        return self.x == other.x and self.y == other.y
    def __abs__(self):
        return Point(abs(self.x), abs(self.y))
class Vector(Point):

    def __init__(self, x:float, y:float):
        super().__init__(x,y)
        self.magnitud:float = (x**2 + y**2)**0.5

    def get_direction(self):
            if self.magnitud == 0:
                return Vector(0,0)
            return Vector((self.x/self.magnitud), (self.y/self.magnitud))
    
    def __str__(self):
        return (f"{self.x}i + {self.y}j")
    def __round__(self, n=0):
        return Vector(round(self.x, n), round(self.y, n))
    def __lt__(self, other):
        if not isinstance(other, (Point, Vector)):
            raise TypeError(f"No se puede comparar con datos del tipo {type(other)}")
        if self.magnitud < (other.x**2 + other.y**2)**0.5:
            return True
        else:
            return False
    def __le__(self, other):
        if not isinstance(other, (Point, Vector)):
            raise TypeError(f"No se puede comparar con datos del tipo {type(other)}")
        if self.magnitud <= (other.x**2 + other.y**2)**0.5:
            return True
        else:
            return False
    def __gt__(self, other):
        if not isinstance(other, (Point, Vector)):
            raise TypeError(f"No se puede comparar con datos del tipo {type(other)}")
        if self.magnitud > (other.x**2 + other.y**2)**0.5:
            return True
        else:
            return False
    def __ge__(self, other):
        if not isinstance(other, (Point, Vector)):
            raise TypeError(f"No se puede comparar con datos del tipo {type(other)}")
        if self.magnitud >= (other.x**2 + other.y**2)**0.5:
            return True
        else:
            return False
    def __eq__(self, other):
        if not isinstance(other, (Point, Vector)):
            raise TypeError(f"No se puede comparar con datos del tipo {type(other)}")
        return self.x == other.x and self.y == other.y
    def __abs__(self):
        return Vector(abs(self.x), abs(self.y))