'''
Created on 11 oct 2024

@author: noelia
'''

from lecturas.lecturas import ejercicio_6, ejercicio_7, ejercicio_8, longitud_promedio_lineas

if __name__ == '__main__':
    
    print("################################################ \n TEST DE LA FUNCIÓN 6:")
    print("El número de veces que aparece la palabra quijote en el fichero resources/lin_quijote.txt es: {num}".format(num=ejercicio_6("ficheros/lin_quijote.txt", " ", "quijote")))
        
    print("################################################ \n TEST DE LA FUNCIÓN 7:")
    print("Las líneas en las que aparece la palabra quijote son: {num}".format(num=ejercicio_7("ficheros/lin_quijote.txt", "quijote")))
        
    print("################################################ \n TEST DE LA FUNCIÓN 8:")
    print("Las palabras únicas en el fichero resources/archivo_palabras.txt son: {num}".format(num=ejercicio_8("ficheros/archivo_palabras.txt")))
        
    print("################################################ \n TEST DE LA FUNCIÓN 9:")
    print("La longitud promedio de las líneas del fichero resources/palabras_random.csv es: {num}".format(num=longitud_promedio_lineas("ficheros/palabras_random.csv")))
    print("La longitud promedio de las líneas del fichero resources/palabras_random.csv es: {num}".format(num=longitud_promedio_lineas("ficheros/vacio.csv")))