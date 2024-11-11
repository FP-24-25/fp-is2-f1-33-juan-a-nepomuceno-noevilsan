'''
Created on 29 oct 2024

@author: noelia
'''

from __future__ import annotations
from typing import TypeVar, Generic, List
from us.lsi.tools import Preconditions

E=TypeVar('E')
P=TypeVar('P')

class ColaDePrioridad(Generic[E,P]):
    def __init__(self):
        self.__elements:List[E]=[]
        self.__priorities:List[P]=[]

    @property
    def size(self)->int:
        return len(self.__elements)

    @property
    def is_empty(self)->bool:
        return self.size==0

    @property
    def elements(self)->List[E]:
        return self.__elements
    
    def add(self, e:E, priority:P)->None:
        p=self.__index_order(priority) # Descubrimos en qué posición debemos ponerlo
        self.__elements.insert(p, e)
        self.__priorities.insert(p, priority) # Lo ponemos en dicha posición
    
    # Objetivo de __index_order: calcula el índice en el que se debe insertar el nuevo elemento, de acuerdo con su prioridad. Para ello, debemos comparar las prioridades de los elementos que ya están ahí. 
    def __index_order(self, priority:P)->int:
        for index, prioridad in enumerate(self.__priorities):
            if priority<prioridad:
                return index
        return len(self.__priorities)
    
    def remove(self)->E:
        Preconditions.check_argument(len(self.__elements)>0, "El agregado está vacío")
        return self.elements.pop(0)
    
    def remove_all(self)->list[E]:
        ls=[]
        while self.is_empty==False:
            ls.append(self.remove())
        return ls
    
    def decrease_priority(self, e:E, new_priority:P)->None:
        self.elements.remove(e)
        self.add(e, new_priority)
    
    def __str__(self)->str:
        return f"ColaDePrioridad([{', '.join(map(str, zip(self.__elements, self.__priorities)))}])" 

if __name__ == '__main__':
    Cola=ColaDePrioridad()
    Cola.add("Paciente A",2)
    Cola.add("Paciente B",2)
    Cola.add("Paciente C",1)
    Cola.add("Paciente D",3)
    Cola.add("Paciente E",1)
    Cola.decrease_priority("Paciente A", 3)
    print(Cola)