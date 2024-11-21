'''
Created on 29 oct 2024

@author: noelia
'''

from __future__ import annotations
from typing import List, TypeVar, Generic, Callable
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
    
    #### A partir de aquí empiezan las modificaciones del examen. Los tests de estas funciones se encuentran en Test_Lista_ordenada
    
    def contains(self, e:E)->bool:
        if e in self.elements: # Si se encuentra en la lista
            return True
        else:
            return False
        
    def find(self,func:Callable[[E], bool])->E | None:
        for i in self.elements:
            if func(i): # Si se cumple la función
                return i # Devolverá el primer elemento en el que se cumpla 
        return None # Si ningún elemento cumple la función, devolverá None
    
    def filter(self, func: Callable[[E], bool])->list[E]:
        ls=[]
        for i in self.elements:
            if func(i): # Es lo mismo que find, solo que esta vez vamos añadiendo los elementos en una lista
                ls.append(i)
        return ls
                
        
if __name__ == '__main__':
    pass