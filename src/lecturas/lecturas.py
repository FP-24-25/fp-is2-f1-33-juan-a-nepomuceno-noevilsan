'''
Created on 11 oct 2024

@author: noelia
'''

from typing import Optional

# Dado un archivo de texto de nombre fichero, cuyos términos están separados mediante el separador sep, implemente una función que, dados el nombre del fichero, el separador y una palabra cad, cuente cuántas veces aparece dicha palabra dentro del fichero

def ejercicio_6(nombre:str, sep:str, cad:str):
    numpalabras=0 # Número
    with open(nombre) as f:
        flist=f.read().split(sep)
        for i in flist:
            if i.lower()==cad.lower():
                numpalabras+=1
    return numpalabras
    
# Dado un archivo de texto de nombre fichero y una cadena de texto cad, implemente una función que devuelva una lista con aquellas líneas que contengan dicha cadena de texto

def ejercicio_7(nombre:str, cad:str):
    lista=[]
    with open(nombre) as f:
        for i in f.readlines():
                for e in i.split():
                    if e.lower().strip()==cad.lower():
                        lista.append(i.strip())
    return lista
    
# Dado un archivo de texto de nombre fichero, implemente una función que encuentre todas las palabras únicas del archivo de texto y las devuelva en una lista sin repeticiones. Tenga en cuenta que las palabras están separadas por espacios.

def ejercicio_8(nombre:str):
    lista=[] # Hacemos una lista vacía
    with open(nombre) as f: # Abrimos el documento
        for i in f.readlines():
            for palabra in i.split():
                if palabra not in lista:
                    lista.append(palabra)
    return lista
    
# Dado un fichero csv de nombre fichero, cuyos términos están separados mediante el separador sep, implemente una función que devuelva la longitud media de las líneas de dicho fichero. La cabecera de dicha función es la siguiente:

def longitud_promedio_lineas(nombre:str)->Optional[float]:
    numpalabras=0 # Número de palabras en total
    numlineas=0
    with open(nombre) as f:
        for i in f.readlines():
            numlineas+=1
            for palabra in i.split(","):
                numpalabras+=1
        if numpalabras==0:
            return None
    return numpalabras/numlineas

if __name__ == '__main__':          
    pass
    