import json

class Alimento:
    def __init__(self, nom, fv, cant):
        self.__nombre = nom
        self.__fechaVencimiento = fv
        self.__cantidad = cant

    def to_dict(self):
        return {
            "nombre": self.__nombre,
            "fechaVencimiento": self.__fechaVencimiento,
            "cantidad": self.__cantidad
        }

    @staticmethod
    def leer():
        nom = input("nombre alimento: ")
        fv = input("fecha vencimiento (aaaa-mm-dd): ")
        cant = int(input("cantidad: "))
        return Alimento(nom, fv, cant)

    def mostrar(self):
        print("Nombre:", self.__nombre)
        print("Fecha vencimiento:", self.__fechaVencimiento)
        print("Cantidad:", self.__cantidad)

    def getNombre(self):
        return self.__nombre

    def getFecha(self):
        return self.__fechaVencimiento

    def getCantidad(self):
        return self.__cantidad


class ArchRefri:
    def __init__(self, nombre):
        self.__nombre = nombre

    def crearArchivo(self):
        with open(self.__nombre, "w") as f:
            json.dump([], f, indent=4)

    def adicionar(self, a):
        try:
            with open(self.__nombre, "r") as f:
                lista = json.load(f)
        except:
            lista = []
        lista.append(a.to_dict())
        with open(self.__nombre, "w") as f:
            json.dump(lista, f, indent=4)

    def cargar(self):
        try:
            with open(self.__nombre, "r") as f:
                return json.load(f)
        except:
            return []

    def listar(self):
        lista = self.cargar()
        for x in lista:
            print(x)

    def modificarPorNombre(self, nom, nuevaFecha, nuevaCant):
        lista = self.cargar()
        for a in lista:
            if a["nombre"] == nom:
                a["fechaVencimiento"] = nuevaFecha
                a["cantidad"] = nuevaCant
        with open(self.__nombre, "w") as f:
            json.dump(lista, f, indent=4)

    def eliminarPorNombre(self, nom):
        lista = self.cargar()
        nueva = []
        for a in lista:
            if a["nombre"] != nom:
                nueva.append(a)
        with open(self.__nombre, "w") as f:
            json.dump(nueva, f, indent=4)

    def caducadosAntes(self, fechaX):
        lista = self.cargar()
        for a in lista:
            if a["fechaVencimiento"] < fechaX:
                print(a)

    def eliminarCero(self):
        lista = self.cargar()
        nueva = []
        for a in lista:
            if a["cantidad"] != 0:
                nueva.append(a)
        with open(self.__nombre, "w") as f:
            json.dump(nueva, f, indent=4)

    def vencidos(self, fechaHoy):
        lista = self.cargar()
        for a in lista:
            if a["fechaVencimiento"] < fechaHoy:
                print(a)

    def maxCantidad(self):
        lista = self.cargar()
        if not lista:
            return
        maxC = max(a["cantidad"] for a in lista)
        for a in lista:
            if a["cantidad"] == maxC:
                print(a)


arch = ArchRefri("refri.bin")
arch.crearArchivo()

a1 = Alimento("Leche", "2024-05-10", 2)
a2 = Alimento("Yogurt", "2024-05-05", 0)
a3 = Alimento("Queso", "2024-06-01", 5)
a4 = Alimento("Mantequilla", "2024-04-30", 3)

arch.adicionar(a1)
arch.adicionar(a2)
arch.adicionar(a3)
arch.adicionar(a4)

arch.listar()
print()


arch.modificarPorNombre("Yogurt", "2024-05-20", 4)
arch.listar()
print()

arch.eliminarPorNombre("Leche")
arch.listar()
print()

arch.caducadosAntes("2024-05-15")
print()

arch.eliminarCero()
arch.listar()
print()


arch.vencidos("2024-05-15")
print()


arch.maxCantidad()
