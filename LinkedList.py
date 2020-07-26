class nodo:
    def __init__(self, dato = None): # Se inicializa la clase con un costructor para el NODO
        self.dato = dato
        self.next = None

class linkedlist:  # A la clase linkedlist le asignamos un HEAD que va a ser la clase NODO
    def __init__(self):
        self.head = nodo()

    def append(self, dato):  #AgrEgar datos
        nuevoNodo = nodo(dato)
        cursor = self.head
        while cursor.next != None: # Pregunta en el NODO si el next existe
            cursor = cursor.next   # Asignamos el valor de cursor para referenciar nuestro proximo dato
        cursor.next = nuevoNodo    # El siguiente dato siempre será el nuevo dato

    def length(self): # Metodo utilizado unicamente para recorrer la lista y saber cuantos nodos tenemos
        cursor = self.head
        total = 0
        while cursor.next != None:
            total+=1
            cursor = cursor.next
        return total
    
    def mostrar(self):  # Metodo para imprimir los nodos vamos creando una lista agregando los 
        elementos = []  # valores de los NEXT
        cursorNodo = self.head
        while cursorNodo.next != None:
            cursorNodo = cursorNodo.next
            elementos.append(cursorNodo.dato)
        print(elementos)

    def get(self, index): # Para obtener los datos de cada nodo primero utilizamos el metodo contador
        if index >= self.length():
            msj = 'Error "GET" fuera del rango de index' # Así podemos saber si el INDEX que esta pidiendo realmente existe
            return msj
        cursorIndex = 0
        cursorNodo = self.head
        while True: 
            cursorNodo = cursorNodo.next    # En caso de que si exista
            if cursorIndex == index:        # El cursos busca el numero de INDEX y retorna el valor almacenado
                return cursorNodo.dato      # en el NODO
            cursorIndex+=1

    def borrar(self, index):    # Para borrar la logica funciona igual que el get
        if index >= self.length():
            msj = 'Error "borrar" fuera del rango de index'
            return msj
        cursorIndex = 0
        cursorNodo = self.head
        while True:
            nodoAnterior = cursorNodo       # A diferencia que al eliminar el dato
            cursorNodo = cursorNodo.next    # Se le pregunta si habia un noto anterior
            if cursorIndex == index:        # Al nodo anterior.next le asignamos el nodo_actual.next
                nodoAnterior.next = cursorNodo.next
                return
            cursorIndex+=1
