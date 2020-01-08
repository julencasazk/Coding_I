class Empleado:

    def __init__(self, nombre, sueldo, code, puntos):
        self.__nombre = 'nombre'
        self.setNombre(nombre)
        self.__sueldo = 1000
        self.setSueldo(sueldo)
        self.__code = 'AB44B'
        self.setCode(code)
        self.__puntos = 0
        self.setPuntos(puntos)
    
    def esCorrecto(self, ncode):
        oficinas = ["ER","EI","ME","DB"]
        if isinstance(ncode, str) and ncode[0:2] in oficinas and ncode[2:4] in range(0,100) and ncode[4] in ["A","B","C","D"]
            return True
        else:
            return False
    
    def getNombre(self):
        return self.__nombre

    def getSueldo(self):
        return self.__sueldo
    
    def getCode(self):
        return self.__code
    
    def getPuntos(self):
        return self.__puntos
    
    def getOficina(self):
        return self.__code[0:2]
    
    def getCodigoNum(self):
        return self.__code[2:4]
    
    def getRango(self):
        return self.__code[-1]
    
    def setNombre(self, nnombre):
        if isinstance(nnombre, str) and len(nnombre) >= 5:
            self.__nombre = nnombre

    def setSueldo(self, nsueldo):
        if isinstance(nsueldo, int) and nsueldo >= 600 and nsueldo <= 2400:
            self.__sueldo = nsueldo
    
    def setCode(self, ncode):
        if esCorrecto(ncode):
            self.__code = ncode

    def setPuntos(self, npuntos):
        if isinstance(npuntos, int):
            self.__puntos = npuntos

class GestionPagaExtra:

    def __init__(self, vEmpleados):
        self.__vEmpleados = vEmpleados
