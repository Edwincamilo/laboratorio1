# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 12:06:29 2021

@author: 57314
"""

def retornar_superficie(lado):
    sup=lado*lado
    return sup


# bloque principal del programa

va=int(input("Ingrese el valor del lado del cuafrado:"))
superficie=retornar_superficie(va)
print("La superficie del cuadrado es",superficie)