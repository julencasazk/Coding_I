class Carta:
    
    def __init__(self, nombre, coste, vida, ataque):
        self.__nombre = nombre
        self.__coste = coste
        self.__vida = vida
        self.__ataque = ataque
    
    def __str__(self):
        return f"{self.__nombre}, Coste: {self.__coste}, Vida: {self.__vida}, Ataque: {self.__ataque}"

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

class Jugador:
    def __init__(self, nombre, trofeos, nivel, baraja):
        self.__nombre = nombre
        self.__trofeos = trofeos
        self.__nivel = nivel
        self.__baraja = baraja
    
    def getNombre(self):
        return self.__nombre

    def getTrofeos(self):
        return self.__trofeos
    
    def getNivel(self):
        return self.__nivel

    def getBaraja(self):
        return self.__baraja
    
    def setNombre(self, nnombre):
        if isinstance(nnombre, str):
            self.__nombre = nnombre
        
    def setTrofeos(self, ntrofeos):
        if isinstance(ntrofeos, int) and ntrofeos >= 0:
            self.__trofeos = ntrofeos
    def setNivel(self, nnivel):
        if isinstance(nnivel, int) and nnivel >= 0:
            self.__nivel = nnivel

    def setBaraja(self, nbaraja):
        if isinstance(nbaraja, list):
            self.__baraja = nbaraja

    def consumoMedioElixir(self):
        lista_consumos = []
        for carta in self.__baraja:
            lista_consumo.append(carta.getCoste())
        return (sum(lista_consumo)/len(lista_consumo))

    class ClashRoyale:
        
        def __init__(self, jugadores):
            self.__jugadores = jugadores

        def crearJugadores(self):
            
