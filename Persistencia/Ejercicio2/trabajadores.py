import json
class Trabajador:
    def __init__(self,nombre,carnet,salario):
        self.__nombre=nombre
        self.__carnet=carnet
        self.__salario=salario
    def getCarnet(self):
        return self.__carnet
    def to_dict(self):
        return{
            "nombre":self.__nombre,
            "carnet":self.__carnet,
            "salario":self.__salario
            }
class ArchivoTrabajador:
    def __init__(self):
        self.__nombreArch="trabajadores.bin"
    def crearArchivo(self):
        s=[]
        with open ( self.__nombreArch,"w")as f:
            json.dump(s,f,indent=4)
    def guardarTrabajador(self,t):
        try:
            with open (self.__nombreArch,"r")as f:
                    tra=json.load(f)
        except:
            tra=[]
        tra.append(t.to_dict())
        with open ( self.__nombreArch,"w")as f:
            json.dump(tra,f,indent=4)
    def cargar(self):
        try:
            with open (self.__nombreArch,"r")as f:
                tra=json.load(f)
            return tra
        except:
            print("todavia no guardaste nada ")
    def aumentarSalario(self,a,t):
        try:
            with open (self.__nombreArch,"r")as f:
                    tra=json.load(f)
        except:
            tra=[]
        for trabajador in tra:
            if trabajador["carnet"]==t.getCarnet():
                trabajador["salario"]=trabajador["salario"]+a
        with open ( self.__nombreArch,"w")as f:
            json.dump(tra,f,indent=4)
    def buscar(self):
        try:
            with open (self.__nombreArch,"r")as f:
                    tra=json.load(f)
        except:
            tra=[]
        for i in range(len(tra)):
            for j in range(0, len(tra) - i - 1):
                if tra[j] ["salario"]> tra[j + 1]["salario"]:
                    tra[j]["salario"], tra[j + 1]["salario"] = tra[j + 1]["salario"], tra[j]["salario"]
        return tra[len(tra)-1]
    def ordenar(self):
        try:
            with open (self.__nombreArch,"r")as f:
                    tra=json.load(f)
        except:
            tra=[]
        for i in range(len(tra)):
            for j in range(0, len(tra) - i - 1):
                if tra[j] ["salario"]> tra[j + 1]["salario"]:
                    tra[j]["salario"], tra[j + 1]["salario"] = tra[j + 1]["salario"], tra[j]["salario"]
        with open ( self.__nombreArch,"w")as f:
            json.dump(tra,f,indent=4)

        

    
tr1=Trabajador("Juan","123123",1560)
tr2=Trabajador("Maria","23423",1900)
tr3=Trabajador("Lucia","4536",1800)
tr4=Trabajador("Roy","893409",1300)


arch=ArchivoTrabajador()

arch.crearArchivo()
arch.guardarTrabajador(tr1)
arch.guardarTrabajador(tr2)
arch.guardarTrabajador(tr3)
arch.guardarTrabajador(tr4)

trabs=arch.cargar()
print(trabs)
print()

arch.aumentarSalario(200,tr1)
trabs=arch.cargar()
print(trabs)
print()
traM=arch.buscar()
print(traM)
print()
arch.ordenar()
trabs=arch.cargar()
print(trabs)




