import json

class Persona:
    def __init__(self, nom, apP, apM, ci):
        self.__nombre = nom
        self.__apellidoPaterno = apP
        self.__apellidoMaterno = apM
        self.__ci = ci

    def to_dict(self):
        return {
            "nombre": self.__nombre,
            "apellidoPaterno": self.__apellidoPaterno,
            "apellidoMaterno": self.__apellidoMaterno,
            "ci": self.__ci
        }

    @staticmethod
    def leer():
        nom = input("nombre: ")
        apP = input("apellido paterno: ")
        apM = input("apellido materno: ")
        ci = int(input("ci: "))
        return Persona(nom, apP, apM, ci)

    def mostrar(self):
        print("Nombre:", self.__nombre)
        print("Apellido Paterno:", self.__apellidoPaterno)
        print("Apellido Materno:", self.__apellidoMaterno)
        print("CI:", self.__ci)

    def getCi(self):
        return self.__ci


class Niño(Persona):
    def __init__(self, nom, apP, apM, ci, edad, peso, talla):
        super().__init__(nom, apP, apM, ci)
        self.__edad = edad
        self.__peso = peso
        self.__talla = talla

    def to_dict(self):
        d = super().to_dict()
        d["edad"] = self.__edad
        d["peso"] = self.__peso
        d["talla"] = self.__talla
        return d

    @staticmethod
    def leer():
        p = Persona.leer()
        edad = int(input("edad: "))
        peso = float(input("peso (kg): "))
        talla = float(input("talla (cm): "))
        return Niño(p._Persona__nombre,
                    p._Persona__apellidoPaterno,
                    p._Persona__apellidoMaterno,
                    p._Persona__ci,
                    edad, peso, talla)

    def mostrar(self):
        super().mostrar()
        print("Edad:", self.__edad)
        print("Peso:", self.__peso)
        print("Talla:", self.__talla)

    def getEdad(self):
        return self.__edad

    def getPeso(self):
        return self.__peso

    def getTalla(self):
        return self.__talla

    def pesoAdecuado(self):
        if self.__edad <= 5:
            return 10 <= self.__peso <= 20 and 80 <= self.__talla <= 110
        if self.__edad <= 12:
            return 20 <= self.__peso <= 40 and 110 <= self.__talla <= 150
        return 40 <= self.__peso <= 80 and 150 <= self.__talla <= 190


class ArchNiño:
    def __init__(self, na):
        self.__na = na

    def crearArchivo(self):
        with open(self.__na, "w") as f:
            json.dump([], f, indent=4)

    def adicionar(self, n):
        try:
            with open(self.__na, "r") as f:
                lista = json.load(f)
        except:
            lista = []
        lista.append(n.to_dict())
        with open(self.__na, "w") as f:
            json.dump(lista, f, indent=4)

    def cargar(self):
        try:
            with open(self.__na, "r") as f:
                return json.load(f)
        except:
            return []

    def listar(self):
        lista = self.cargar()
        for n in lista:
            print(n)

    def contarAdecuados(self):
        lista = self.cargar()
        c = 0
        for n in lista:
            edad = n["edad"]
            peso = n["peso"]
            talla = n["talla"]
            if edad <= 5:
                ok = 10 <= peso <= 20 and 80 <= talla <= 110
            elif edad <= 12:
                ok = 20 <= peso <= 40 and 110 <= talla <= 150
            else:
                ok = 40 <= peso <= 80 and 150 <= talla <= 190
            if ok:
                c += 1
        return c

    def mostrarNoAdecuados(self):
        lista = self.cargar()
        for n in lista:
            edad = n["edad"]
            peso = n["peso"]
            talla = n["talla"]
            if edad <= 5:
                ok = 10 <= peso <= 20 and 80 <= talla <= 110
            elif edad <= 12:
                ok = 20 <= peso <= 40 and 110 <= talla <= 150
            else:
                ok = 40 <= peso <= 80 and 150 <= talla <= 190
            if not ok:
                print(n)

    def promEdad(self):
        lista = self.cargar()
        if len(lista) == 0:
            return 0
        s = 0
        for n in lista:
            s += n["edad"]
        return s / len(lista)

    def buscarCi(self, ci):
        lista = self.cargar()
        for n in lista:
            if n["ci"] == ci:
                print(n)

    def mostrarMaxTalla(self):
        lista = self.cargar()
        if not lista:
            return
        maxT = max(n["talla"] for n in lista)
        for n in lista:
            if n["talla"] == maxT:
                print(n)


arch = ArchNiño("ninos.bin")
arch.crearArchivo()

n1 = Niño("Ana", "Lopez", "Guzman", 111, 4, 15, 95)
n2 = Niño("Luis", "Perez", "Mamani", 222, 8, 25, 130)
n3 = Niño("Maria", "Quispe", "Flores", 333, 6, 18, 120)
n4 = Niño("Jose", "Rojas", "Vega", 444, 13, 55, 160)
n5 = Niño("Lucia", "Diaz", "Lara", 555, 5, 30, 100)

arch.adicionar(n1)
arch.adicionar(n2)
arch.adicionar(n3)
arch.adicionar(n4)
arch.adicionar(n5)


arch.listar()
print()


print(arch.contarAdecuados())
print()


arch.mostrarNoAdecuados()
print()


print(arch.promEdad())
print()


arch.buscarCi(222)
print()


arch.mostrarMaxTalla()
