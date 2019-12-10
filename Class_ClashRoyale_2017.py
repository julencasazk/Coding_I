class Carta:
    
    def __init__(self, nombre, coste, vida, ataque):
        self.__nombre = nombre
        self.__coste = coste
        self.__vida = vida
        self.__ataque = ataque
    
    def __str__(self):
        return f""

    def getNombre(self):
        return self.__nombre

    def getCoste(self):
        return self.__coste

    def getVida(self):
        return self.__vida
    
    def getAtaque(self):
        return self.__ataque

    def setNombre(self, nnombre):
        if isinstance(nnombre, str):
            self.__nombre = nnombre
    def setCoste(self, ncoste):
        if isinstance(ncoste, int) and ncoste >= 0:
            self.__coste = ncoste
        
    def setVida(self, nvida):
        if isinstance(nvida, int) and nvida >= 0:
            self.__vida = nvida

    def setAtaque(self, nataque):
        if isinstance(nataque, int) and nataque >= 0:
            self.__ataque = nataque
