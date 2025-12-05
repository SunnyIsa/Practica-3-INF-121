import json

class Animal:
    def __init__(self, esp, nom, cant):
        self.__especie = esp
        self.__nombre = nom
        self.__cantidad = cant

    def to_dict(self):
        return {
            "especie": self.__especie,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad
        }

    @staticmethod
    def leer():
        esp = input("especie: ")
        nom = input("nombre animal: ")
        cant = int(input("cantidad: "))
        return Animal(esp, nom, cant)

    def mostrar(self):
        print("Especie:", self.__especie)
        print("Nombre:", self.__nombre)
        print("Cantidad:", self.__cantidad)

    def getEspecie(self):
        return self.__especie

    def getCantidad(self):
        return self.__cantidad


class Zoologico:
    def __init__(self, i, nom):
        self.__id = i
        self.__nombre = nom
        self.__nroAnimales = 0
        self.__animales = []

    @staticmethod
    def leer():
        i = int(input("id zoologico: "))
        nom = input("nombre zoologico: ")
        z = Zoologico(i, nom)
        while True:
            s = input("registrar animal (si/no): ")
            if s == "si":
                a = Animal.leer()
                z.agregar(a)
            else:
                break
        return z

    def agregar(self, a):
        if self.__nroAnimales < 30:
            self.__animales.append(a)
            self.__nroAnimales += 1

    def mostrar(self):
        print("ID:", self.__id)
        print("Nombre:", self.__nombre)
        print("Nro Animales:", self.__nroAnimales)
        for a in self.__animales:
            a.mostrar()

    def to_dict(self):
        lista = []
        for a in self.__animales:
            lista.append(a.to_dict())
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "nroAnimales": self.__nroAnimales,
            "animales": lista
        }

    def getId(self):
        return self.__id

    def getAnimales(self):
        return self.__animales

    def tieneEspecie(self, esp):
        for a in self.__animales:
            if a.getEspecie() == esp:
                print(a.to_dict())


class ArchZoo:
    def __init__(self, nombre):
        self.__nombre = nombre

    def crearArchivo(self):
        with open(self.__nombre, "w") as f:
            json.dump([], f, indent=4)

    def adicionar(self, z):
        try:
            with open(self.__nombre, "r") as f:
                lista = json.load(f)
        except:
            lista = []
        lista.append(z.to_dict())
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

    def modificar(self, idZoo, nuevoNombre):
        lista = self.cargar()
        for z in lista:
            if z["id"] == idZoo:
                z["nombre"] = nuevoNombre
        with open(self.__nombre, "w") as f:
            json.dump(lista, f, indent=4)

    def eliminar(self, idZoo):
        lista = self.cargar()
        nueva = []
        for z in lista:
            if z["id"] != idZoo:
                nueva.append(z)
        with open(self.__nombre, "w") as f:
            json.dump(nueva, f, indent=4)

    def mayorVariedad(self):
        lista = self.cargar()
        maxV = max([len(z["animales"]) for z in lista]) if lista else 0
        for z in lista:
            if len(z["animales"]) == maxV:
                print(z)

    def vacios(self):
        lista = self.cargar()
        nueva = []
        for z in lista:
            if len(z["animales"]) == 0:
                print(z)
            else:
                nueva.append(z)
        with open(self.__nombre, "w") as f:
            json.dump(nueva, f, indent=4)

    def mostrarEspecie(self, esp):
        lista = self.cargar()
        for z in lista:
            for a in z["animales"]:
                if a["especie"] == esp:
                    print(a)

    def mover(self, esp, idX, idY):
        lista = self.cargar()
        origen = None
        destino = None

        for z in lista:
            if z["id"] == idX:
                origen = z
            if z["id"] == idY:
                destino = z

        if origen is None or destino is None:
            return

        restantes = []
        for a in origen["animales"]:
            if a["especie"] == esp:
                destino["animales"].append(a)
                destino["nroAnimales"] += 1
            else:
                restantes.append(a)
        origen["animales"] = restantes
        origen["nroAnimales"] = len(restantes)
        with open(self.__nombre, "w") as f:
            json.dump(lista, f, indent=4)


arch = ArchZoo("zoos.bin")
arch.crearArchivo()

z1 = Zoologico(1, "Safari")
z1.agregar(Animal("Felino", "Tigre", 2))
z1.agregar(Animal("Ave", "Aguila", 3))

z2 = Zoologico(2, "Amazonico")
z2.agregar(Animal("Reptil", "Caiman", 4))

z3 = Zoologico(3, "Desierto")

arch.adicionar(z1)
arch.adicionar(z2)
arch.adicionar(z3)


arch.listar()
print()

arch.modificar(2, "Amazonas Grande")
arch.listar()
print()

arch.eliminar(3)
arch.listar()
print()


arch.mayorVariedad()
print()

arch.vacios()
arch.listar()
print()

arch.mostrarEspecie("Felino")
print()

arch.mover("Ave", 1, 2)
arch.listar()
