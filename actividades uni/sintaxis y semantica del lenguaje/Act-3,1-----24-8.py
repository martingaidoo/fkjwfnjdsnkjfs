texto = input("Dime el texto: (con el formato { , , , ,})")
alfabeto = input("Dime el alfabeto: (con el formato { , , , ,})")
externa=""
contador = 0
longitud_conjunto=0
principio = 1
for i in range(len(texto)):
    bandera = False
    if texto[i] == ",":
        if longitud_conjunto == contador:
            print("OK, El conjunto:", texto[principio:i])
        else:
            print("NO OK El conjunto:", texto[principio:i], " Lo externo es:", externa)
        principio = i+1
        externa= ""
        contador = 0
        longitud_conjunto = 0
    if texto[i] != "{" and texto[i] != "}" and texto[i] != ",":
        longitud_conjunto = longitud_conjunto + 1
        for j in range(len(alfabeto)):
            if alfabeto[j] != "{" and alfabeto[j] != "}" and alfabeto[j] != ",":
                if alfabeto[j] == texto[i]:
                    bandera = True
        if bandera == False:
            externa = externa + texto[i]
        else:
            contador = contador+1
if longitud_conjunto == contador:
    print("OK, El conjunto:", texto[principio:i])
else:
    print("NO OK El conjunto:", texto[principio:i], " Lo externo es:", externa)