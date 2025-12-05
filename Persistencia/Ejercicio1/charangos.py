import json
class Charango:
    def __init__(self,material,Cuerdas):
        self.material=material
        self.nroCuerdas=0
        self.Cuerdas=[]
        for i in range(len(Cuerdas)):
            if self.nroCuerdas <10:
                self.Cuerdas.append(Cuerdas[i])
                self.nroCuerdas+=1
                
            else:
                print (f"se llego al limite en la cuerda {i}")
    def agregar(self, cuerda):
        if self.nroCuerdas<10:
            self.Cuerdas.append(cuerda)
            self.nroCuerdas+=1
        else:
            print("ya no hay espoacio para mas cuerdas")
class Archivo:
    def __init__(self):
        self.charangos=[]
    def agregar(self,charango):

        self.charangos.append(charango.__dict__)

    def actualizar(self):

        with open ("charangos.bin","w")as f:
            json.dump(self.charangos,f,indent=4)
    def cargar(self):
        try:
            with open ("charangos.bin","r")as f:
                char=json.load(f)
            return char
        except:
            print("todavia no guardaste nada ")
    def eliminar(self):
        char2=[]
        with open ("charangos.bin","r")as f:
                char=json.load(f)
        for charango in char:
            s=0
            for cuerda in charango["Cuerdas"]:
                if cuerda==False:
                    s+=1
            if s<7:
                char2.append(charango)
        self.charangos=char2
        self.actualizar()
    def listar(self,x):
        try:
            with open ("charangos.bin","r")as f:
                    char=json.load(f)
        except:
            char=[]
        for charango in char:
            if charango["material"]==x:
                print(charango)
    def buscar(self):
        try:
            with open ("charangos.bin","r")as f:
                    char=json.load(f)
        except:
            char=[]
        for charango in char:
            if charango["nroCuerdas"]==10:
                return charango
    def ordenar(self):
        try:
            with open ("charangos.bin","r")as f:
                    char=json.load(f)
        except:
            char=[]
        for i in range(len(char)):
            for j in range(0, len(char) - i - 1):
                if char[j] ["material"]> char[j + 1]["material"]:
                    char[j]["material"], char[j + 1]["material"] = char[j + 1]["material"], char[j]["material"]
        self.charangos=char
        self.actualizar()
                
        
        


        

ch1=Charango("palosanto",[True,False,False,False,False,False,False,True,True,True,True])
ch2=Charango("nogal",[True,False,False,False,False,False,False,True,True,True])
ch3=Charango("rauli",[True,False,False,False,False,False,False,True,False,True])
ch4=Charango("mara",[True,False,False,False,False,False,False,True,False,True])
ac=Archivo()
ac.agregar(ch1)
ac.agregar(ch2)
ac.agregar(ch3)
ac.agregar(ch4)
ac.actualizar()
char=ac.cargar()
print(char)
print()
ac.eliminar()
char=ac.cargar()
print(char)
print()
ac.listar("palosanto")
print()
char10=ac.buscar()
print(char10)
print()
ac.ordenar()
char=ac.cargar()
print(char)

