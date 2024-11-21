'''
Created on 8 oct 2024

@author: noelia
'''
from funciones.funciones import primer_ejercicio, segundo_ejercicio, tercer_ejercicio, cuarto_ejercicio, quinto_ejercicio

if __name__ == '__main__':
    print("################################################ \n TEST DE LA FUNCIÓN 1:")
    print("El producto de 4 y 2 es: {num}".format(num=primer_ejercicio(4,2)))
    
    print("################################################ \n TEST DE LA FUNCIÓN 2:")
    print("El producto de la secuencia geométrica con a1 = 3, r = 5 y k = 2 es: {num}".format(num=segundo_ejercicio(3, 5, 2)))
    
    print("################################################ \n TEST DE LA FUNCIÓN 3:")
    print("El número combinatorio de 4 y 2 es: {num}".format(num=tercer_ejercicio(4, 2)))
    
    print("################################################ \n TEST DE LA FUNCIÓN 4:")
    print("El número S(n,k) siendo n = 4 y k = 2 es: {num}".format(num=cuarto_ejercicio(4, 2)))
    
    print("################################################ \n TEST DE LA FUNCIÓN 4:")
    print("Resultado de la función 5 con a = 3 y e = 0.001, f(x) = 2x^2 y f'(x) = 4x: {num}".format(num=quinto_ejercicio(3, 0.001)))