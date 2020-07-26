from threading import Thread
import time

class observable(object):       #Se declara el comstructor del Observable
    def __init__(self):
        self._observers = set()

    def agregarObserver(self, observer):        #Un metodo destinado a agreagar a los observer
        self._observers.add(observer)

    def notificaObservers(self, event):         #El que utilizamos para realizar la notificación a todos los Observer
        for observer in self._observers:
            observer.update(self, event)


class observer(object):
    def update(self, observable, event):
        raise NotImplemented('X') # Metodo no necesario, ya que Python tiene "duck typing""


class myObservable(Thread, observable):
    def __init__(self, *args, **kargs):
        Thread.__init__(self, *args, **kargs)
        observable.__init__(self, *args, **kargs)
        self._finish = False

    def run(self): #En ejecución mientras no haya terminado va a seguir disparando el evento
        while not self._finish: #En este ejemplo como no tenemos parametros de cantidad
            self.disparador()   #Se utiliza un parametro definiendo un tiempo de disparo
            time.sleep(0.1)

    def disparador(self):       
        self.notificaObservers("Se han ralizado cambios")

    def stop(self):
        self._finish = True


class myObserver(observer): #Notificacion para cada Observer
    def update(self, observable, event):
        print ("Cambios realizados")