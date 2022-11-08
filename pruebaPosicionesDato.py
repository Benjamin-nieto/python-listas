from listas_2022 import *
#Creacion instancia
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