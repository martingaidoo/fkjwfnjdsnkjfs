##Definir una función que reciba 3 enteros. Si los 3 enteros son
##iguales, retornar 20. Si solo 2 enteros son iguales, retornar 10. Si los 3 son desiguales, retornar 0.

import random
def funcion1(entero1,entero2,entero3):
    igualdad = 0
    valor =0
    if entero1==entero2:
        igualdad = igualdad + 1
    if entero1==entero3:
        igualdad = igualdad + 1
    if entero2==entero3:
        igualdad = igualdad + 1
    if igualdad == 1:
        valor=10
    elif igualdad == 3:
        valor = 30
    return(valor)

#Definir una función/procedimiento que reciba una lista de números. Debe retornar el segundo valor más alto y su posición en la lista.
def funcion2():
    largo = int(input("dime el largo de la lista"))
    lista = []
    mayor = 0
    segundomayor=0
    posicion_segundo=0
    for i in range(largo):
        lista.append(int(input()))
        if mayor < lista[i]:
            mayor = lista[i]
    for i in range(largo):
        if lista[i] != mayor:
            if lista[i] > segundomayor:
                segundomayor = lista[i]
                posicion_segundo = i
    print(segundomayor)
    print(posicion_segundo)
    
##Definir una función/procedimiento que dado un texto, encuentre cuantas veces se repite otra cadena ingresada por el usuario.
def funcion3():
    texto = input("")
    cadena = input("")
    largo = len(cadena)
    contador = 0
    repite = 0
    while contador <= len(texto)-largo:
        if texto[contador:contador+largo] == cadena:
            repite = repite +1
        contador = contador+1
    return(repite)

adivino = ""
palabra = input("")
intentos = int(input(""))
palabraoculta= palabra
contador=0
letrasborradas=[]
while (contador*100)/len(palabra) < 40-(100/len(palabra)):
    random_integer = random.randint(0, len(palabra)-1)
    if palabraoculta[random_integer] != "_":
        palabraoculta = palabraoculta[0:random_integer] + "_" + palabraoculta[random_integer+1:len(palabra)]
        contador = contador+1
        letrasborradas.append(palabra[random_integer])
print(letrasborradas)

salir = False

while intentos > 0 and salir == False:
    bandera = False
    letra= input("dime tu letra o palabra")
    for i in letrasborradas:
        if letra == i:
            bandera = True
    if bandera == True:
        for i in range(len(palabra)):
            if letra == palabra[i]:
                if palabraoculta[i] == "_":
                    palabraoculta= palabraoculta[0:i]+ letra + palabraoculta[i+1:len(palabra)]
                    contador = contador-1

    if contador == 0 or letra == palabra:
        salir = True
        print("entro")
    intentos= intentos-1
    print("tus intentos son:" , intentos)
    if bandera == True:
        print("es correcto, la letra"+ letra + palabraoculta)
    else:
        print("es incorrecto, la letra"+ letra + palabraoculta)
