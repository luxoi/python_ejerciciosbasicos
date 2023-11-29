#Escribe una funcion que recibe como párametro un arreglo de Strings y un string.
#La función debe regresar cuantas veces se encuentra la palabra en el arreglo
#Ej: ["Hola", "Como", "Estas", "como", "te", "Encuentras"]
# como -> 2

def encuentraPalabra(arreglo, palabra):
    cont = 0
    for pal in arreglo:
        if pal == palabra:
            cont += 1
    return cont

arreglo = ["Hola", "como", "estas?", "me", "gusta", "programar", "Tambien", "me", "gusta", "programar"]
print(encuentraPalabra(arreglo, "programar"))