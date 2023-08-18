abecedario= ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " "]
lenguaje = ["4","I3", "[", ")", "3", "|=" , "&", "#", "1", ",_|", ">|", "1", "JVI", "^/", "0", "|*", "(_,)", "I2", "5", "7", "(_)", "\/", "\/\/", "><", "j", "2", "L", "R", "E", "A", "S", "b", "T", "B", "g", "o", " "]   
bandera = True
while bandera:
    transformacion = ""
    palabra = str(input("dime la palabra"))
    palabra = palabra.lower()
    for i in palabra:
        for j in range(len(abecedario)):
            if abecedario[j] == i:
                transformacion = transformacion + lenguaje[j]

    print (transformacion)