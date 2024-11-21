'''
Created on 8 oct 2024

@author: noelia
'''
from us.lsi.tools import Preconditions
from math import factorial
from itertools import repeat

'''EJERCICIO 1'''

def primer_ejercicio(n:int, k:int):
    Preconditions.check_argument(n>k, "n debe ser mayor que k")
    s=1 # Como vamos a hacer un producto, ponemos uno (si pusieramos 0, nos saldría error)
    for i in range(0,k+1): # Si pusieramos simplemente k, el rango sería de 0 a k-1
        s*=n-i+1 # Realizamos el producto
    return s

'''EJERCICIO 2'''

def segundo_ejercicio(a:int, r:int, k:int):
    s=1
    # a_n=a-r^{n-1}
    for n in range (1, k+1):
       s*=a*r**(n-1)
    return s
    
'''EJERCICIO 3'''

def tercer_ejercicio(n:int, k:int):
    Preconditions.check_argument(n>=k, "n tiene que ser mayor o igual que k")
    factorial_n=1
    factorial_k=1
    factorial_resta=1
    # Se podría hacer también el factorial con alguna función de una librería pero yo voy a hacerlo por 'for'
    for i in range(1, n+1):
        factorial_n*=i # Factorial de n    
    for i in range(1, k+1):
        factorial_k*=i # Factorial de k
    for i in range(1, n-k+1):
        factorial_resta*=i # Factorial de n-k
    factorial=factorial_n/(factorial_k*factorial_resta)
    return factorial

'''EJERCICIO 4'''

def cuarto_ejercicio(n:int, k:int):
    sum=0
    for i in range(0, k):
        sum+=(-1)**i*tercer_ejercicio(k+1, i+1)*(k-i)**n # Sumatorio
    factorial_k=1
    for i in range(1, k+1):
        factorial_k*=i # Factorial de k
    solucion=(1/factorial_k)*sum
    return solucion

'''EJERCICIO 5'''

def quinto_ejercicio(a:float, e:float):
    def f(x):
        return 2*x**2
    def der_f(x):
        return 4*x
    xn1=a-(f(a)/der_f(a))
    while (abs(f(xn1))>=e):
            xn1=a-(f(a)/der_f(a))
            a=xn1
    return xn1
    
if __name__ == '__main__':
    pass
