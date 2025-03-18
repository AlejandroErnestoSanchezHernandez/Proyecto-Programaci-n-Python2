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
from rich.console import Console
from rich import print



def main():
    creaTabla()
    contador = 0 
    consola = Console()

    while True:
        if contador % 4 == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
        print("[yellow]\n--- Menú ---[/yellow]")
        print("[bright_magenta]Versión del programa:[/bright_magenta] 0.5.0")
        print("1. [green]Registro persona[/green]")
        print("2. [green]Registro llamada[/green]")
        print("3. [green]Ver personas registradas[/green]")
        print("4. [green]Ver registros de llamadas[/green]")
        print("5. [green]Modificar llamada[/green]")
        print("6. [green]Eliminar llamada[/green]")
        print("7. [red]Salir[/red]")

        opcion = consola.input("[dark_cyan]Selecciona una opción: [/dark_cyan]")

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
        print(contador)    
         
if __name__ == "__main__":
    main()



