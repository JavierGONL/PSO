class Point: 
    #! tuve que hacer un monton de cosas raras aca, usar copilot :(
    #!  2 horas buscando una solucion por mi mismo
    #! y resulta que el malp python cuando hace un (escalar * un vector)
    #! es diferente que un (vector * un escalar) y segun cada caso invoca o __mul__ o __rmul__ :/ 
    #! y pasa lo mismo con la hpta suma y resta.
    #! yo solo iba a agregar un clase punto re basica para hacer pruebas y nop dos horas arreglando esta cosa JAJAJAJAJAJA, :[

    def __init__(self, x: float, y: float, *args):
        if len(args) > 0:
            raise ValueError(f"Point solo acepta 2 componentes, se recibieron: {2 + len(args)}")
        self.x = x
        self.y = y
        self.comp_to_list = [self.x, self.y]

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(float(self.x) + float(other.x), float(self.y) + float(other.y))
        elif isinstance(other, (int, float)):
            return Point(float(self.x) + other, float(self.y) + other)
        else:
            raise TypeError(f"No se puede sumar Point con {type(other)}")

    def __radd__(self, p):
        return self.__add__(p)

    def __sub__(self, p):
        # Devuelve un Vector con la diferencia de componentes
        return Vector(float(self.x) - float(p.x), float(self.y) - float(p.y))
    
    def __rsub__(self, p):
        return self.__sub__(p)

    def __mul__(self, k):
        if not isinstance(k, (int, float)):
            raise TypeError(f"Solo se puede multiplicar Point por un escalar, no por {type(k)}")
        return Point(float(self.x) * float(k), float(self.y) * float(k))

    def __rmul__(self, k):
        return self.__mul__(k)

    def __str__(self):
        return f"{self.x},{ self.y}"

    def __pow__(self, k):
        if isinstance(k, (int, float)):
            return Point(self.x ** k, self.y ** k)
        raise TypeError(f"No se puede elevar Point a {type(k)}")


class Vector(Point):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        self.magnitud: float = self.calculate_magnitude()

    def calculate_magnitude(self):
        return (self.x**2 + self.y**2)**0.5

    def get_direction(self):
        if self.magnitud == 0:
            return Vector(0.0, 0.0, 0.0)
        return Vector((self.x / self.magnitud), (self.y / self.magnitud))

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(float(self.x) + float(other.x), float(self.y) + float(other.y))
        raise TypeError(f"No se puede sumar Vector con {type(other)}")

    def __rsub__(self, p):
        return self.__sub__(p)

    def __sub__(self, p):
        return Vector(float(self.x) - float(p.x), float(self.y) - float(p.y))

    def __mul__(self, k):
        if isinstance(k, (int, float)):
            return Vector(float(self.x) * float(k), float(self.y) * float(k))
        elif isinstance(k, Vector):
            return Vector(float(self.x) * float(k.x), float(self.y) * float(k.y))
        raise TypeError(f"Solo se puede multiplicar Vector por un escalar o por otro Vector, no por {type(k)}")

    def __pow__(self, k):
        if isinstance(k, (int, float)):
            return Vector(self.x ** k, self.y ** k)
        raise TypeError(f"No se puede elevar Vector a {type(k)}")
