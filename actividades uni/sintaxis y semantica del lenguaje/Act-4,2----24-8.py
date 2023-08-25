l1="{ca,ma}" 
l2 = "{nta,sa}"
texto="{canta,casta,manta,masa}"
principio_texto=1
principio_l1=1
principio_l2=1
for i in range(len(texto)):
    bandera1=False
    bandera2=False
    if  texto[i] == "}" or texto[i] == ",":
        palabra = texto[principio_texto:i]

        for j in range(len(l1)):
            if l1[j] == "}" or l1[j] == ",":
                for k in range(len(l1[principio_l1:j]),len(palabra)+1):
                    if l1[principio_l1:j] == palabra[k-len(l1[principio_l1:j]):k]:
                        bandera1=True
                principio_l1 = j+1

        for x in range(len(l2)):
            if l2[x] == "}" or l2[x] == ",":
                for y in range(len(l2[principio_l2:x]),len(palabra)+1):
                    if l2[principio_l2:x] == palabra[y-len(l2[principio_l2:x]):y]:
                        bandera2=True
                principio_l2 = x+1

        principio_l2=1
        principio_l1=1
        principio_texto = i+1
        if bandera2==True and bandera1==True:
            print("La palabra", palabra, " corresponde al lenguaje l1 y l2")
        else:
            print("La palabra", palabra, " no corresponde al lenguaje l1 y l2")