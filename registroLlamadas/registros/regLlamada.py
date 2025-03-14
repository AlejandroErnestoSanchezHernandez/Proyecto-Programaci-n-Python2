#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 12:03:23 2025

@author: Alejandro Ernesto Sanchez Hernandez

Este modulo da al usuario un modo para agregar llamadas a la base de datos
"""
from datetime import datetime
import sqlite3
from.creaEmpleado import creaEmpleado

def regLlamada():
    conx=sqlite3.connect("log_llamadas.db")
    cursor=conx.cursor()    
    cursor.execute("SELECT id, nombre, primer_apellido, segundo_apellido FROM empleados")
    personas = cursor.fetchall()
    
    if not personas:
        print("\nNo hay personas registradas. Registre una persona antes de registrar una llamada.\n")
        conx.close()
        return
    
    print("\nPersonas registradas:")
    for persona in personas:
        print(f"ID: {persona[0]}, Nombre: {persona[1]} {persona[2]} {persona[3]}")
        
    
    while True:
        
        idPersona = input("Ingrese el ID de la persona a la que llamó: ")
        cursor.execute("SELECT id FROM empleados WHERE id = ?", (idPersona,))
        if cursor.fetchone():
            break
        print("ID no válido. ¿Deseas registrar una nueva persona?")
        print("1. Sí")
        print("2. No, volver a intentar.")
        print("3. Regresar al menú principal.")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            creaEmpleado()
            return
        elif opcion == "3":
            return
    
    fecha_Llamada = input(f"Fecha de la llamada (YYYY-MM-DD) [Por defecto: {datetime.now().strftime('%Y-%m-%d')}]: ") or datetime.now().strftime('%Y-%m-%d')
    hora_Llamada = input(f"Hora de la llamada (HH:MM) [Por defecto: {datetime.now().strftime('%H:%M')}]: ") or datetime.now().strftime('%H:%M')
    resumen = input("Resumen de la llamada: ")
    
    cursor.execute('''
        INSERT INTO llamadasTelefonicas (id_Persona, fecha_llamada, hora_llamada, resumen)
        VALUES (?, ?, ?, ?)
    ''', (idPersona, fecha_Llamada, hora_Llamada, resumen))
    conx.commit()
    conx.close()
    print("\nLlamada registrada exitosamente.\n")