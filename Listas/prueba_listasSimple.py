from listas_2022 import *
"""
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
"""
#prueba 2
"""
lista_02 = ListaSimple()
lista_02.adicionarAlInicio(10)
lista_02.adicionarAlInicio(20)
lista_02.adicionarAlInicio(30)
lista_02.adicionarAlInicio(40)
lista_02.adicionarAlInicio(50)
lista_02.adicionarAlInicio(60)
print("Lista 02:", lista_02)
#Buscar por posición
try:
    print("Posicion 01:",lista_02.buscarPosicion(-1))
except Exception as e:
    print(e)
print("Posicion 02:",lista_02.buscarPosicion(10))
print("Posicion 03:",lista_02.buscarPosicion(3))

#Eliminar
print("Eliminar 01:",lista_02.eliminarInfo(100))
print("Lista 02:", lista_02)
print("Eliminar 02:",lista_02.eliminarInfo(40))
print("Lista 02:", lista_02)
print("Eliminar 03:",lista_02.eliminarInfo(10))
print("Lista 02:", lista_02)
print("Eliminar 04:",lista_02.eliminarInfo(60))
print("Lista 02:", lista_02)
"""
#prueba 3

#Creacion instancia
listaNumeros = ListaSimple()

#Adicion elementos
listaNumeros.adicionarAlInicio(1)
listaNumeros.adicionarAlInicio(6)
listaNumeros.adicionarAlInicio(1)
listaNumeros.adicionarAlInicio(1)
listaNumeros.adicionarAlInicio(1)
listaNumeros.adicionarAlInicio(3)

print("Lista de Numero:",listaNumeros)
#print(listaNumeros.eliminarPorPosicion(2))
#print("se repite ",listaNumeros.buscarYContarUnDato(1)," veces")
#print("Lista  con numeros eliminados")
#listaNumeros.EliminarPenultimo()
print('posicion de Datos consecutivos: ', listaNumeros.buscarPosicionDatoConsecutivos(1))

#Prueba 4
print("Lista de Numero:",listaNumeros.obtenerListaInvertida())
"""
#Creacion instancia
listaNumeros = ListaSimple()

#Adicion elementos

listaNumeros.adicionarAlInicio(1)
listaNumeros.adicionarAlInicio(2345)
listaNumeros.adicionarAlInicio(12)
listaNumeros.adicionarAlInicio(45)
listaNumeros.adicionarAlInicio(4)
listaNumeros.adicionarAlInicio(25)

print(listaNumeros)
listaNumeros.moverElemento(0, 1)
print("elementos movidos")
print(listaNumeros)
"""

#Creacion instancia
"""
listaNumeros = ListaSimple()

#Adicion elementos
listaNumeros.adicionarAlFinal(1)
listaNumeros.adicionarAlFinal(2345)
listaNumeros.adicionarAlFinal(7)
listaNumeros.adicionarAlFinal(7)
listaNumeros.adicionarAlFinal(7)
print(listaNumeros)
print(listaNumeros.buscarPosicionesDato(7))
print(listaNumeros.buscarElementosEntrePosiciones(1,3))
"""
