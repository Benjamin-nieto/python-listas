from listas_2022 import *

#Creacion instancia
lista_01 = ListaSimple()
lista_02 = ListaSimple()
print("Lista:",lista_01)
print("Esta Vacia:",lista_01.estaVacia())

#Adicion elementos
lista_01.adicionarAlInicio(1)
lista_01.adicionarAlInicio(2)
lista_01.adicionarAlInicio(3)
print("Lista:",lista_01)
print("Esta Vacia:",lista_01.estaVacia())
print("longitud: ",lista_01.longitud())

#Adicion al final de elementos
#Adicion elementos
lista_02.adicionarAlFinal('a')
lista_02.adicionarAlFinal('b')
lista_02.adicionarAlFinal('c')
lista_02.adicionarAlFinal('d')
lista_02.adicionarAlFinal('e')
lista_02.adicionarAlFinal('f')
lista_02.adicionarAlFinal('g')
print("Lista:",lista_02)
print("eleento", lista_02.buscarPenultimoElemento())
print("Esta Vacia:",lista_02.estaVacia())
#Eliminar al Final
lista_02.eliminarAlFinal()
print("Lista:",lista_02)
print(lista_02.buscarUltimoElemento())
#Adicion al final de elementos
#Adicion elementos
lista_02.adicionarPorPosicion(2, 2)
print("Lista:",lista_02)

#Buscar elementos
print("Buscar 01:",lista_01.buscar(5))
print("Buscar 02:",lista_01.buscar(1))

#Eliminar elementos
print("Eliminar 01:",lista_01.eliminarAlInicio())
print("Lista:",lista_01)
