class Sabor:

    def __init__(self, nombre, hidratos, proteinas, grasas):
        self.__nombre = nombre
        self.__hidratos = hidratos
        self.__proteinas = proteinas
        self.__grasas = grasas

    def __str__(self):
        return f"´{self.__nombre}: Hidratos de Car.: {self.__hidratos}, Proteinas: {self.__proteinas}, Grasas: {self.__grasas}"

    def getNombre(self):
        return self.__nombre
    
    def getHidratos(self):
        return self.__hidratos

    def getProteinas(self):
        return self.__proteinas
    
    def getGrasas(self):
        return self.__grasas
    
    def setNombre(self, nnombre):
        if isinstance(nnombre, str):
            self.__nombre = nnombre

    def setHidratos(self, nhidratos):
        if isinstance(nhidratos, float):
            self.__hidratos = nhidratos
    
    def setProteinas(self, nproteinas):
        if isinstance(nproteinas, float):
            self.__proteinas = nproteinas

    def setGrasas(self, ngrasas):
        if isinstance(ngrasas, float):
            self.__grasas = ngrasas

class Helado:

    def __init__(self, tipo, tamanyo, cobertura, adornos, sabores):
        self.__tipo = tipo
        self.__tamanyo = tamanyo
        self.__cobertura = cobertura
        self.__adornos = adornos
        self.__sabores = sabores
        self.__listaTipo = ["cucurucho","terrina"]
        self.__listaTamanyos = ["Pequeño", "Mediano", "Grande"]
        self.__hayAdornos = "sin adornos"
        self.__listaSabores = []
        self.__nombreCobertura = "sin cobertura"
        if self.__cobertura != "":
            self.__nombreCobertura = f"con cobertura de {self.__cobertura}"
        if self.__adornos:
            self.__hayAdornos = "con adornos"
        for sabor in sabores:
            self.__listaSabores.append(sabor.getNombre())
            

    def __str__(self):
        return f"Helado en {self.__listaTipo[self.__tipo]} de tamaño {self.__listaTamanyos[self.__tamanyo].lower()}, {self.__hayAdornos}. \n Sabores: {self.__listaSabores}"

    def getTipo(self):
        return self.__tipo
    
    def getTamanyo(self):
        return self.__tamanyo
    
    def getCobertura(self):
        return self.__cobertura
    
    def getAdornos(self):
        return self.__adornos
    
    def getSabores(self):
        return self.__sabores
    
    def setSabores(self, nsabores):
        if isinstance(nsabores, list):
            self.__sabores = nsabores
    
    def setTipo(self, ntipo):
        if ntipo in [0,1]:
            self.__tipo = ntipo

    def setTamanyo(self, ntamanyo):
        if ntamanyo in [0,1,2]:
            self.__tamanyo = ntamanyo

    def setCobertura(self, ncobertura):
        if isinstance(ncobertura, str):
            self.__cobertura = ncobertura

    def setAdornos(self, nadornos):
        if isinstance(nadornos, bool):
            self.__adornos = nadornos 

    def getPrecio(self):
        precio = 0
        if self.__tamanyo == 0:
            precio += (len(self.__sabores) * 0.5)
        elif self.__tamanyo == 1:
            precio += (len(self.__sabores) * 0.75)
        elif self.__tamanyo == 2:
            precio += (len(self.__sabores))
        if self.__cobertura != "":
            precio += 0.5
        if self.__adornos:
            precio += 1
        return precio

class DeustoGelati:

    def __init__(self, helados, tastes):
        self.__helados = helados
        self.__tastes = tastes
        self.__tastenames = []
        self.__numero = 1
        for taste in tastes:
            self.__tastenames.append(f"[{self.__numero}] {self.__tastes[taste].getNombre()}")
            self.__numero += 1
    
    def registrarVentas(self):
        print("¡Bienvenido a la heladría Deusto!")
        eleccion = ""
        elecfin = ""
        while elecfin.lower() != "no":
            listasabores = []
            while eleccion.lower() != "salir":
                print(f"Sabores disponibles: {self.__tastenames} ")
                print("Elige el numero del sabor para añadírselo a tu helado o escribe salir para salir:")
                eleccion = input()
                listasabores.append(self.__tastes[int(eleccion) - 1])
            print("Elige tu tipo de cucurucho: 0: cucurucho, 1: tarrina")
            tipocucurucho = int(input())
            print('Elige el tamaño de tu helado: 0: Pequeño, 1: Mediano, 2: Grande')
            tamanyohelado = int(input())
            print('Escribe el tipo de tu cobertura: ')
            tipocobertura = input()
            print("Quieres adornos?: 1.- Si, 2.- No")
            elec2 = int(input())
            if elec2 == 1:
                haycobertura = True
            elif elec2 == 2:
                haycobertura = False
            self.__helados.append(Helado(tipocucurucho, tamanyohelado, tipocobertura, haycobertura, listasabores))
            print("¡Hecho! Se ha añadido tu helado.")
            print("Quiere introducir otro helado?: ")
            elecfin = str(input())

    def mostrarTotalesNutriciones(self, helados):
        hidratos_total = 0
        proteinas_total = 0
        grasas_total = 0
        for helado in helados:
            hidratos_per_helado = 0
            proteinas_per_helado = 0
            grasas_per_helado = 0
            for sabor in helado.getSabores():
                hidratos_per_helado += sabor.getHidratos()
                proteinas_per_helado += sabor.getProteinas()
                grasas_per_helado += sabor.getGrasas()
            if helado.getTipo() == 0:
                if helado.getTamanyo() == 0:
                    hidratos_total += 0.8 * (hidratos_per_helado + 17.7)
                    proteinas_total += 0.8 * (proteinas_per_helado + 1.67)
                    grasas_total += 0.8 * (grasas_per_helado + 10.9)
                elif helado.getTamanyo == 2:
                    hidratos_total += 1.2 * (hidratos_per_helado + 17.7)
                    proteinas_total += 1.2 * (proteinas_per_helado + 1.67)
                    grasas_total += 1.2 * (grasas_per_helado + 10.9)
                else:
                    hidratos_total += (hidratos_per_helado + 17.7)
                    proteinas_total += (proteinas_per_helado + 1.67)
                    grasas_total += (grasas_per_helado + 10.9)
        print(f"En esta lista de helados: Hidratos: {hidratos_total}, Proteinas: {proteinas_total}, Grasas: {grasas_total}")

    def mostrarIngresoMedio(self, helados):
        lista_precios = []
        for helado in helados:
            lista_precios.append(helado.getPrecio())
        print(sum(lista_precios)/len(lista_precios))

#if __name__ = "__main__":
