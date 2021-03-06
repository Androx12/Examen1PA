from LinkedList import linkedlist
from Vistas import vistasMenu
from ObservationalPatter import myObservable
from ObservationalPatter import myObserver
import time
import random
import msvcrt

class ejecucionSistemaControl:

    objLinkedList = linkedlist()
    Obj_VistaMenu = vistasMenu()

    def __init__(self):
        self.Obj_VistaMenu.mInicio_Programa()

    def CorrerPrograma(self):
        
        BanderaPrograma = True
        sEntrada_Usuario = None
        sEntrada_Interna = None

        while BanderaPrograma == True:  #Se crea un ciclo para mantener el flujo validando con (BanderaPrograma)

            try:
                print('Programa de RIFA ALEATORIA')
                self.Obj_VistaMenu.mOpcionesMenu() #Se trae la vista de el Menú
                sEntrada_Usuario = input("Seleccione una opción de Menú --> ")
                
                if (sEntrada_Usuario == '1'): #Flujo en 1

                    self.Obj_VistaMenu.mDiezLineas()
                    self.Obj_VistaMenu.mOpcionesMenuInterno() #Se trae la vista de el Menú interno

                    sEntrada_Interna = input("Seleccione una opción de Menú --> ")

                    if sEntrada_Interna == '1':

                        self.Obj_VistaMenu.mDiezLineas()
                        sReistro = input("Ingrese el nombre del participante: \n")
                        self.objLinkedList.append(sReistro)
                        print('')
                        total = self.objLinkedList.length() #El deletro de cantidad lo utilizamos para imprimir el valor de NODO
                        print('En este momento tenemos un total de {} participantes \n'.format(total))
                        print('Esta es la lista de TODOS los participantes \n')
                        self.objLinkedList.mostrar()
                        self.Obj_VistaMenu.mContinuar()
                    else:
                        if sEntrada_Interna == '2':
                            
                            bBanderaCiclo = False
                            
                            while(not bBanderaCiclo):

                                self.Obj_VistaMenu.mDiezLineas()
                                total = self.objLinkedList.length() #El deletro de cantidad lo utilizamos para imprimir el valor de NODO
                                print('En este momento tenemos un total de {} participantes \n'.format(total))
                                print('Esta es la lista de TODOS los participantes \n')
                                self.objLinkedList.mostrar()
                                print('')
                                print('')

                                bCorrecto = False
                                while(not bCorrecto):
                                    try:
                                        iIndex = int(input("Ingrese el numero del participante que desea eliminar: \n"))
                                        bCorrecto = True
                                    except ValueError:
                                        print("")
                                        print('Error, introduce un numero entero \n')
                                self.Obj_VistaMenu.mDiezLineas()




                                print('El participante que desea eliminar es: {}'.format(self.objLinkedList.get(iIndex)))
                                self.Obj_VistaMenu.mConfirmar()
                                sConfiramar = input("Seleccione una opción de Menú --> ")
                                if sConfiramar == '1':
                                    bBanderaCiclo = True
                                    self.objLinkedList.borrar(iIndex)
                                    self.Obj_VistaMenu.mDiezLineas()
                                    total = self.objLinkedList.length()
                                    print('En este momento tenemos un total de {} participantes \n'.format(total))
                                    print('Esta es la lista de TODOS los participantes \n')
                                    self.objLinkedList.mostrar()
                                    self.Obj_VistaMenu.mContinuar()
                                    self.Obj_VistaMenu.mDiezLineas()
                                else:
                                    if sConfiramar == '2':
                                        bBanderaCiclo = False
                                        self.Obj_VistaMenu.mDiezLineas()
                                    else:
                                        bBanderaCiclo = False
                                        self.Obj_VistaMenu.mDiezLineas()
                                        print('Entrada invalida.')
                                        print("Las opciones del Menú son '1' y '2'.")
                                        print("Presione 'C' para voler al Menú")
                                        key = None
                                        while key != 'C':           #Hasta que no se presione 'C' no permite la entrada de datos
                                            key = msvcrt.getwch()   #como un HANDLE de .Net
                                        self.Obj_VistaMenu.mDiezLineas()
                        else:
                            if sEntrada_Interna == '3':

                                self.Obj_VistaMenu.mDiezLineas()
                                total = self.objLinkedList.length() #Estblecer limite para random
                                print('En este momento tenemos un total de {} participantes \n'.format(total))
                                print('Esta es la lista de TODOS los participantes \n')
                                self.objLinkedList.mostrar()
                                print('')
                                iGanador = (random.randrange(total)) #Utilizamos la libreria random para seleccionar un ganador
                                print('El ganador de el premio es: {}'.format(self.objLinkedList.get(iGanador)))
                                print('')
                                self.Obj_VistaMenu.mContinuar()

                            else:
                                self.Obj_VistaMenu.mDiezLineas()
                                print('Entrada invalida.')
                                print("Las opciones del Menú interno son '1', '2' o '3'.")
                                print("Presione 'C' para voler al Menú Principal")
                                key = None
                                while key != 'C':           #Hasta que no se presione 'C' no permite la entrada de datos
                                    key = msvcrt.getwch()   #como un HANDLE de .Net
                                self.Obj_VistaMenu.mDiezLineas()


                else:
                    if sEntrada_Usuario == '2':  #Flujo en S
                        self.Obj_VistaMenu.mDiezLineas()
                        self.Obj_VistaMenu.mFin_Programa() #Vista de Salida
                        BanderaPrograma = False

                        ObjObservable = myObservable()  #Como creamos las clases Observable y Observer por aparte
                        objObserver = myObserver()      #Ahora solo tenemos que instanciarlas

                        ObjObservable.agregarObserver(objObserver)  #Llamamos al metodo de agragar al observador
                                                                    #para poder ejecutarlo
                        ObjObservable.start()   #Se inicia el patrón y sedefine un tiempo de ejecucion de 2
                        time.sleep(2)           #segundos como parametro ya que no tenemos otro parametro
                        ObjObservable.stop()    #que no sea tiempo, despues de eso lo detenemos
                                                #en el metodo que dispara el evento 'Disparador' se ejecuta siempre y cuando el
                                                #STOP no haya PUESTO UN FINISH  a la condicion de WHILE

                        print("Final del Patrón Observational")

                    else:                       #Otra entrada genera un flujo de error para obligar al usuario
                        BanderaPrograma = True  #a ingresar los datos dentro del menú
                        self.Obj_VistaMenu.mDiezLineas()
                        print('Entrada invalida.')
                        print("Las opciones del Menú son '1' y '2'.")
                        print("Presione 'C' para voler al Menú")
                        key = None
                        while key != 'C':           #Hasta que no se presione 'C' no permite la entrada de datos
                            key = msvcrt.getwch()   #como un HANDLE de .Net
                        self.Obj_VistaMenu.mDiezLineas()
            except:
                pass