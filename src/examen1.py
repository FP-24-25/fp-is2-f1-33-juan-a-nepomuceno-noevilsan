'''
Created on 24 oct 2024

@author: noelia
'''

from us.lsi.tools import Preconditions
from lecturas.lecturas import ejercicio_6
from funciones.funciones import tercer_ejercicio
from _ast import Try

##########################
# EJERCICIO 1

def P2(n:int, k:int, i:int=1):
    Preconditions.check_argument(n>=k, "n debe ser mayor o igual que k")
    Preconditions.check_argument(n>0, "n debe ser positivo")
    Preconditions.check_argument(k>0, "k debe ser positivo")
    Preconditions.check_argument(i>0, "i debe ser positivo")
    Preconditions.check_argument(i<k+1, "i debe ser menor que k+1")
    sol=1
    for i in range (k-1):
        sol*=(n-i+1)
    return sol

def C2(n:int, k:int):
    Preconditions.check_argument(n>k, "n debe ser mayor que k")
    factorial_n=1
    factorial_k=1
    factorial_resta=1
    for i in range(1, n+1): 
        factorial_n*=i
    for i in range(1, k+2):
        factorial_k*=i
    for i in range(1, n-(k+1)+1):
        factorial_resta*=i
    factorial=factorial_n/(factorial_k*factorial_resta)
    return factorial

def S2(n:int, k:int):
    Preconditions.check_argument(n>=k, "n debe ser mayor o igual que k")
    sum=0
    for i in range(0, k):
        sum+=(-1)**i*tercer_ejercicio(k, i)*(k-i)**(n+1) # Sumatorio
    factorial_k=1
    for i in range(1, (k+2)+1):
        factorial_k*=i # Factorial de k
    solucion=(1/n*factorial_k)*sum
    return solucion

def palabrasMasComunes(fichero:str, n:int=5)->list[str]:
    Preconditions.check_argument(n>1, "n debe ser mayor que 1")
    lista=[]
    lista2=[]
    e=0
    with open(fichero) as f:
        for i in f.readlines():
            for palabra in i.split():
                lista.append(palabra)
    for i in lista:
        if (i.lower().strip(),ejercicio_6(fichero, " ", i)) not in lista2:
            lista2.append((i.lower().strip(),ejercicio_6(fichero, " ", i)))
    sortedlista2=sorted(lista2, key=lambda x: x[1], reverse=True)
    return sortedlista2[:n]

if __name__ == '__main__':
    
    print("########################### EJERCICIO 1")
    try:
        print(P2(10, 30))
    except AssertionError:
        print(P2(3, 2))
        
    try:
        P2(-1, -1, -1)
    except AssertionError:
        print(P2(4,3))
        
    try:
        print(P2(1,1,3))
    except AssertionError:
        print(P2(3,2)) 
        
    print("########################### EJERCICIO 2")
        
    try:
        print(C2(2,3))
    except AssertionError:
        print(C2(10,2))
        
    print("########################### EJERCICIO 3")
    
    try:
        print(S2(3,4))
    except AssertionError:
        print(S2(4,3))
        
    print("########################### EJERCICIO 4")
    
    try:
        print(palabrasMasComunes("test/ficheros/archivo_palabras.txt", -1))
    except:
        print(palabrasMasComunes("test/ficheros/archivo_palabras.txt"))
     
        
        