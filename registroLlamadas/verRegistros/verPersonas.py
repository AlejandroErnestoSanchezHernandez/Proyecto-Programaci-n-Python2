#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 12:31:07 2025

@author: Alejandro Ernesto Sanchez Hernandez

Este modulo permite al usuario ver las personas registradas en la base de datos
"""

import sqlite3
from rich.console import Console
from rich.table import Table

def verPersonas():
    consola = Console()
    tabla = Table(title="[bold yellow]Ver personas[/bold yellow]", border_style="blue")
    
    conx = sqlite3.connect("log_llamadas.db")
    cursor = conx.cursor()
    cursor.execute("SELECT id, nombre, primer_apellido, segundo_apellido, telefono, extension, celular, correo, empresa FROM empleados")
    personas = cursor.fetchall()
    conx.close()
    
    if not personas:
        print("\nNo hay personas registradas.\n")
        return

    tabla.add_column("ID",justify="center", style="cyan")
    tabla.add_column("Persona", justify="center", style="cyan")
    tabla.add_column("Telefono", justify="center", style="cyan")
    tabla.add_column("Celular", justify="center", style="cyan")
    tabla.add_column("Correo", justify="center", style="cyan")
    tabla.add_column("Empresa", justify="center", style="cyan")
    
    for personas in personas:
        persona = f"{personas[1]} {personas[2]} {personas[3]}"
        tabla.add_row(str(personas[0]),str( persona), str(personas[4]), str(personas[5]), str(personas[6]), str(personas[7]), str(personas[8]) )
    
    consola.print(tabla)    
