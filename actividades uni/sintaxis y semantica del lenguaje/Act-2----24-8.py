#Ingresar una palabra y determinar el número de ocurrencias de un símbolo dado.
palabra= input("Dime la palabra")
simbolo = input("Dime el simbolo")
contador=0
for i in range(len(simbolo), len(palabra)+1,1):
    if palabra[i-len(simbolo):i] == simbolo:
        contador = contador+1
print("El numero de ocurrencias es de", contador)