class Point: #a

    def __init__(self, x: float, y: float, *args):
        if len(args) > 0:
            raise ValueError(f"Point solo acepta 2 componentes, se recibieron: {2 + len(args)}")
        self.x = x
        self.y = y
        self.comp_to_list : list = [self.x, self.y]

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

    def __mul__(self , k):
        if not isinstance(k, (int, float)):
            raise TypeError(f"Solo se puede multiplicar Point por un escalar, no por {type(k)}")
        return Point(float(self.x) * float(k), float(self.y) * float(k))

    def __rmul__(self, k):
        return self.__mul__(k)

    def __str__(self):
        return f"{self.x},{ self.y}"
    
    def __round__(self, n=0):
        return Point(round(self.x, n), round(self.y, n))

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
            if len(self.comp_to_list) != len(other.comp_to_list):
                raise ValueError("Dimensiones incompatibles para suma de vectores")
            return Vector(*(float(x) + float(y) for x, y in zip(self.comp_to_list, other.comp_to_list)))
        raise TypeError(f"No se puede sumar Vector con {type(other)}")

    def __rsub__(self, p):
        return self.__sub__(p)

    def __sub__(self, other):
        if isinstance(other, Vector):
            if len(self.comp_to_list) != len(other.comp_to_list):
                raise ValueError("Dimensiones incompatibles para resta de vectores")
            return Vector(*(float(x) - float(y) for x, y in zip(self.comp_to_list, other.comp_to_list)))
        raise TypeError(f"No se puede restar Vector con {type(other)}")

    def __mul__(self, k):
        if isinstance(k, (int, float)):
            return Vector(*(float(x) * float(k) for x in self.comp_to_list))
        elif isinstance(k, Vector):
            if len(self.comp_to_list) != len(k.comp_to_list):
                raise ValueError("Dimensiones incompatibles para multiplicación Hadamard")
            return Vector(*(float(x) * float(y) for x, y in zip(self.comp_to_list, k.comp_to_list)))
        raise TypeError(f"Solo se puede multiplicar Vector por un escalar o por otro Vector, no por {type(k)}")

    def __pow__(self, k):
        if isinstance(k, (int, float)):
            return Vector(self.x ** k, self.y ** k)
        raise TypeError(f"No se puede elevar Vector a {type(k)}")

    def __round__(self, n=0):
        return Vector(*(round(x, n) for x in self.comp_to_list))

    def __str__(self):
        return ','.join(str(x) for x in self.comp_to_list)
