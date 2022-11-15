from listasDobles2022 import *

#Creacion instancia
lista_01 = ListaDoble()
#Adicion de elementos al inicio
"""
lista_01.adicionarAlInicio(1)
lista_01.adicionarAlInicio(2)
lista_01.adicionarAlInicio(3)
"""
#Adicion de elementos al final
lista_01.adicionarAlFinal('a')
lista_01.adicionarAlFinal('b')
lista_01.adicionarAlFinal('c')
print("Lista:",lista_01)
print("Longitud:",lista_01.longitud())
print("Lista esta vacia?:",lista_01.estaVacia())