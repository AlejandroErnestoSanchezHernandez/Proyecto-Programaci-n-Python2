#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 11:11:03 2025

@author: Alejandro Ernesto Sanchez Hernandez 

Este modulo permite ditar una de las llamadas registradas
"""

import sqlite3
from datetime import datetime
import sys
from rich.console import Console
from rich import print
from rich.table import Table

#sys.path.append("../verRegistros/")
#from verRegistros.verLlamadas import  verLlamadas


sys.path.append("../..")  # Agregar el directorio padre de 'verRegistros'
from registroLlamadas.verRegistros.verLlamadas import verLlamadas
#from registroLlamadas.verRegistros.verLlamadas import verLlamadas

consola = Console()
def elimnarLlamada():
    #consola = Console()
    conx = sqlite3.connect("log_llamadas.db")
    cursor = conx.cursor()
    verLlamadas()
    #cursor.execute("SELECT id, nombre, primer_apellido, segundo_apellido FROM llamadasTelefonicas")
    
    
    while True:
        idLlamada = consola.input("[dark_cyan]Ingrese el ID de la llamada a elimnar: [/dark_cyan]")
        cursor.execute("SELECT id FROM llamadasTelefonicas WHERE id = ?", (idLlamada ,))
        if cursor.fetchone():
            break
        print("[red]ID no válido. Intenta nuevamente.[/red]")

    cursor.execute("DELETE FROM llamadasTelefonicas WHERE id = ?", (idLlamada ,))
    conx.commit()
    conx.close()
    
    print(f"[green]La llamada con ID {idLlamada} ha sido eliminada correctamente.[/green]")

    
def modLlamada():
    conx= sqlite3.connect("log_llamadas.db")
    cursor = conx.cursor()
    verLlamadas()
    #cursor.execute("SELECT id, nombre, primer_apellido, segundo_apellido FROM llamadasTelefonicass")
    
    while True:
        idLlamada = consola.input("[dark_cyan]Ingrese el ID de la llamada a modificar: [/dark_cyan]")
        cursor.execute("SELECT id FROM llamadasTelefonicas WHERE id = ?", (idLlamada ,))
        if cursor.fetchone():
            break
        print("[red]ID no válido. Intenta nuevamente.[/red]")
        
    fechaLlamada = consola.input(f"[dark_cyan]Fecha de la llamada (YYYY-MM-DD) [Por defecto: {datetime.now().strftime('%Y-%m-%d')}]: [/dark_cyan]") or datetime.now().strftime('%Y-%m-%d')
    horaLlamada = consola.input(f"[dark_cyan]Hora de la llamada (HH:MM) [Por defecto: {datetime.now().strftime('%H:%M')}]: [/dark_cyan]") or datetime.now().strftime('%H:%M')
    resumen = consola.input("[dark_cyan]Resumen de la llamada: [/dark_cyan]")
    
    cursor.execute("""
        UPDATE llamadasTelefonicas 
        SET fecha_llamada = ?, hora_llamada = ?, resumen = ?
        WHERE id = ?
    """, (fechaLlamada, horaLlamada, resumen, idLlamada))
    conx.commit()
    conx.close()
    