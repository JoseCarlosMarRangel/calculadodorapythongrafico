
resultado = 0

def convertir(lista):
    lista2 = lista.split(",")
    b= [int(x) for x in lista2]
    print("b es: ", b)
    #operacion(b)
    resultado = operacion(b)
    return resultado
    #igual(resultado)
    
    print("el resultado es: ",resultado)

def operacion(lista):
    """"""
    #print(type(lista))
    return lista[0] + operacion(lista[1:]) if lista else 0