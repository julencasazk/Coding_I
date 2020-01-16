class Vehicle():
    def __init__(self, brand, vid, model, user, hp, mileage):
        self.__brand = brand
        self.__vid = vid
        self.__model = model 
        self.__user = user
        self.__hp = hp
        self.__mileage = mileage
    
    def getbrand(self):
        return self.__brand

    def getvid(self):
        return self.__vid

    def getmodel(self):
        return self.__model

    def getuser(self):
        return self.__user
    
    def gethp(self):
        return self.__hp

    def getmileage(self):
        return self.__mielage
    
    def setbrand(self, n):
        if isinstance(n, str):
            self.__brand = n
    
    def setvid(self, n):
        if isinstance(n, str):
            self.__vid = n

    def setmodel(self, n):
        if isinstance(n, str):
            self.__model = n

    def setuser(self, n):
        if isinstance(n, str):
            self.__user = n
    
    def sethp(self, n):
        if isinstance(n, int):
            self.__hp = n
    
    def setmileage(self, n):
        if isinstance(n, float):
            self.__mileage = n

class Floor():
    def __init__(self, fid, vclist, lots):
        self.__fid = fid
        self.__vclist = vclist
        self.__lots = lots
    
    def __str__(self):
        return f'Planta {self.__fid} ({len(self.__vclist)} vehiculos, {((self.__lots) - (len(self.__vclist)))} plazas libres)'
    
    def setlots(self, n):
        if isinstance(n, int):
            self.__lots = n
    
    def setfid(self, n):
        if isinstance(n, int):
            self.__fid = n
    
    def setvclist(self, n):
        if isinstance(n, list):
            self.__vclist = n

    def getlots(self, n):
        return self.__lots
    
    def getfid(self):
        return self.__fid
    
    def getvclist(self):
        return self.__vclist

    
    def getvcquant(self):
        return len(self,__vclist)

    def getFreeLots(self):
        return ((self.__lots) - (len(self.__vclist)))
    
    def getFullPercent(self):
        return (((self.__lots) - (len(self.__vclist))) / (self.__lots))

class DeusPark():
    def __init__(self, flquant, lotsperfl):
        self.__park = []
        self.__flquant = flquant
        self.__lotsperfl = lotsperfl
        for i in range(0, floorquant):
            self.__park.append(Floor(i, [], self.__lotsperfl))

    def poblarParking(self, vehiclelist):
        for i in range(0, len(self.__park)):
            x = 0
            cars = []
            while self.__park[i].getFreeLots() != 0:
                cars.append(vehiclelist[x])
                vehiclelist.remove(vehiclelist[x])
                self.__park[i].setvclist(cars)
                x = x + 1
    
    def getNumeroVehiculos(self):
        CarQuant = 0
        for i in range(0, len(self.__park)):
            for x in range(0, len(self.__park[i].getvclist())):
                CarQuant = CarQuant + 1
        return CarQuant
    
    def mostrarPorcentajeOcupacion(self):
        TotalFreeLots = 0
        for i in range(0, len(self.__park)):
            TotalFreeLots = TotalFreeLots + self.__park[i].getFreeLots()
        return (TotalFreeLots/(self.__flquant * self.__lotsperfl))
    
    def buscarMasPotente(self):
        MasPotenteLista = []
        MaxPotence = 0
        for i in range(0, len(self.__park)):
            hplist = []
            for x in range(0, len(self.__park[i].getvclist())):
                hplist.append((self.__park[i].getvclist())[x].gethp())
            for y in range(0, len(self.__park[i].getvclist())):
                if max(hplist) == (self.__park[i].getvclist())[y].gethp():
                    MasPotenteLista.append((self.__park[i].getvclist())[y])
        cvlist = []
        for z in range(0, len(MasPotenteLista)):
            cvlist.append(MasPotenteLista[z].gethp())
        for b in range(0, len(MasPotenteLista)):
            if max(cvlist) == (MasPotenteLista[b].gethp()):
                MaxPotence = MasPotenteLista[b]
        return MaxPotence
    
    def consumoMedioPorPlanta(self):
        avglist = []
        for i in range(0, self.__flquant):
            totalcons = 0
            for x in range(0, len(self.__park[i].getvclist())):
                totalcons = totalcons + (self.__park[i].getvclist())[x].getmileage()
            avglist.append( totalcons / (self.__park[i].getvcquant()))
        return avglist
    
    def consumoMedioPorMarca(self, marca):
        consumtot = 0
        caramm = 0
        for i in range(0, self.__flquant):
            consumoporplanta = 0
            carporplanta = 0
            for x in range(0, len(self.__park[i].getvclist())):
                if (self.__park[i].getvclist())[x].getbrand() == marca:
                    consumoporplanta = consumoporplanta + (self.__park[i].getvclist())[x].getmileage()
                    carporplanta = carporplanta + 1
            consumtot = consumtot + consumoporplanta
            caramm = caramm + carporplanta
        return (consumtot / carmm)


 #sinceramente me da tremenda pereza probarlo con los vehiculos que da el examen, bruh           
