aPlanetas = ["Tatooine","Dagobah","Jakku","Naboo"]
aRutas = []
aContObservaciones = [[0,2,0,5],[1,0,3,1],[2,1,2,3],[3,0,0,0]] #En orden: Tatooine, Dagobah, Jakku, Naboo

class Ruta:

    def __init__(self, origen, destino, controladaPrimeraOrden):
        self.__origen = origen
        self.__destino = destino
        self.__controladaPrimeraOrden = controladaPrimeraOrden

    
class Observacion:

    def __init__(self, planeta, rutaOrigen, rutaDestino, descripcionObservacion, fechaObservacion):

        self.__planeta = planeta
        self.__rutaOrigen = rutaOrigen
        self.__rutaDestino = rutaDestino
        self.__descripcionObservacion = descripcionObservacion
        self.__fechaObservacion = fechaObservacion
    
    def getPlaneta(self):
        return self.__planeta

    def getRutaOrigen(self):
        return self.__rutaOrigen
    
    def getRutaDestino(self):
        return self.__rutaDestino

    def getDescripcionObservacion(self):
        return self.__descripcionObservacion
    
    def getFechaObservacion(self):
        return self.__fechaObservacion


    def setPlaneta(self, n):
        if isinstance(n, str) and len(n) != 0:
            self.__planeta = n

    def setRutaOrigen(self, n):
        if isinstance(n, str):
            self.__rutaOrigen
    
    def setRutaDestino(self, n):
        if isinstance(n, str):
            self.__rutaDestino

    def setDescripcionObservacion(self, n):
        if isinstance(n, str):
            self.__descripcionObservacion
    
    def setFechaObservacion(self, n):
        if isinstance(n, int) and len(n) == 8:    #Formato aaaammdd incluyendo 0 para dias y meses de digito único
            self.__fechaObservacion
    
    def __str__(self):
        return f"Observacion en fecha {self.__fechaObservacion} (aaaammdd), en el planeta {self.__planeta}, ruta mercante {self.__rutaOrigen}-{self.__rutaDestino}, {self.__descripcionObservacion}"

    
def actualizarObservaciones(self, sights, planets, biarray): #sights es un array con observaciones recientes que se usará para añadir +1 al array bidimensional biarray
    for sight in sights:                  #0: Tatooine, 1: Dagobah, 2: Jakku, 3: Naboo
        for i in range(0, len(planets)):
            for x in range(0, len(planets)):
                if sight.getRutaDestino() == planets[x] and sight.getRutaOrigen() == planets[i]:
                    biarray[i][x] += 1

class Gestion:
    
    def __init__(self):
        self.__aObservaciones = []

    def cargarObservaciones(self):
        templist = []
        fechaslist = []
        fixedlist = []

        respuesta = ""
        while respuesta != "N":
            print("Nueva observacion: ")
            print("Planeta donde se vio a Skywalker: ")
            nPlaneta = str(input())
            print("Planeta origen de la ruta en curso: ")
            nRutaOrigen = str(input())
            print("Planeta destino de la ruta en curso: ")
            nRutaDestino = str(input())
            print("Breve descripción de la observación (con máximo detalle): ")
            nDescripcion = str(input())
            print("Fecha entera de la observación (formato aaaammdd, incluye ceros):")
            nFecha = int(input())
            listaFechas.append(nFecha)
            templist.append(Observacion(nPlaneta, nRutaOrigen, nRutaDestino, nDescripcion, nFecha))
            print("Introducir otra observación? [Y/N]")
            respuesta = str(input())

        for sight in templist:
            fechaslist.append(sight.getFechaObservacion())
        for i in range(0, len(fechaslist)):
            fixedlist.append(max(fechaslist))
            fechaslist.remove(max(fechaslist))
        for fecha in fixedlist:
            for sight in templist:
                if sight.getFechaObservacion() == fecha:
                    self.__aObservaciones.append(sight)
    
            

        



                                 




