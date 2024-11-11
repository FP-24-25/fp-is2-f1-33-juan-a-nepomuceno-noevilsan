'''
Created on 29 oct 2024

@author: noelia
'''

from entrega2.tipos.Lista_ordenada_sin_repeticion import ListaOrdenadaSinRepetición

if __name__ == '__main__':
    print("TEST DE LISTA ORDENADA SIN REPETICIÓN\n######################")
    print("Creación de una lista con criterio de orden lambda x:-x")
    lista:ListaOrdenadaSinRepetición[int,int]=ListaOrdenadaSinRepetición.of(lambda x:-x)
    print("Se añade en este orden: 23, 47, 47, 1, 2, -3, 4, 5")
    lista.add(23)
    lista.add(47)
    lista.add(47)
    lista.add(1)
    lista.add(2)
    lista.add(-3)
    lista.add(4)
    lista.add(5)
    print(f"Resultado de la lista: {lista}")
    print("######################")
    print(f"El elemento eliminado al utilizar remove(): {lista.remove()}")
    print("######################")
    lista.add(47)
    print(f"Elementos eliminados utilizando remove_all: {lista.remove_all()}")
    print("######################")
    lista.add_all([47,23,5,4,2,1,-3])
    print("Comprobado si se añaden los elementos en la posición correcta:")
    lista.add(0)
    print(f"Lista después de añadirle el 0: {lista}")
    lista.add(0)
    print(f"Lista después de añadirle el 10: {lista}")
    lista.add(7)
    print(f"Lista después de añadirle el 7: {lista}")
    
    
    
