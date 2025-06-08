class vector:
    def __init__(self,x:float,y:float,z:float)->None:
        self.x:float = x
        self.y:float = y
        self.z:float = z
        self.magnitud:float = (x**2 + y**2 + z**2)**0.5
        self.vect_direccion: list = [x/self.magnitud,y/self.magnitud,z/self.magnitud]  
        self.formav: list = (x,y,z)  
def escalar_product(k:float,v:vector)->vector:
    r= vector((k*v.x), k*(v.y), k*(v.z))
    return r        
def dot_product(v1:vector,v2:vector)->float:
    return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z
def product_vectorial(v1:vector,v2:vector)->vector:
    x =v1.y*v2.z - v1.z*v2.y
    y = -(v1.x*v2.z - v1.z*v2.x)
    z = v1.x*v2.y - v1.y*v2.x
    return vector(x,y,z)
def proyeccion_vectorial(v1:vector,v2:vector)->vector:
    m = (dot_product(v1,v2))/v2.magnitud
    lamb = escalar_product(m,v2.vect_direccion)
    return lamb
