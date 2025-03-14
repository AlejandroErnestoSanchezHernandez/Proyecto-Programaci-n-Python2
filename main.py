#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 13:46:41 2025

@author: Alejandro Ernesto Sanchez Hernandez

Este es el main, el script principal del programa
"""

#from sys import path 

#path.append("funcionesRegistroLlamadas")

#from registroLlamadas.bd.crearTabla import creaTabla
#import registroLlamadas

#registroLlamadas.bd.crearTabla.creaTabla()

from registroLlamadas.bd.crearTabla import creaTabla
from registroLlamadas.registros.creaEmpleado import creaEmpleado
from registroLlamadas.registros.regLlamada import regLlamada
from registroLlamadas.verRegistros.verLlamadas import verLlamadas
from registroLlamadas.verRegistros.verPersonas import verPersonas
from registroLlamadas.registros.editarLlamada import elimnarLlamada
from registroLlamadas.registros.editarLlamada import modLlamada
import os
#import datetime.datetime

def main():
    creaTabla()
    contador = 0 

    while True:
       
        print("\n--- Menú ---")
        print("Versión del programa: 0.5.0")
        print("1. Registrpo persona")
        print("2. Registro llamada")
        print("3. Ver personas registradas")
        print("4. Ver registros de llamadas")
        print("5. Modificar llamada")
        print("6. Eliminar llamada")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            creaEmpleado()
            contador+=1
        elif opcion == "2":
            regLlamada()
            contador+=1
        elif opcion == "3":
            verPersonas()
            contador+=1
        elif opcion == "4":
            verLlamadas()
            contador+=1
        elif opcion == "5":
            contador+=1
            modLlamada()
        elif opcion == "6":
            contador+=1    
            elimnarLlamada()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            contador+=1
         # Limpiar la terminal
        if contador == 3:
            os.system('cls' if os.name == 'nt' else 'clear')    
        #print(contador)    

if __name__ == "__main__":
    main()



