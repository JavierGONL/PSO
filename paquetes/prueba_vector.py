class Point: #definimos el punto por dos coordenadas en el plano
  def __init__(self, x: float, y: float, z:float): 
     self.x = x
     self.y = y
     self.z = z
     self.comp_to_list: list = (self.x, self.y, self.z)
  def redo(self, nx , ny, nz):
     self.x = nx
     self.y = ny
     self.z = nz
  def __str__(self):
     return ("(" +str(self.x)+ ", " + str(self.y) + ", " + str(self.z) + ")")
  def __add__(self, v:"Point"):
        return Point(self.x + v.x, self.y + v.y, self.z + v.z)
  def __sub__(self, v: "Point"):
        return Point(self.x - v.x, self.y - v.y, self.z - v.z)
  def __mul__(self, k:float):
        return Point(k*self.x, k*self.y, k*self.z)
class Vector(Point):
    def __init__(self, x:float, y:float, z:float = 0):
        super().__init__(x,y,z)
        self.magnitud:float = (x**2 + y**2 + z**2)**0.5
    def get_direction(self):
        return Vector((self.x/self.magnitud), (self.y/self.magnitud), (self.z/self.magnitud))
    def __str__(self):
        return (str(self.x)+ "i + " + str(self.y) + "j + " + str(self.z) + "k")