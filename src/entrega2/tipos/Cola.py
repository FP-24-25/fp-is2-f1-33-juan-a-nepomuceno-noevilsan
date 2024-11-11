'''
Created on 29 oct 2024

@author: noelia
'''

from __future__ import annotations
from typing import TypeVar, Generic
from entrega2.tipos.Agregado_lineal import Agregado_Lineal

E=TypeVar('E')

class Cola(Agregado_Lineal[E], Generic[E]):

    @staticmethod
    def of()->Cola[E]:
        return Cola()
    
    def add(self, e:E):
        self.elements.append(e)
        
    def __str__(self)->str:
        return f"Cola([{', '.join(map(str, self.elements))}])"

if __name__ == '__main__':
    pass
    