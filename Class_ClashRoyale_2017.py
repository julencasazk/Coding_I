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
        
        def __init__(self, jugadores, cartas):
            self.__jugadores = jugadores
            self.__cartas = cartas
            self.__listacartas = []
            for carta in cartas:
                self.__listacartas.append(carta.getNombre())

        def crearJugadores(self):
            salir = ""
            while int(salir) != 1:
                print("Introduce el nombre de tu nuevo jugador: ")
                nombre_jugador = str(input())
                print("Introduce el numero de trofeos de tu jugador: ")
                trofeos_jugador = int(input())
                print("Establece el nivel del jugador: ")
                nivel_jugador = int(input())
                self.__jugadores.append(Jugador(nombre_jugador, trofeos_jugador, nivel_jugador, []))
                print("Hecho. ¿Quiere introducir cartas a su baraja? [1] Si, [2] No")
                elec1 = int(input())
                if elec1 == 1:
                    elec2 = 0
                    while elec2 != 1:
                        print("")
                        print(f"Lista de cartas disponibles: {self.__listacartas}")
                        print("Escribe el nombre de la carta: ")
                        nombre_carta = str(input())
                        for carta in self.__cartas:
                            if nombre_carta.lower() == carta.getNombre():
                                self.__jugadores[-1].setBaraja(self.__jugadores[-1].getBaraja().append(carta))
                        print("Terminar de introducir cartas? [1] Si, [2] No")
                        elec2 = int(input())
                print("Salir de introducir jugador? [1] Si, salir [2] Introducir otro jugador")

        
