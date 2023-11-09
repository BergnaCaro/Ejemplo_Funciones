
# Escribir una función que reciba dos números enteros positivos y
# retorne su suma invertida. Ayuda un int se puede pasar a str y viceversa 
# Ejemplo, si recibe (123,456) (123+456=579), Retornaría 975.
# OJO retorna un ENTERO

def invertir_numero(numero1,numero2):
    suma=numero1 +numero2
    cambio=str(suma)
    voltear=""
    for elemento in cambio [::-1]:
        voltear+=elemento
    cambio=int(voltear)
    return cambio



# Escribir una función que reciba un número entero y devuelva FALSE si el 
# número es igual a la suma de sus divisores sin contarse a el mismo.
# Y TRUE en caso contrario 
# Ejemplo, 6 Retornaría FALSE porque 1 + 2 + 3 = 6.
# Ejemplo, 8 Retornaría TRUE porque 1 + 2 + 4 != 8.

def es_numero_perfecto(numero):
    respuesta = True
    sumatoria= 0
    for i in range(1,numero):
        if numero % i == 0:
            sumatoria = sumatoria+ i
            if sumatoria == numero:
                respuesta = False
            else:
                respuesta = True
    return respuesta


# Escribir una función que reciba una lista de números enteros y además 
# un número entero n, y devuelva una lista con los números que 
# son mayores a n en el mismo orden que aparecen.
# Ejemplo ([3,6,2,4,7,1,8],6) retornaría [7,8]
# Ejemplo ([3,6,2,4,7,1,8],3) retornaría [6,4,7,8]

def numeros_mayores(lista, n):
    numeros=[]
    for elemento in lista:
        if elemento>n:
            numeros.append(elemento)
    return numeros


# Escribir una función que reciba dos listas de números enteros y devuelva una 
# lista con los números de la primera que no están en la segunda, en el mismo orden .
# Ejemplo [3,6,2,4,7,1,8],[11,6,12,14,7,1] retornaría [3,2,4,8]
# Ejemplo [15,2,6,8,34,12],[12,17,26,2,34,9] retornaría [15,6,8]
# Ejemplo [7,23,11,31,83,89],[1,3,7,11,83,23] retornaría [31,89]

def no_estan(lista1, lista2):
    nuevaLista =[]
    cipi=lista1
    for elemento in lista1:
        for elementos in lista2:
            if elemento is elementos:
                nuevaLista.append(elemento)
    for x in nuevaLista:
        for elemento in lista1:
            if x == elemento:
                cipi.remove(x)
    return cipi

