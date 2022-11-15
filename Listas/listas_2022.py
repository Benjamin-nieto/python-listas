#Clase Nodo Simple
from ast import For
from ctypes import pointer
#import numpy as np

class NodoSimple:
    #Constructor
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    #Str
    def __str__(self) -> str:
        return str(self.dato)
    #Eq
    def __eq__(self, other):
        if not isinstance(other, NodoSimple):
            return False
        return self.dato == other.dato
#Clase ListaSimple
class ListaSimple:
    #Constructor
    def __init__(self) -> None:
        self.nodoInicial = None
    
    #Lista Vacia
    def estaVacia(self):
        return self.nodoInicial == None

    #Adicionar al inicio
    def adicionarAlInicio(self, dato_nuevo):
        nodoNuevo = NodoSimple(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoNuevo.siguiente = self.nodoInicial
            self.nodoInicial = nodoNuevo
    #Adicionar al Final (hecho por daniela)
    def adicionarAlFinal(self, dato_nuevo):
        nodoNuevo = NodoSimple(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoActual = self.nodoInicial
            while nodoActual.siguiente != None:
                nodoActual = nodoActual.siguiente
            nodoActual.siguiente = nodoNuevo
    
    #Adicionar por posicion (hecho por daniela)
    def adicionarPorPosicion(self, dato_nuevo, posicion):
        nodoNuevo = NodoSimple(dato_nuevo)
        contador = 0
        if posicion > self.longitud() + 1 :
            raise Exception("posicion mayor a la longitud: ", posicion)
        if self.estaVacia() and posicion == 0 :
            #caso Lista Vacia
            self.nodoInicial = nodoNuevo
        else:
            nodoActual = self.nodoInicial
            nodoPrevio = self.nodoInicial
            while contador < posicion :
                nodoPrevio = nodoActual
                nodoActual = nodoActual.siguiente
                contador = contador + 1
            if posicion == 0 :
                self.adicionarAlInicio(dato_nuevo)
            else:
                nodoPrevio.siguiente = nodoNuevo
                nodoNuevo.siguiente = nodoActual
        
    #Eliminar al inicio
    def eliminarAlInicio(self):
        if self.estaVacia():
            return None
        else:
            dato = self.nodoInicial.dato
            self.nodoInicial = self.nodoInicial.siguiente
            return dato
    
    #Eliminar al final (hecho por daniela)
    def eliminarAlFinal(self):
        if self.estaVacia():
            return None
        else:
            nodoActual = self.nodoInicial
            nodoPrevio = self.nodoInicial
            dato = self.nodoInicial.dato
            while nodoActual.siguiente != None :
                nodoPrevio = nodoActual
                nodoActual = nodoActual.siguiente
            nodoPrevio.siguiente = None
            return dato

    #Buscar por dato
    def buscar(self, dato_buscar):
        if self.estaVacia():
            return False
        else:
            nodoActual = self.nodoInicial
            while nodoActual != None:
                if nodoActual.dato == dato_buscar:
                    return True
                nodoActual = nodoActual.siguiente
            return False
    #Str
    def __str__(self):
        recorrido = ""
        nodoActual = self.nodoInicial
        while nodoActual != None:
            recorrido += str(nodoActual.dato) + " "
            nodoActual = nodoActual.siguiente
        return recorrido

    #Longitud (hecho por daniela)
    def longitud(self):
        nodoActual = self.nodoInicial
        contador = 0
        while nodoActual != None:
            nodoActual = nodoActual.siguiente
            contador = contador + 1
        return contador

    #Buscar por posición (hecho por daniela)
    def buscarPosicion(self, posicion):
        if self.estaVacia():
            return None
        if posicion < 0:
            raise Exception("La posición debe ser mayor o igual a cero!")
        nodoActual = self.nodoInicial
        contador_posicion = 0
        while (nodoActual != None and contador_posicion < posicion):
            contador_posicion += 1
            nodoActual = nodoActual.siguiente
        if nodoActual == None:
            return None
        return nodoActual.dato
    
    #Buscar Ultimo Elemento(Daniela)
    def buscarUltimoElemento(self):
        if self.estaVacia():
            return None
        else:
            NodoActual = self.nodoInicial
            while NodoActual.siguiente != None :
                NodoActual = NodoActual.siguiente
            return NodoActual.dato
    
    #buscar penultimo elemento (hecho por daniela)
    def buscarPenultimoElemento(self):
        if self.estaVacia():
            return None
        else:
            nodoActual = self.nodoInicial
            nodoPrevio = self.nodoInicial
            while nodoActual.siguiente != None:
                nodoPrevio = nodoActual
                nodoActual = nodoActual.siguiente
            return nodoPrevio.dato

    #Eliminar penultimo elemento (made by daniela)
    def EliminarPenultimo(self):
        if self.estaVacia():
            raise Exception("Lista vacia no hay elementos para eliminar!")
        else:
           self.eliminarPorPosicion(self.longitud()-2)
        

    #Eliminar por información
    def eliminarInfo(self, dato_eliminar):
        if self.estaVacia():
            return False
        if self.nodoInicial.dato == dato_eliminar:
            self.eliminarAlInicio()
            return True
        nodoPrevio = None
        nodoActual = self.nodoInicial
        while nodoActual != None and nodoActual.dato != dato_eliminar:
            nodoPrevio = nodoActual
            nodoActual = nodoActual.siguiente
        if nodoActual == None:
            return False
        if nodoActual.siguiente == None:
            nodoPrevio.siguiente = None
        else:
            nodoPrevio.siguiente = nodoActual.siguiente
        return True
    
    #eliminar apariciones de un dato (los borra todos no deja ni uno)
    def eliminarAparicionesDeUnDato(self, datoAeliminar):
        if self.estaVacia() :
            return False
        else:
            nodoPrevio = self.nodoInicial
            nodoActual = self.nodoInicial
            while nodoActual != None :
                if self.nodoInicial.dato.__eq__(datoAeliminar):
                    self.eliminarAlInicio()
                if nodoActual.dato.__eq__(datoAeliminar):
                    nodoPrevio.siguiente = nodoActual.siguiente
                if nodoActual == None :
                    return False 
                nodoPrevio = nodoActual
                nodoActual = nodoActual.siguiente
        return True
    
    #eliminar por posicion
    def eliminarPorPosicion(self, posicion):
        contador = 0
        nodoActual = self.nodoInicial
        nodoPrevio = self.nodoInicial
        dato = self.nodoInicial.dato

        if self.estaVacia() or posicion < 0 :
            raise Exception("indice:", posicion)
        if posicion == 0 :
            self.eliminarAlInicio()
        else :
            while ( nodoActual != None and contador < posicion ):
                contador = contador + 1
                nodoPrevio = nodoActual
                nodoActual = nodoActual.siguiente
            nodoPrevio.siguiente = nodoActual.siguiente
        return dato

    #  buscar y contar el numero de veces que aparece un dato
    def buscarYContarUnDato(self, datoABuscar):
        contador = 0
        nodoActual = self.nodoInicial
        while (nodoActual != None):
            if nodoActual.dato == datoABuscar :
                contador = contador + 1
            nodoActual = nodoActual.siguiente
        return contador

    #mover elemento dado en( posicion inicial) a una posicion final dada por el usuario
    def moverElemento(self, posInicial, posFinal):
        ##posiciones menores a 0
        if (posInicial < 0 or posFinal < 0):
            raise Exception("La posición debe ser mayor o igual a cero!")
        if (posInicial == posFinal):
            raise Exception("La posición iguales!")
        if self.estaVacia() :
            raise Exception("lista vacia no se puede mover elementos!")
        else :
            contador = 0
            nodoActual = self.nodoInicial
            nodoPrevio = self.nodoInicial
            temporal = None
            if (posInicial == 0):
                temporal = nodoActual
            else :
                while (contador < posInicial):
                    contador = contador + 1
                    nodoPrevio = nodoActual
                    if (contador == posInicial):
                        temporal = nodoActual.siguiente
                    nodoActual =nodoActual.siguiente
            if (posInicial == 0):
                self.eliminarAlInicio()
            else :
                nodoPrevio.siguiente = nodoActual.siguiente
            contador = 0
            nodoActual = self.nodoInicial
            nodoPrevio = self.nodoInicial
            while (contador < posFinal):
                contador = contador + 1
                nodoPrevio = nodoActual
                nodoActual = nodoActual.siguiente
            if (posFinal == 0):
                temporal.siguiente = self.nodoInicial
                self.nodoInicial = temporal
            else :
                nodoPrevio.siguiente = temporal
                temporal.siguiente = nodoActual

    #buscar posiciones de un dato
    def buscarPosicionesDato(self, datoAbuscar):
        arrayPosiciones = []
        nodoActual = self.nodoInicial
        contador = 0
        while nodoActual != None :
            if (nodoActual.dato == datoAbuscar):
                arrayPosiciones.append(contador)
            nodoActual = nodoActual.siguiente
            contador = contador + 1
        return arrayPosiciones
    
    # buscar y mostrar elementos entre posiciones
    def buscarElementosEntrePosiciones(self, posInicial, posFinal):
        arrayElementos = []
        nodoActual = self.nodoInicial
        contador = 0
        while nodoActual != None :
            if (contador >= posInicial and contador <= posFinal):
                arrayElementos.append(nodoActual.dato)
            nodoActual = nodoActual.siguiente
            contador = contador + 1
        return arrayElementos
    
    #Indicar las posiciones en las que aparece en forma consecutiva
    #un dato indicado por el usuario en la lista enlazada.(probar varios casos)
    # sin terminar no funciona.
    
    def buscarPosicionDatoConsecutivos(self, datoAbuscar):
        elementosConsecutivos = []
        nodoActual = self.nodoInicial
        contador = 0
        if self.estaVacia() :
            return None
        else :
            while nodoActual != None :
                if (nodoActual.dato == datoAbuscar and (nodoActual.siguiente != None and nodoActual.siguiente.dato == datoAbuscar)):
                    
                    elementosConsecutivos.append(contador)
                    elementosConsecutivos.append(contador+1)
                contador = contador + 1
                nodoActual = nodoActual.siguiente      
        return sorted(list(set(elementosConsecutivos)))
    
    #obtener  lista invetida
    def obtenerListaInvertida(self):
        elementos = []
        contador = self.longitud()-1
        if self.estaVacia() :
            return None
        else :
            while contador >= 0 :
               elementos.append(self.buscarPosicion(contador))
               contador = contador - 1
        return elementos

 #ordenamiento ascendente de nodos de una lista simple, solo funciona con un tipo de dato
 #capturar excepcion si la lista tiene diferentes tipos de datos
    def ordenAscendenteLista(self):
        contador = self.longitud()
        while contador > 0:
            nodoPrevio = self.nodoInicial
            nodoActual = self.nodoInicial
            contador = 0
            for i in range(self.longitud()-1):
                nodoPrevio = nodoActual
                nodoActual = nodoActual.siguiente
                if nodoPrevio.dato > nodoActual.dato :
                    #intercambio de datos
                    self.moverElemento(i, i+1)
                    contador = contador + 1
 
 #Metodo que determina que tipo de dato hay en cada posicion de la lista
    def TiposDeDatosLista(self):
        TipoDatos = []
        if self.estaVacia():
            return None
        else:
            nodoActual = self.nodoInicial
            while nodoActual != None:
                TipoDatos.append(type(nodoActual.dato))
                nodoActual = nodoActual.siguiente
            return TipoDatos

 #eliminar la o las repeticiones de un dato (dejando solo uno)
 # #ejemplo si ya [1,2,2,2,4] al eliminar deberia quedar asi [1,2,4], utilizar method buscarPosicionesDato.


 #Intercambio dos elementos de una lista enlazada (segun sus valores)
    def intercambioDosElementos(self, primerElemento, segundoElemento):
        contador = self.longitud()
      
             





            
                

