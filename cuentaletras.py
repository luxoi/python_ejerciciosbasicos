#Escribe una funcion que reciba como párametro un string.
#La funcion debe retornar un diccionario con el numero de veces
#que se encuentren en cada letra
    #Ej: "Hola como estas" -> {'H: 1, 'o': 2 } etc...

def cuentaLetras(text):
    diccionario = {}
    for letra in text:
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1
    return diccionario

print(cuentaLetras("Hola como estas"))  