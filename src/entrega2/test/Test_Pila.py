'''
Created on 29 oct 2024

@author: noelia
'''
from entrega2.tipos.Pila import Pila

if __name__ == '__main__':
    print("TEST DE PILA\n######################")
    pila=Pila.of()
    print("Se añade en este orden: 3,1,2")
    pila.add(3)
    pila.add(1)
    pila.add(2)
    print(f"Resultado de la fila: {pila}")
    print("######################")
    print(f"El elemento eliminado al utilizar remove(): {pila.remove()}")
    print("######################")
    pila.add(2)
    print(f"Elementos eliminados utilizando remove_all: {pila.remove_all()}")