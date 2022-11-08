from listas_2022 import *
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
listaNumeros.moverElemento(5, 2)
print("elementos movidos")
print(listaNumeros)

