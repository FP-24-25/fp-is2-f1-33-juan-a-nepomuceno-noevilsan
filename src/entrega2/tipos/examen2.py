'''
Created on 21 nov 2024

@author: noelia
'''

#### El ejercicio 2 se encuentra en el módulo Agregado_Lineal

from __future__ import annotations
from typing import TypeVar, Generic, Callable
from entrega2.tipos.Agregado_lineal import Agregado_Lineal

E=TypeVar('E')

class ColaConLimite(Agregado_Lineal[E], Generic[E]):
    def __init__(self, capacidad:int):
        super().__init__() # Para que pueda heredera los métodos de Agregado_Lineal
        self.__capacidad=capacidad # Privado
        
    @property
    def capacidad(self)->int:
        return self.__capacidad
    
    @staticmethod
    def of(capacidad:int)->ColaConLimite[E]:
        return ColaConLimite(capacidad) 
        
    def add(self, e:E)->None:
        if self.size>=self.capacidad:
            raise OverflowError("La cola está llena")
        else:
            self.elements.append(e)
            
    def is_full(self)->str:
        if self.size>=self.capacidad: # self.size es un método de Agregado_Lineal que nos dirá la cantidad de elementos que hay en nuestra lista. Si está es mayor o igual a la capacidad: 
            return "La cola está llena"
        else:
            return "La cola no está llena"
        
    def __str__(self)->str:
        return f"ColaConLimite([{', '.join(map(str, self.elements))}])"

if __name__ == '__main__':
    cola=ColaConLimite[str].of(3)
    print("La capacidad será: {a}".format(a=cola.capacidad))
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    cola.add("Tarea 3")
    try:
        cola.add("Tarea 4")
    except OverflowError as e:
        print(e) # Debe imprimir "La cola está llena"
    print(cola.remove()) # Como el código está heredado de AgregadoLineal, todos sus métodos son utilizables aquí
    # Ahora me aparecerá que no está llena:
    print(cola.is_full())
    # Pero si añado otro:
    cola.add("Tarea 100")
    print(cola.is_full())
    