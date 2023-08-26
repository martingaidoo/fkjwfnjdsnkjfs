# 1- UNION DE CONJUNTOS
# Dados dos conjuntos A={1,2,3,4,5,6,7,} y B={8,9,10,11} la unión de estos conjuntos
# será A∪B={1,2,3,4,5,6,7,8,9,10,11}
# 2- INTERSECCIÓN DE CONJUNTOS
# Dados dos conjuntos A={1,2,3,4,5} y B={4,5,6,7,8,9} la intersección de estos
# conjuntos será A∩B={4,5}
# 3- DIFERENCIA DE CONJUNTOS
# Dados dos conjuntos A={1,2,3,4,5} y B={4,5,6,7,8,9} la diferencia de estos conjuntos
# será A-B={1,2,3}
# 4- COMPLEMENTO DE UN CONJUNTO
# Dado el conjunto Universal U={1,2,3,4,5,6,7,8,9} y el conjunto A={1,2,9}, el conjunto
# A' estará formado por los siguientes elementos A'={3,4,5,6,7,8}
# 5- DETERMINAR EL TAMAÑO DE UN CONJUNTO
# Por ejemplo A = {{a}, {b, c}} (longitud = 2)

def union(conjunto1, conjunto2): 
    conjunto1 = "," + conjunto1[1:-1] + ","
    conjunto2 = "," + conjunto2[1:-1] + ","
    elementos_no_repetidos = str("")
    i=0
    while i<(len(conjunto2)): 
        tamaño_elemento = 1
        if conjunto2[i]!="," and conjunto1.find("," + conjunto2[i:i + conjunto2[i:].find(",")] + ",") == -1: 
            tamaño_elemento = (conjunto2[i:].find(","))
            elementos_no_repetidos = elementos_no_repetidos +  "," + conjunto2[i:i + conjunto2[i:].find(",")]
        i += tamaño_elemento
    conjunto1 = "{"+ conjunto1[1:-1] + elementos_no_repetidos +  "}"
    return conjunto1

def diferencia(conjunto1, conjunto2): 
    conjunto2 = "," + conjunto2[1:-1] + ","
    conjunto1 = "," + conjunto1[1:-1] + ","
    elementos_no_repetidos = str("")
    i=0
    while i<(len(conjunto1)): 
        tamaño_elemento = 1
        if conjunto1[i]!="," and conjunto2.find("," + conjunto1[i:i + conjunto1[i:].find(",")] + ",") == -1: 
            tamaño_elemento = (conjunto1[i:].find(","))
            elementos_no_repetidos = elementos_no_repetidos +  "," + conjunto1[i:i + conjunto1[i:].find(",")]
        i += tamaño_elemento
    conjunto1 = "{"+ elementos_no_repetidos.strip(",") +  "}"
    return conjunto1

def interseccion(conjunto1, conjunto2): 
    conjunto2 = "," + conjunto2[1:-1] + ","
    conjunto1 = "," + conjunto1[1:-1] + ","
    elementos_repetidos = str("")
    i=0
    while i<(len(conjunto1)): 
        tamaño_elemento = 1
        if conjunto1[i]!="," and conjunto2.find("," + conjunto1[i:i + conjunto1[i:].find(",")] + ",") != -1: 
            if conjunto1[i]=="{":
                tamaño_elemento = (conjunto1[i:].find("}")+1)
            else:
                tamaño_elemento = (conjunto1[i:].find(","))
            elementos_repetidos = elementos_repetidos +  "," + conjunto1[i:i + conjunto1[i:].find(",")]
        i += tamaño_elemento
    conjunto1 = "{"+ elementos_repetidos.strip(",") +  "}"
    return conjunto1

def complementar(universo,conjunto):
    complemento=''
    for numero in universo:
        if numero != ',' and (numero not in conjunto):
            complemento += ","+ numero
    complemento = complemento[1:len(complemento)]
    return "{"+complemento+"}"


def tamaño(conjunto):
    contador = 0
    bandera = False
    for i in conjunto:
        if i == "{" or i == "}":
            bandera = not bandera
        if i == "," and bandera == True:
            contador = contador+1
    return(contador+1)