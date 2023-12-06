from Nodo import Nodo
class ListaEncadenada:
    def __init__(self):
        self.head = None
        
    def insertaNodo(self, nuevoNodo):
        if self.head == None:
            self.head = nuevoNodo
        else : 
            aux = self.head
            while aux.next != None:
                aux = aux.next
            aux.next = nuevoNodo

    def imprimeLista(self):
        aux = self.head
        while aux != None:
            print(aux.valor)
            aux = aux.next

    def buscaNodo(self, id):
        aux = self.head
        while aux != None:
            if aux.getId() == id:
                return aux
            aux = aux.next
        return None

    def eliminaNodo(self, id):
        if self.head == None:
            return "La lista esta vacia, no puedes eliminar nodos"    
        else:
            aux = self.head
            if aux.getId() == id:
                #1.- El nuevo head es el next (el que le sigue) de mi nodo actual
                self.head = aux.next
                #2.- Del nodo que estoy eliminando, el NEXT debe ser None
                aux.next = None
                return "eliminado"
            else:
                prevAux = aux
                while aux.next != None:
                    prevAux = aux
                    aux = aux.next
                    #1.- Buscar el nodo que queremos eliminar en base a su id
                    if aux.getId() == id:
                        #2.- Un nodo antes, su next sea el next de el nodo a eliminar
                        prevAux.next = aux.next
                        #3.- el nodo que estoy eliminado, el Next debe ser none
                        aux.next = None
                        return "Nodo eliminado"

    def insertaNodoEnPosicion(self, nuevoNodo, posicion):
        if indice <= self.longitude():
            if posicion == 0:
                nuevoNodo.next = self.head
                self.head = nuevoNodo
            else:
                aux = self.head
                prev = aux
                x = 0
                while x < posicion:
                    prev = aux
                    aux = aux.next
                    x += 1	
                prev.next = nuevoNodo
                nuevoNodo.next = aux    

        else:
            return "Posicion no valida"

    def longitud(self):
        aux = self.head
        cont = 0
        while aux != None:
            cont+=1
            aux = aux.next
        return cont