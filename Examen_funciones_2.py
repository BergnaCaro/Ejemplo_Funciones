
# Escribir una función que reciba dos números enteros y devuelva la
# la multiplicación de todos los números entre el número menor y el mayor.
# Ejemplo, para 7 y 10 retornaría 5040.
# Ejemplo, para 8 y 3 retornaría 20160.

def multiplicacion(numero1, numero2):
    resultado=1
    
    if numero1 < numero2:
        for elemento in range(numero1,numero2+1):
            resultado = resultado * elemento
        
    else:
        for elemento in range(numero2,numero1+1):
            resultado = resultado * elemento
        
    return resultado


# Escribir una función que reciba un número entero y devuelva True si el 
# número es igual a la suma de sus divisores sin contarse a el mismo. 
# Por ejemplo, 6 Retornaría True porque 1 + 2 + 3 = 6.
# Por ejemplo, 8 Retornaría False porque 1 + 2 + 4 != 8.

def es_numero_perfecto(numero):
    respuesta = True
    sumatoria= 0
    for i in range(1,numero):
        if numero % i == 0:
            sumatoria = sumatoria+ i
            if sumatoria == numero:
                respuesta = True
            else:
                respuesta = False
    return respuesta



# Escribir una función que reciba una lista de números enteros y devuelva True
# si la lista está ordenada de menor a mayor, y False en caso contrario. 
# Ejemplo [3,6,2,4,7,1,8] retornaría False
# Ejemplo [3,6,8,8,12,18] retornaría True

def esta_ordenada(lista):
    lista2=lista [ : ]
    lista2.sort()
    if lista == lista2:
        ordenada= True
    else:
        ordenada = False
    return ordenada

    




# Escribir una función que reciba una lista de números enteros positivos
# entre los que hay un -1 (menos uno) y retorne el promedio de los valores
# de la lista hasta el valor -1 (redondeado a 2 decimales).
# EJEMPLO: lista = [8, 12, 9, -1, 7, 20] retornaría 9.67 
# EJEMPLO: lista = [4, 6, 2, 1, -1, 13, 12, 20] retornaría 3.25
# EJEMPLO: lista = [5, 3, 7, 9, 10, 4, -1, 6] retornaría 6.33


def promedio(lista):
    contador= 0
    sumatoria = 0
    posicion= lista.index(-1)
    for elemento in lista[0:posicion]:
        sumatoria= sumatoria +elemento
        contador= contador +1
    resultado =sumatoria/contador
    return round(resultado,2)


