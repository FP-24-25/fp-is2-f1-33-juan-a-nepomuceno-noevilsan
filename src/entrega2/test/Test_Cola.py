'''
Created on 29 oct 2024

@author: noelia
'''
from entrega2.tipos.Cola import Cola

if __name__ == '__main__':
        print("TEST DE COLA\n######################")
        cola:Cola[int]=Cola.of()
        cola.add_all([23,47,1,2,-3,4,5])
        print(f"Creación de una cola vacía a la que luego se le añaden con un solo método los números: 23, 47, 1, 2, -3, 4, 5\nResultado de la cola: {cola}")
        print("######################")
        print(f"Elementos eliminados utilizando remove_all: {cola.remove_all()}")