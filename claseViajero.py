
class Viajero:
    __numero_viajero = ''
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = ''

    def __init__(self,x = 'numero',y = 'dni',z = 'nombre',w = 'apellido',f = 'millas'):
        self.__numero_viajero = int(x)
        self.__dni = int(y)
        self.__nombre = z
        self.__apellido = w
        self.__millas_acum = int(f)

    def getNombre(self):
        return self.__nombre
    def CantidaTotalMillas(self):
        return self.__millas_acum

    def AcumularMillas(self,millas):
        self.__millas_acum += millas
        return self.__millas_acum

    def CanjearMillas(self,millascanjear):
        if millascanjear <= self.__millas_acum:
            self.__millas_acum = self.__millas_acum - millascanjear
            return self.__millas_acum
        else:
            return None
    def mostrardatos(self):
        print('numero de viajero: {},dni: {},nombre: {},apellido: {},millas acumuladas: {}'.format(self.__numero_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum))

    def getnumero(self):
        return self.__numero_viajero
