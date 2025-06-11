class Point: 
    #! tuve que hacer un monton de cosas raras aca, usar copilot :(
    #!  2 horas buscando una solucion por mi mismo
    #! y resulta que el malp python cuando hace un (escalar * un vector)
    #! es diferente que un (vector * un escalar) y segun cada caso invoca o __mul__ o __rmul__ :/ 
    #! y pasa lo mismo con la hpta suma y resta.
    #! yo solo iba a agregar un clase punto re basica para hacer pruebas y nop dos horas arreglando esta cosa JAJAJAJAJAJA, :[

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.comp_to_list = [self.x, self.y]

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x + other, self.y + other)
        else:
            return "Error: un dato mal ingresado en la suma Point"

    def __radd__(self, p):
        return self.__add__(p)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)
    
    def __rsub__(self, p):
        return self.__sub__(p)

    def __mul__(self, k):
        x = float(self.x)
        y = float(self.y)
        return Point(x * k, y * k)

    def __rmul__(self, k):
        return self.__mul__(k)

    def __str__(self):
        return f"{self.x},{ self.y}"


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
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError(f"No se puede sumar Vector con {type(other)}")

    def __rmul__(self, k):
        return self.__mul__(k)
