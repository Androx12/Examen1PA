class nodo:
    def __init__(self, dato = None):
        self.dato = dato
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = nodo()

    def append(self, dato):
        nuevoNodo = nodo(dato)
        cursor = self.head
        while cursor.next != None:
            cursor = cursor.next
        cursor.next = nuevoNodo

    def length(self):
        cursor = self.head
        total = 0
        while cursor.next != None:
            total+=1
            cursor = cursor.next
        return total
    
    def mostrar(self):
        elementos = []
        cursorNodo = self.head
        while cursorNodo.next != None:
            cursorNodo = cursorNodo.next
            elementos.append(cursorNodo.dato)
        print(elementos)

    def get(self, index):
        if index >= self.length():
            msj = 'Error "GET" fuera del rango de index'
            return msj
        cursorIndex = 0
        cursorNodo = self.head
        while True:
            cursorNodo = cursorNodo.next
            if cursorIndex == index:
                return cursorNodo.dato
            cursorIndex+=1

    def borrar(self, index):
        if index >= self.length():
            msj = 'Error "borrar" fuera del rango de index'
            return msj
        cursorIndex = 0
        cursorNodo = self.head
        while True:
            nodoAnterior = cursorNodo
            cursorNodo = cursorNodo.next
            if cursorIndex == index:
                nodoAnterior.next = cursorNodo.next
                return
            cursorIndex+=1
