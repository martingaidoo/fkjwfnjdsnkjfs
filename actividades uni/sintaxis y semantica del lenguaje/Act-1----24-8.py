##1- Ingresar dos palabras y determinar si una es la inversa de la otra.
palabra1 =input("dime la primera palabra: ")
palabra2=input("dime la segunda palabra: ")
bandera = 0
bandera2 = 0
contador=0
inversor = len(palabra2)-1
while bandera == 0:
    if palabra1[contador] != palabra2[inversor]:  
        bandera = 1
    if inversor != 0:
        contador = contador + 1
        inversor= inversor-1
    else:
        if bandera != 1:
            bandera = 2
if bandera == 1:
    print("No son inversas")
else:
    print("Son inversas")