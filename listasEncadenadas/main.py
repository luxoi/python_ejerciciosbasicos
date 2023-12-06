from Nodo import Nodo
from ListaEncadenada import ListaEncadenada

listaPersonas = ListaEncadenada()

persona1 = Nodo("Alex", "Mtz", 1)
persona2 = Nodo("Ben", "Frank", 2)
persona3 = Nodo("Carlos", "Hdz", 3)
persona4 = Nodo("Diana", "Montoya", 4)

listaPersonas.insertaNodo(persona1)
listaPersonas.insertaNodo(persona2)
listaPersonas.insertaNodo(persona3)
listaPersonas.insertaNodo(persona4)

nodo = listaPersonas.buscaNodo(3)
nodo.imprimeDatos()