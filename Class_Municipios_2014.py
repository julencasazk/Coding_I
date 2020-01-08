class Municipio:

    def __init__(self, nombre, CP, habitantes, hogares, cta): #cta = consumo total anual
        self.__nombre = nombre
        self.__CP = CP
        self.__habitantes = habitantes
        self.__hogares = hogares
        self.__cta = cta
    
    def getNombre(self):
        return self.__nombre
    
    def getCP(self):
        return self.__CP
    
    def getHabitantes(self):
        return self.__habitantes

    def getHogares(self):
        return self.__hogares

    def getCta(self):
        return self.__cta

    def setNombre(self, nnombre):
        if isinstance(nnombre, str) and len(nnombre) > 0:
            self.__nombre = nnombre

    def setCP(self, nCP):
        if isinstance(nCP, int) and nCP >= 0:
            self.__CP = nCP

    def setHabitantes(self, nhabitantes):
        if isinstance(nhabitantes, int) and nhabitantes >= 0:
            self.__habitantes = nhabitantes

    def setHogares(self, nhogares):
        if isinstance(nhogares, int) and nhogares >= 0:
            self.__hogares = nhogares

    def setCta(self, nCta):
        if isinstance(nCta, float) and nCta >= 0:
            self.__cta = nCta
    
    def consumoMedioHab(self):
        return (self.__CP/self.__habitantes)

    def crearMensaje(self):
        return f"{self.__hogares} hogares han consumido en total {self.__CP} m3, con una media de {self.consumoMedioHab()} m3/habitante"
    
    def cargarMunicipios(self):
        vMunicipios()

    
