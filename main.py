from ManejadorViajeros import ManejadorViajeros
from claseViajero import Viajero
def test():
    opc = int(input("desea probar los metodos con datos 1 = correctos 2 = incorrectos 3 = salir test\n"))
    while opc != 3:
        if opc == 1:
            viajerocorrecto = Viajero('1234', '41230328', 'julian', 'alvarez', '10000')
            print("""
            Viajero:{}
            Numero: {}
            Cantidad de millas acumuladas: {}
            """.format(viajerocorrecto.getNombre(), viajerocorrecto.getnumero(), viajerocorrecto.CantidaTotalMillas()))
            millas = int(input("ingrese la cantidad de millas a acumular\n"))
            viajerocorrecto.AcumularMillas(millas)
            viajerocorrecto.mostrardatos()
            millas = int(input("ingrese la cantidad de millas a canjear\n"))
            viajerocorrecto.CanjearMillas(millas)
            viajerocorrecto.mostrardatos()
        if opc == 2:
            viajerocorrecto = Viajero('unodostrescuatro', '41230328', 'julian', 'alvarez', 'abc')
            print("""
               Viajero:{}
               Numero: {}
               Cantidad de millas acumuladas: {}
               """.format(viajerocorrecto.getNombre(), viajerocorrecto.getnumero(),viajerocorrecto.CantidaTotalMillas()))
            millas = int(input("ingrese la cantidad de millas a acumular\n"))
            viajerocorrecto.AcumularMillas(millas)
            viajerocorrecto.mostrardatos()
            millas = int(input("ingrese la cantidad de millas a canjear\n"))
            viajerocorrecto.CanjearMillas(millas)
            viajerocorrecto.mostrardatos()
        opc = int(input("desea probar los metodos con datos 1 = correctos 2 = incorrectos 3 = salir test\n"))



if __name__ == '__main__':
    opc = input("""desea hacer un test antes de iniciar el programa
Ingrese y = SI  n = NO\n""")
    if opc == 'y':
        test()
    print("_____main______")
    viajeros = ManejadorViajeros()
    viajeros.cargarDatos()
    viajeros.menu()












