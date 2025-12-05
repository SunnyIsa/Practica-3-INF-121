import json
class Estudiante:
    def __init__(self,ru,nombre,paterno,materno,edad):
        self.ru=ru
        self.nombre=nombre
        self.paterno=paterno
        self.materno=materno
        self.edad=edad
class Nota:
    def __init__(self,materia,notaFinal,estudiante):
        self.materia=materia
        self.notaFinal=notaFinal
        self.estudiante=estudiante
    
class ArchiNota:
    def __init__(self,nombreArchi):
        self.nombreArchi=nombreArchi
    def crearArchivo(self):
        s=[]
        with open ( self.nombreArchi,"w")as f:
            json.dump(s,f,indent=4)
    def cargar(self):
        try:
            with open (self.nombreArchi,"r")as f:
                nots=json.load(f)
            return nots
        except:
            print("todavia no guardaste nada ")
    def guardarNotas(self,notas):
        try:
            with open (self.nombreArchi,"r")as f:
                    nots=json.load(f)
        except:
            nots=[]
        for n in notas:
            nota=Nota(n.materia,n.notaFinal,n.estudiante.__dict__)
            nots.append(nota.__dict__)
        with open ( self.nombreArchi,"w")as f:
            json.dump(nots,f,indent=4)
    def promedio(self):
        s=0
        try:
            with open (self.nombreArchi,"r")as f:
                    nots=json.load(f)
        except:
            nots=[]
        for n in nots:
            s+=n["notaFinal"]
        return s/len(nots)
    def buscarM(self):
        s=[]
        g=0
        try:
            with open (self.nombreArchi,"r")as f:
                    nots=json.load(f)
        except:
            nots=[]
        for i in range(len(nots)):
            for j in range(0, len(nots) - i - 1):
                if nots[j] ["notaFinal"]> nots[j + 1]["notaFinal"]:
                    nots[j]["notaFinal"], nots[j + 1]["notaFinal"] = nots[j + 1]["notaFinal"], nots[j]["notaFinal"]
        g=nots[len(nots)-1]["notaFinal"]
        for n in nots:
            if n["notaFinal"]==g:
                s.append(n)
        return s
    def eliminar(self,mat):
        s=[]
        try:
            with open (self.nombreArchi,"r")as f:
                    nots=json.load(f)
        except:
            nots=[]
        for n in nots:
            if n["materia"]!=mat:
                s.append(n)
        with open ( self.nombreArchi,"w")as f:
            json.dump(s,f,indent=4)

        
arch=ArchiNota("notas.bin")
arch.crearArchivo()
est1=Estudiante("1123","Juan","Perez","Martinez",12)
est2=Estudiante("1124","Lucia","Torrez","Cruz",15)
est3=Estudiante("1125","Maria","Callisaya","Vázquez",13)
est4=Estudiante("1126","Juan","Campos","Farias",12)
not1=Nota("Matematicas",89,est1)
not2=Nota("Lenguaje",98,est2)
not3=Nota("Ciencias",87,est3)
not4=Nota("Religion",98,est4)

notas=[not1,not2,not3,not4]
arch.guardarNotas(notas)
nots=arch.cargar()
print(nots)
print()
s=arch.promedio()
print(s)
print()
m=arch.buscarM()
print(m)
print()
arch.eliminar("Ciencias")
nots=arch.cargar()
print(nots)




    
