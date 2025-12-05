import json

class Medicamento:
    def __init__(self, nom, cod, tip, pre):
        self.__nombre = nom
        self.__codMedicamento = cod
        self.__tipo = tip
        self.__precio = pre

    def to_dict(self):
        return {
            "nombre": self.__nombre,
            "codMedicamento": self.__codMedicamento,
            "tipo": self.__tipo,
            "precio": self.__precio
        }

    @staticmethod
    def leer():
        nom = input("nombre del medicamento: ")
        cod = int(input("codigo del medicamento: "))
        tip = input("tipo del medicamento: ")
        pre = float(input("precio del medicamento: "))
        return Medicamento(nom, cod, tip, pre)

    def mostrar(self):
        print("Nombre:", self.__nombre)
        print("Codigo:", self.__codMedicamento)
        print("Tipo:", self.__tipo)
        print("Precio:", self.__precio)

    def getTipo(self):
        return self.__tipo

    def getPrecio(self):
        return self.__precio

    def getNombre(self):
        return self.__nombre


class Farmacia:
    def __init__(self, nom, suc, direc):
        self.__nombreFarmacia = nom
        self.__sucursal = suc
        self.__direccion = direc
        self.__nroMedicamentos = 0
        self.__m = []

    def agregar(self, med):
        if self.__nroMedicamentos < 100:
            self.__m.append(med)
            self.__nroMedicamentos += 1

    @staticmethod
    def leer():
        nom = input("nombre farmacia: ")
        suc = int(input("sucursal: "))
        direc = input("direccion: ")
        f = Farmacia(nom, suc, direc)
        while True:
            s = input("registrar medicamento (si/no): ")
            if s == "si":
                med = Medicamento.leer()
                f.agregar(med)
            else:
                break
        return f

    def mostrar(self):
        print("Farmacia:", self.__nombreFarmacia)
        print("Sucursal:", self.__sucursal)
        print("Direccion:", self.__direccion)
        print("Numero de medicamentos:", self.__nroMedicamentos)
        for m in self.__m:
            m.mostrar()

    def to_dict(self):
        meds = []
        for m in self.__m:
            meds.append(m.to_dict())
        return {
            "nombreFarmacia": self.__nombreFarmacia,
            "sucursal": self.__sucursal,
            "direccion": self.__direccion,
            "nroMedicamentos": self.__nroMedicamentos,
            "medicamentos": meds
        }

    def getDireccion(self):
        return self.__direccion

    def getSucursal(self):
        return self.__sucursal

    def mostrarMedicamentos(self, x):
        for m in self.__m:
            if m.getTipo() == x:
                m.mostrar()

    def buscaMedicamento(self, x):
        for m in self.__m:
            if m.getNombre() == x:
                m.mostrar()


class ArchFarmacia:
    def __init__(self, na):
        self.__na = na

    def crearArchivo(self):
        with open(self.__na, "w") as f:
            json.dump([], f, indent=4)

    def adicionar(self, f):
        try:
            with open(self.__na, "r") as arch:
                lista = json.load(arch)
        except:
            lista = []
        lista.append(f.to_dict())
        with open(self.__na, "w") as arch:
            json.dump(lista, arch, indent=4)

    def cargar(self):
        try:
            with open(self.__na, "r") as arch:
                return json.load(arch)
        except:
            return []

    def listar(self):
        lista = self.cargar()
        for f in lista:
            print(f)

    def mostrarMedicamentosResfrios(self):
        lista = self.cargar()
        for f in lista:
            for m in f["medicamentos"]:
                if m["tipo"] == "resfrio":
                    print(m)

    def precioMedicamentoTos(self):
        lista = self.cargar()
        s = 0
        c = 0
        for f in lista:
            for m in f["medicamentos"]:
                if m["tipo"] == "tos":
                    s += m["precio"]
                    c += 1
        if c == 0:
            return 0
        return s / c

    def mostrarMedicamentosMenorTos(self):
        prom = self.precioMedicamentoTos()
        lista = self.cargar()
        for f in lista:
            for m in f["medicamentos"]:
                if m["tipo"] == "tos" and m["precio"] < prom:
                    print(m)

    def mostrarTosSucursal(self, suc):
        lista = self.cargar()
        for f in lista:
            if f["sucursal"] == suc:
                for m in f["medicamentos"]:
                    if m["tipo"] == "tos":
                        print(m)

    def farmaciasTapsin(self):
        lista = self.cargar()
        for f in lista:
            for m in f["medicamentos"]:
                if m["nombre"] == "Tapsin":
                    print("Sucursal:", f["sucursal"], "Direccion:", f["direccion"])

    def buscarTipo(self, tipo):
        lista = self.cargar()
        for f in lista:
            for m in f["medicamentos"]:
                if m["tipo"] == tipo:
                    print(m)

    def ordenarPorDireccion(self):
        lista = self.cargar()
        lista.sort(key=lambda x: x["direccion"])
        with open(self.__na, "w") as arch:
            json.dump(lista, arch, indent=4)
        return lista

    def moverTipo(self, tip, sucY, sucZ):
        lista = self.cargar()
        origen = None
        destino = None
        for f in lista:
            if f["sucursal"] == sucY:
                origen = f
            if f["sucursal"] == sucZ:
                destino = f
        if origen is None or destino is None:
            return
        nuevos = []
        for m in origen["medicamentos"]:
            if m["tipo"] == tip:
                destino["medicamentos"].append(m)
                destino["nroMedicamentos"] += 1
            else:
                nuevos.append(m)
        origen["medicamentos"] = nuevos
        origen["nroMedicamentos"] = len(nuevos)
        with open(self.__na, "w") as arch:
            json.dump(lista, arch, indent=4)


arch = ArchFarmacia("farmacias.bin")
arch.crearArchivo()

f1 = Farmacia("Central", 1, "Av. Siempre Viva 123")
f1.agregar(Medicamento("Tapsin", 101, "tos", 10.5))
f1.agregar(Medicamento("Jarabe", 102, "tos", 8.0))
f1.agregar(Medicamento("Vitamina C", 103, "resfrio", 5.5))

f2 = Farmacia("Sur", 2, "Calle B 456")
f2.agregar(Medicamento("Tapsin", 201, "resfrio", 9.5))
f2.agregar(Medicamento("Paracetamol", 202, "fiebre", 4.0))

f3 = Farmacia("Norte", 3, "Av. Colon 789")
f3.agregar(Medicamento("Jarabe Infantil", 301, "tos", 7.0))

arch.adicionar(f1)
arch.adicionar(f2)
arch.adicionar(f3)


arch.mostrarTosSucursal(1)
print()


arch.farmaciasTapsin()
print()


arch.buscarTipo("resfrio")
print()


print(arch.ordenarPorDireccion())
print()


arch.moverTipo("tos", 1, 3)
arch.listar()

    
        
