def esCorrecto(self, ncode):
    oficinas = ["ER","EI","ME","DB"]
    if isinstance(ncode, str) and ncode[0:2] in oficinas and ncode[2:4] in range(0,100) and ncode[4] in ["A","B","C","D"]
        return True
    else:
        return False


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

class Operacion:

    def __init__(self, codigo, tipo, importe):
        self.__codigo = codigo
        self.__importe = importe
        self.__tipo = tipo
    
    def getCodigo(self):
        return self.__codigo

    def getTipo(self):
        return self.__tipo
    
    def getImporte(self):
        return self.__importe
    
    def setCodigo(self,n):
        self.__codigo = n 

    def setTipo(self,n):
        self.__tipo = n
    
    def setImporte(self,n):
        self.__importe = n
    
class GestionPagaExtra:

    def __init__(self, vEmpleados, vOperaciones):
        self.__vEmpleados = vEmpleados
        self.__vOperaciones = vOperaciones
    

    def cargarOperaciones(self):
        correct = False
        correct2 = False
        correct3 = False
        respuesta = ''
        code = ''
        tipo = ''
        importe = 0
        empleadocodelist = []
            for worker in self.__vEmpleados:
                empleadocodelist.append(worker.getCode())
        while respuesta.upper() != "N"
            while correct != False:
                print("Introduce codigo de empleado, formato XX99X:")
                ncodigo = str(input())
                if not esCorrecto(ncodigo):
                    print("El formato del código no es correcto!")
                elif ncodigo not in empleadocodelist:
                    print(f"El empleado con su codigo no existe!")
                else:
                    correct = True
            code = ncodigo

            while correct2 != True:
                print("Introduzca el tipo de la operación"):
                ntipo = str(input())
                if ntipo.upper() not in ["H","F","C","P"]:
                    print("Valor incorrecto!")
                else:
                    correct2 = True
            tipo = ntipo

            while  correct3 != True:
                print("Introduce importe: "):
                nimporte = int(input())
                if nimporte <= 0:
                    print("No es un valor válido para un importe!")
                else:
                    correct3 = True
            importe = nimporte
            self.__vOperaciones.append(Operacion(code, tipo, importe))
            print("Hecho!")
            print("Quiere introducir otra operacion? [Y/N]")
            respuesta = str(input())

    def asignarPuntos(self):
        for operation in self.__vOperaciones:
            for worker in self.__vEmpleados:
                if operation.getCodigo() == worker.getCode():
                    if operation.getTipo() == "H":
                        worker.setPuntos(operation.getImporte * 3)
                    elif operation.getTipo() == "F":
                        worker.setPuntos(operation.getImporte)
                    elif operation.getTipo() == "C":
                        worker.setPuntos(operation.getImporte * 0.02)
                    elif operation.getTipo() == "P":
                        worker.setPuntos(operation.getImporte * 0.002)
    
    def puntosPorSucursalTipo(self):

        ermua = 0
        eibar = 0
        mendaro = 0
        deba = 0

        for worker in self.__vEmpleados:
            if worker.getOficina() == "ER":
                ermua += worker.getPuntos()
            elif worker.getOficina() == "EI":
                eibar += worker.getPuntos()
            elif worker.getOficina() == "ME":
                mendaro += worker.getPuntos()
            else:
                deba += worker.getPuntos()
        
        print(f"Puntos: Eibar({eibar}), Ermua({ermua}), Mendaro({mendaro}), Deba({deba})")
    
    def asignarPagaExtra(self):
        
        listapuntos = []
        tiers = ["A","B","C","D"]
        

        for worker in self.__vEmpleados:
            listapuntos.append(worker.getPuntos())
        
        
        print("Paga extra de 1000 euros para los siguientes empleados: ")
        for i in range(4):
            empleado = 0
            for worker in self.__vEmpleados:
                if sorted(listapuntos)[i] == worker.getPuntos():
                    print(f"{tiers[i]} - {worker.getNombre()} - {sorted(listapuntos)[i]}")
        
    




