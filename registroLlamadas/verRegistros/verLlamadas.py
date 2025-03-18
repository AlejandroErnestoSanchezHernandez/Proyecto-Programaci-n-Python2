#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 13:50:51 2025

@author: Alejandro Ernesto Sanchez Hernandez

Este modulo permite al usuario el poder ver las llamadas realizadas
"""
import sqlite3
from rich.console import Console
from rich.table import Table

def verLlamadas():
    consola = Console()
    tabla = Table(title="[bold yellow]Registros de llamadas[/bold yellow]", border_style="blue")

    conx = sqlite3.connect("log_llamadas.db")
    cursor = conx.cursor()
    cursor.execute('''
        SELECT llamadasTelefonicas.id, empleados.nombre, empleados.primer_apellido, empleados.segundo_apellido, 
               llamadasTelefonicas.fecha_llamada, llamadasTelefonicas.hora_llamada, llamadasTelefonicas.resumen
        FROM llamadasTelefonicas
        JOIN empleados ON llamadasTelefonicas.id_persona = empleados.id
    ''')
    logs = cursor.fetchall()
    conx.close()

    if not logs:
        print("\nNo hay registros de llamadas.\n")
        return
    
    tabla.add_column("ID",justify="center", style="cyan")
    tabla.add_column("Persona", justify="center", style="cyan")
    tabla.add_column("Fecha", justify="center", style="cyan")
    tabla.add_column("Hora", justify="center", style="cyan")
    tabla.add_column("Resumen", justify="center", style="cyan")
    
    for registros in logs:
        persona = f"{registros[1]} {registros[2]} {registros[3]}"
        tabla.add_row(str(registros[0]),str( persona), str(registros[4]), str(registros[5]), str(registros[6]))
    
    consola.print(tabla)    

