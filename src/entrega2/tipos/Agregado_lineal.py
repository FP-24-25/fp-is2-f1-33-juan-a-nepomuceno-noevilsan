'''
Created on 29 oct 2024

@author: noelia
'''

from __future__ import annotations
from typing import List, TypeVar, Generic
from abc import abstractmethod

E=TypeVar('E')

class Agregado_Lineal(Generic[E]):
    
    def __init__(self):
        self.__elements:List[E]=[]

    @property
    def size(self)->int:
        return len(self.__elements)

    @property
    def is_empty(self)->bool:
        return self.size==0

    @property
    def elements(self)->List[E]:
        return self.__elements

    @abstractmethod
    def add(self, e:E)->None:
        pass

    def add_all(self, ls:List[E])->None:
        for i in ls:
            self.add(i)

    def remove(self):
        return self.elements.pop(0)

    def remove_all(self)->list[E]:
        ls=[]
        while self.is_empty==False:
            ls.append(self.remove())
        return ls
            

if __name__ == '__main__':
    pass