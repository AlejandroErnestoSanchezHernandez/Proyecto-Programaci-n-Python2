#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 12:03:23 2025

@author: Alejandro Ernesto Sanchez Hernandez

Este modulo da al usuario un modo para agregar llamadas a la base de datos
"""
from datetime import datetime
import sqlite3
from rich.console import Console
from rich import print
from rich.table import Table
from.creaEmpleado import creaEmpleado

#Esta funcion permite al usuario registrar una llamada, primero hace un select en la base de datos, si no hay una persona lo indica
# en caso contrario pregunta por el id de la persona que hará el registro (si no es valido el id lo indica). Acto seguido 
def regLlamada():
    consola = Console()
    tabla = Table(title="[bold yellow]Ver personas[/bold yellow]", border_style="blue")
    conx=sqlite3.connect("log_llamadas.db")
    cursor=conx.cursor()    
    cursor.execute("SELECT id, nombre, primer_apellido, segundo_apellido FROM empleados")
    personas = cursor.fetchall()
    
    if not personas:
        print("\[red]nNo hay personas registradas. Registre una persona antes de registrar una llamada.[/red]\n")
        conx.close()
        return
    
    
    tabla.add_column("ID",justify="center", style="cyan")
    tabla.add_column("Persona", justify="center", style="cyan")
    
    for personas in personas:
        persona = f"{personas[1]} {personas[2]} {personas[3]}"
        tabla.add_row(str(personas[0]),str( persona), )
    consola.print(tabla)        
    
    """print("\nPersonas registradas:")
    for persona in personas:
        print(f"ID: {persona[0]}, Nombre: {persona[1]} {persona[2]} {persona[3]}")"""
        
    
    while True:
        
        idPersona = consola.input("[dark_cyan]Ingrese el ID de la persona a la que llamó: [/dark_cyan]")
        cursor.execute("SELECT id FROM empleados WHERE id = ?", (idPersona,))
        if cursor.fetchone():
            break
        print("[red]ID no válido. ¿Deseas registrar una nueva persona?[/red]")
        print("1. Sí")
        print("2. No, volver a intentar.")
        print("3. Regresar al menú principal.")
        opcion = consola.input("Selecciona una opción: ")
        if opcion == "1":
            creaEmpleado()
            return
        elif opcion == "3":
            return
    
    fecha_Llamada = consola.input(f"[dark_cyan]Fecha de la llamada (DD-MM-YY) [Por defecto: {datetime.now().strftime('%d-%m-%Y')}]: [/dark_cyan]") or datetime.now().strftime('%d-%m-%Y')
    hora_Llamada = consola.input(f"[dark_cyan]Hora de la llamada (HH:MM) [Por defecto: {datetime.now().strftime('%H:%M')}]: [/dark_cyan]") or datetime.now().strftime('%H:%M')
    resumen = consola.input("[dark_cyan]Resumen de la llamada: [/dark_cyan]")
    
    cursor.execute('''
        INSERT INTO llamadasTelefonicas (id_Persona, fecha_llamada, hora_llamada, resumen)
        VALUES (?, ?, ?, ?)
    ''', (idPersona, fecha_Llamada, hora_Llamada, resumen))
    conx.commit()
    conx.close()
    print("\n[green]Llamada registrada exitosamente.[/green]\n")