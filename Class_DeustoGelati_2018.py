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
            self.__listaSabores.append(self.__sabores.getNombre())
            

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

class DeustoGelati:
    
