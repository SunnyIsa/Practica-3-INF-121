import json
class Producto:
    def __init__(self,codigo,nombre,precio):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__precio=precio
    def getCodigo(self):
        return self.__codigo
    def to_dict(self):
        return{
            "codigo":self.__codigo,
            "nombre":self.__nombre,
            "precio":self.__precio
            }
class ArchivoProducto:
    def __init__(self,n):
        self.__nomA=n
    def crearArchivo(self):
        s=[]
        with open ( self.__nomA,"w")as f:
            json.dump(s,f,indent=4)
    def guardarProducto(self,p):
        try:
            with open (self.__nomA,"r")as f:
                    pro=json.load(f)
        except:
            pro=[]
        pro.append(p.to_dict())
        with open ( self.__nomA,"w")as f:
            json.dump(pro,f,indent=4)
    def cargar(self):
        try:
            with open (self.__nomA,"r")as f:
                pro=json.load(f)
            return pro
        except:
            print("todavia no guardaste nada ")
    def buscarProducto(self,c):
        try:
            with open (self.__nomA,"r")as f:
                    pro=json.load(f)
        except:
            pro=[]
        for producto in pro:
            if producto["codigo"]==c:
                print(producto)
    def calcularProm(self):
        s=0
        try:
            with open (self.__nomA,"r")as f:
                    pro=json.load(f)
        except:
            pro=[]
        for producto in pro:
            s+=producto["precio"]
        return s/len(pro)
    def masCaro(self):
        try:
            with open (self.__nomA,"r")as f:
                    pro=json.load(f)
        except:
            pro=[]
        for i in range(len(pro)):
            for j in range(0, len(pro) - i - 1):
                if pro[j] ["precio"]> pro[j + 1]["precio"]:
                    pro[j]["precio"], pro[j + 1]["precio"] = pro[j + 1]["precio"], pro[j]["precio"]
        return pro[len(pro)-1]
arch=ArchivoProducto("productos.bin")
arch.crearArchivo()
pro1=Producto(111,"galleta",3)
pro2=Producto(112,"bebida",5)
pro3=Producto(113,"dulce",0.50)
pro4=Producto(114,"helado",3)
arch.guardarProducto(pro1)
arch.guardarProducto(pro2)
arch.guardarProducto(pro3)
arch.guardarProducto(pro4)
pros=arch.cargar()
print(pros)
print()
arch.buscarProducto(114)
print()
s=arch.calcularProm()
print(s)
print()
car=arch.masCaro()
print(car)
    
        
