
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

