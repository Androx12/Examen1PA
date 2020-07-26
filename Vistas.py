import msvcrt

class vistasMenu:

    def __init__ (self): #Menús de vistas que se utilizan en el flujo como menús
        self.SaltoLinea =   ""

    def mInicio_Programa(self):
        print( self.SaltoLinea + "\n" + "\n" +"Bienvenido al sistema de RIFA ALEATORIA")

    def mFin_Programa(self):
        print("************************************")
        print( "\n" + self.SaltoLinea + "Gracias por usar el Sistema de RIFA ALEATORIA")
        print("\n")
        print("************************************")


    def mOpcionesMenu(self):
        print("")
        print("*----*----*----*----*----*----*----*")
        print("| 1. Ingresar al Menú.             |")
        print("| 2. Salir del programa.           |")
        print("*----*----*----*----*----*----*----*")
        print("")

    def mOpcionesMenuInterno(self):
        print("")
        print("*----*----*----*----*----*----*----*")
        print("| 1. Registrar participante.       |")
        print("| 2. Eliminar participante.        |")
        print("| 3. Realizar sorteo.              |")
        print("*----*----*----*----*----*----*----*")
        print("")
    
    def mConfirmar(self):
        print("")
        print("*------*------*------*-----*-----*------*------*")
        print("| Si está seguro presione 1 de lo contrario 2  |")
        print("|                                              |")
        print("| 1. Confirmar.                                |")
        print("| 2. Volver.                                   |")
        print("*------*------*------*-----*-----*------*------*")
        print("")

    def mDiezLineas(self):
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")

    
    def mContinuar(self):
        print("")
        print("")
        print("Presiones 'C' para volver al menú del sistema.")
        key = None
        while key != 'C':           #Hasta que no se presione 'C' no permite la entrada de datos
            key = msvcrt.getwch()   #como un HANDLE de .Net