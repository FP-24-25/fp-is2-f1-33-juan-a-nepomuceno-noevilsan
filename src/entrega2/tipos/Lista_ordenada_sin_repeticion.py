'''
Created on 29 oct 2024

@author: noelia
'''
from __future__ import annotations
from typing import TypeVar, Callable, Generic
from entrega2.tipos.Agregado_lineal import Agregado_Lineal

E=TypeVar('E')
R=TypeVar('R')

class ListaOrdenadaSinRepetición(Agregado_Lineal[E], Generic[E,R]):
    def __init__(self, order:Callable[[E], R]):
        super().__init__() # Para que se inicialice correctamente Agregado_Lineal[E]
        self.__order=order
        
    @property
    def order(self)->Callable[[E],R]:
        return self.__order
    
    @staticmethod
    def of(order:Callable[[E],R])->ListaOrdenadaSinRepetición[E,R]:
        return ListaOrdenadaSinRepetición(order)
    
    def __index_order(self, e:E)->int:
        for index, elemento in enumerate(self.elements):
            if self.order(e)<self.order(elemento):
                return index
        return len(self.elements)
    
    def add(self, e:E)->None:
        order=self.__index_order(e)
        if e not in self.elements:
            self.elements.insert(order, e)
    
    def __str__(self)->str:
        return f"ListaOrdenadaSinRepetición([{', '.join(map(str, self.elements))}])"
    
if __name__ == '__main__':
    pass
    