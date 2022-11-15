from listas_2022 import *

#Diseño Lista Doble
#Clase Nodo Doble
class NodoDoble(NodoSimple):
    #Constructor
    def __init__(self, dato):
        super().__init__(dato)
        self.previo = None
    #Eq
    def __eq__(self, other):
        if not isinstance(other, NodoDoble):
            return False
        return self.dato == other.dato
# Clase ListaDoble
class ListaDoble(ListaSimple):
    # Constructor
    def __init__(self) -> None:
        super().__init__()        

    # Adicionar al inicio
    def adicionarAlInicio(self, dato_nuevo):
        nodoNuevo = NodoDoble(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoNuevo.siguiente = self.nodoInicial
            self.nodoInicial.previo = nodoNuevo
            self.nodoInicial = nodoNuevo

    #Adicionar al final
    def adicionarAlFinal(self, dato_nuevo):
        nodoNuevo = NodoDoble(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoActual = self.nodoInicial
            while (nodoActual.siguiente != None):
                nodoActual = nodoActual.siguiente
            nodoActual.siguiente = nodoNuevo
            nodoNuevo.previo = nodoActual
    
    

    #Eliminar al inicio
    def eliminarAlInicio(self):
        if self.estaVacia():
            return None
        else:
            dato = self.nodoInicial.dato
            self.nodoInicial = self.nodoInicial.siguiente
            if self.nodoInicial != None:
                self.nodoInicial.previo = None
            return dato

    # Eliminar por información
    def eliminarInfo(self, dato_eliminar):
        if self.estaVacia():
            return False
        if self.nodoInicial.dato == dato_eliminar:
            self.eliminarAlInicio()
            return True
        nodoActual = self.nodoInicial
        while nodoActual != None and nodoActual.dato != dato_eliminar:
            nodoActual = nodoActual.siguiente
        if nodoActual == None:
            return False
        nodoPrevio = nodoActual.previo
        if nodoActual.siguiente == None:
            nodoPrevio.siguiente = None
        else:
            nodoPrevio.siguiente = nodoActual.siguiente
            nodoSiguiente = nodoActual.siguiente
            nodoSiguiente.previo = nodoPrevio
        return True