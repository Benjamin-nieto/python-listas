from Listas.listas_2022 import ListaSimple
class Metodos:
    #Mayor de una lista de enteros
    def mayorValorEntero(lista_datos:ListaSimple) -> int:
        if not isinstance(lista_datos, ListaSimple):
            return None
        if lista_datos.estaVacia():
            return None
        mayor = lista_datos.buscarPosicion(0)
        if not isinstance(mayor, int):
            return None
        longitud_lista = lista_datos.longitud()
        for i in range(longitud_lista):
            dato = lista_datos.buscarPosicion(i)
            if not isinstance(dato, int):
                return None
            if dato > mayor:
                mayor = dato
        return mayor
    
    # multiplicar numeros
    def multiplicacionNumeros(lista_datos:ListaSimple) -> int:
        if not isinstance(lista_datos, ListaSimple):
            return None
        if lista_datos.estaVacia():
            return None
        totalMultiplicacion = 1
        longitud_lista = lista_datos.longitud()
        for i in range(longitud_lista):
            totalMultiplicacion = totalMultiplicacion * lista_datos.buscarPosicion(i)
        return totalMultiplicacion

    # numeros par
    def NumerosPares(lista_datos:ListaSimple) -> int:
        if not isinstance(lista_datos, ListaSimple):
            return None
        if lista_datos.estaVacia():
            return None
        numPares = []
        longitud_lista = lista_datos.longitud()
        for i in range(longitud_lista):
            if (lista_datos.buscarPosicion(i) % 2 )== 0 :
                numPares.append(lista_datos.buscarPosicion(i))
        return numPares

    # numeros impar
    def NumerosImpares(lista_datos:ListaSimple) -> int:
        if not isinstance(lista_datos, ListaSimple):
            return None
        if lista_datos.estaVacia():
            return None
        numImpares = []
        longitud_lista = lista_datos.longitud()
        for i in range(longitud_lista):
            if (lista_datos.buscarPosicion(i) % 2 ) != 0 :
                numImpares.append(lista_datos.buscarPosicion(i))
        return numImpares

    # comparar dos listas y buscar cuales si y cuales no son similares
    def buscarSimilareDeDosListas(lista_datos:ListaSimple, lista_datos2:ListaSimple) -> int:
        arraySimilares = []
        if not isinstance(lista_datos, ListaSimple):
            return None
        if lista_datos.estaVacia() and lista_datos2.estaVacia():
            return None
        if lista_datos.longitud() != lista_datos2.longitud():
            return None
        if lista_datos.longitud() == lista_datos2.longitud():
            longitud_lista = lista_datos.longitud()
            for i in range(longitud_lista):
                if (lista_datos.buscarPosicion(i) == lista_datos2.buscarPosicion(i)) :
                    arraySimilares.append(True)
                else:
                   arraySimilares.append(False) 
        return arraySimilares
    
    #es similar o no es similar(dos listas)
    def esSimilar(lista_datos:ListaSimple, lista_datos2:ListaSimple) -> int:
        similar = []
        longitud = lista_datos.longitud()
        contador = 0
        similar = Metodos.buscarSimilareDeDosListas(lista_datos, lista_datos2)
        if lista_datos.longitud() == longitud:
            for i in range (longitud):
                if similar[i] == True :
                    contador = contador + 1
            if contador == longitud :
               return True
            else:
                return False

    #    
        
           
        



    