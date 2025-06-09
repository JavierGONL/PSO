class Vector:
    def __init__(self,x:float,y:float,z:float):
        self.x:float = x
        self.y:float = y
        self.z:float = z
        self.magnitud:float = (x**2 + y**2 + z**2)**0.5
        self.comp_to_list: list = (self.x,self.y,self.z)
    def get_direction(self):
        return Vector((self.x/self.magnitud),(self.y/self.magnitud),(self.z/self.magnitud))
    def __add__(self,v):
        if type(v) == Vector:
            return Vector(self.x + v.x, self.y + v.y, self.z + v.z)
    def escalar_product(k:float,v):
        return Vector(k*(v.x),k*(v.y),k*(v.z))
    def dot_product(v1,v2)->float:
        return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z
    def product_vectorial(v1,v2):
        x =v1.y*v2.z - v1.z*v2.y
        y = -(v1.x*v2.z - v1.z*v2.x)
        z = v1.x*v2.y - v1.y*v2.x
        return Vector(x,y,z)