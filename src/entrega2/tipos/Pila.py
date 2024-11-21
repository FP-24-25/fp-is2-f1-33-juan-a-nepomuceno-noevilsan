'''
Created on 29 oct 2024

@author: noelia
'''

from __future__ import annotations
from typing import TypeVar, Callable, Generic
from entrega2.tipos.Agregado_lineal import Agregado_Lineal

E=TypeVar('E')

class Pila(Agregado_Lineal[E], Generic[E]):

    @staticmethod
    def of()->Pila[E]:
        return Pila()
    
    def add(self, e:E):
        self.elements.insert(0, e)
        
    def __str__(self)->str:
        return f"Pila([{', '.join(map(str, self.elements))}])"

if __name__ == '__main__':
    pass
    