#_______________Program_______________________________________________
class Subject():

    def __init__(self, name, code, course, credit):
        self.__name = name
        self.__code = code
        self.__course = course
        self.__credit = credit
    
    def getName(self):
        return self.__name

    def getCode(self):
        return self.__code


class Student():
    
    def __init__(self, sname, sid, scourse, asignaturas):
        self.__sname = sname
        self.__sid = sid
        self.__scourse = scourse
        self.__asignaturas = asignaturas
        self.__matricula = []
    
    def __str__(self):
        return f"Nombre: {self.__sname}, DNI: {self.__sid}, Curso: {self.__scourse}, Matrícula: {self.__matricula}"

    def matricular(self, subcode):
        for i in range(0,len(self.__asignaturas)):
            if (self.__asignaturas[i].getCode()) == subcode:
                self.__matricula.append(self.__asignaturas[i])

    def desmatricular(self, subcode):
        for i in range(0,len(self.__asignaturas)):
            if (self.__asignaturas[i].getCode()) == subcode:
                self.__matricula.remove(self.__asignaturas[i])

#________________Testing______________________________________________
Mat = Subject("Calculo", 5555, 1, 6)
Alg = Subject("Algebra", 4444, 1, 6)
Ico = Subject('Introduccion a Computadoras', 3333, 1, 6)
Ade = Subject("Administracion de Empresas", 2222, 1, 3)
asig = [Mat, Alg, Ico, Ade]

bruh = Student("Brunicio Skere", "790790790790H", 1, asig)
print(bruh)
bruh.matricular(5555)
bruh.matricular(4444)
bruh.matricular(3333)
bruh.matricular(2222)
print(bruh)
bruh.desmatricular(5555)
bruh.desmatricular(3333)
print(bruh)
        
