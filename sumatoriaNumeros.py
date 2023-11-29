#Dado un numero,regresar la sumatoria de todos sus digitos
#ej: si recibo 1234 regresarme 10
def sumatoria(num):
    total = 0
    while num != 0:
        ultimoDigito = num % 10 #1234 % 10 -> 4
        total += ultimoDigito
        num = num // 10 #Division de entero -> Me va a dividir, me va a regresar la division redondeada hacia abajo
    print(total)


sumatoria(int(input("escribe un numero: ")))

