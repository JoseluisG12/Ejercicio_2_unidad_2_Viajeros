from claseViajero import Viajero
import csv

class ManejadorViajeros():
    __viajeros = []

    def __init__(self):
        self.__viajeros = []
    def cargarDatos(self):
        archivo = open('viajeros.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            numero = fila[0]
            dni = fila[1]
            nombre = fila[2]
            apellido = fila[3]
            millas = fila[4]
            via = Viajero(numero, dni, nombre, apellido, millas)
            self.__viajeros.append(via)

        archivo.close()


    def getViajero(self, num):

        retorno = None

        band = False
        i = 0

        while (not band and (i < len(self.__viajeros))):

            if self.__viajeros[i].getnumero() == num:
                retorno = i
                band = True
            i += 1

        return retorno

    def menu(self):

        b = 0

        num = int(input("ingrese el numero del viajero\n"))

        dato = self.getViajero(num)

        while b != 4:

            print("ingrese 1 para saber la cantidad de millas disponibles del cliente")
            print("ingrese 2 para acumular las millas nuevas")
            print("ingrese 3 para canjear  millas ")


            b = int(input())
            if (dato == None):
                print("no se encontro el numero de viajero")
                num = int(input("ingrese el numero del viajero de nuevo\n"))
                dato = self.getViajero(num)

            elif (b == 1):
                print("la cantidad total de millas disponibles es:",self.__viajeros[dato].CantidaTotalMillas())

            elif (b == 2):
                millas = int(input("ingrese las millas nuevas a guardar\n"))
                print("la cantidad de millas totales son: {}".format(self.__viajeros[dato].AcumularMillas(millas)))

            elif (b == 3):
                millasacanjear = int(input("ingrese la cantidad de millas a canjear.\n"))
                milla = self.__viajeros[dato].CanjearMillas(millasacanjear)
                if milla != None:
                    print("millas restantes: {}".format(milla))
                else:
                    print("cantidad de millas insuficientes.\n millas totales: ",self.__viajeros[dato].CantidaTotalMillas())

            b = int(input("ingresar algun numero para reingresar o 4 para salir \n"))


