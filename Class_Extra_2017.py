class Extra:

    def __init__(self, nombre, precio, promocion):
        self.__nombre = nombre
        self.__precio = precio
        self.__promocion = promocion
    
    def __str__(self):
        return f"{self.__nombre}: {self.__precio} Euros, de promocion {self.__promocion}"
    
    def getNombre(self):
        return self.__nombre

    def getPrecio(self):
        return self.__precio
    
    def getPromocion(self):
        return self.__promocion
    
    def setNombre(self, nnombre):
        if isinstance(nnombre, str):
            self.__nombre = nnombre
    
    def setPrecio(self, nprecio):
        if isinstance(nprecio, float) and nprecio >= 0:
            self.__precio = nprecio

    def setPromocion(self, npromocion):
        if isinstance(npromocion, float) and npromocion >= 0:
            self.__promocion = npromocion

class Coche:

    def __init__(self, modelo, motor, pintura, descapotable, extras):
        self.__modelo = modelo
        self.__motor = motor
        self.__pintura = pintura
        self.__descapotable = descapotable
        self.__isroofless = 'con techo'
        if self.__descapotable:
            self.__isroofless = 'descapotable'
        self.__extras = extras
        self.__nombreExtras = ''
        for extra in self.__extras:
            self.__nombreExtras = f'{self.__nombreExtras}, {extra.getNombre()}'

    def __str__(self):
        return f'Coche '

    def getModelo(self):
        return self.__modelo

    def getMotor(self):
        return self.__motor

    def getPintura(self):
        return self.__pintura

    def getDescapotable(self):
        return self.__descapotable

    def getExtras(self):
        return self.__extras

    def setModelo(self, nmodelo):
        if modelo in [0,1,2,3]:
            self.__modelo = nmodelo
    
    def setMotor(self, nmotor):
        if nmotor in [0,1,2,3]:
            self.__motor = nmotor

    def setPintura(self, npintura):
        if npintura in ['rojo','negro','azul','azul metalizado','gris metalizado']:
            self.__pintura = npintura

    def setDescapotable(self, ndescapotable):
        if isinstance(ndescapotable, bool):
            self.__descapotable = ndescapotable

    def setExtras(self, nextras):
        if isinstance(nextras, list):
            self.__extras = nextras
