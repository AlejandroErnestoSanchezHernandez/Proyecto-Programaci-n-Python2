#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 13:50:51 2025

@author: Alejandro Ernesto Sanchez Hernandez

Este modulo permite al usuario el poder ver las llamadas realizadas
"""
import sqlite3

def verLlamadas():
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

    print("\nRegistros de llamadas:")
    for log in logs:
        print(f"ID: {log[0]}, \n\tPersona: {log[1]} {log[2]} {log[3]}, \n\tFecha: {log[4]}, \n\tHora: {log[5]}, \n\tResumen: {log[6]}")
    print("")