class Vector:
    def __init__(self, x:float, y:float, z:float = 0):
        self.x = x
        self.y = y
        self.z = z
        self.magnitud:float = (x**2 + y**2 + z**2)**0.5
        self.comp_to_list: list = (self.x, self.y, self.z)
    def get_direction(self):
        return Vector((self.x/self.magnitud), (self.y/self.magnitud), (self.z/self.magnitud))
    def __str__(self):
        return (str(self.x)+ "i + " + str(self.y) + "j + " + str(self.z) + "k")
    def __add__(self, v:"Vector"):
        return Vector(self.x + v.x, self.y + v.y, self.z + v.z)
    def __sub__(self, v: "Vector"):
        return Vector(self.x - v.x, self.y - v.y, self.z - v.z)
    def __mul__(self, k:float):
        return Vector(k*self.x, k*self.y, k*self.z)