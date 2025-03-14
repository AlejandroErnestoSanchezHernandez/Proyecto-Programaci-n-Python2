#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 12:31:07 2025

@author: Alejandro Ernesto Sanchez Hernandez

Este modulo permite al usuario ver las personas registradas en la base de datos
"""

import sqlite3

def verPersonas():
    
    conx = sqlite3.connect("log_llamadas.db")
    cursor = conx.cursor()
    cursor.execute("SELECT id, nombre, primer_apellido, segundo_apellido, telefono, extension, celular, correo, empresa FROM empleados")
    personas = cursor.fetchall()
    conx.close()
    
    if not personas:
        print("\nNo hay personas registradas.\n")
        return
    
    print("\nPersonas registradas:")
    for persona in personas:
        print(f"ID: {persona[0]}, Nombre: {persona[1]} {persona[2]} {persona[3]}, \n\tTeléfono: {persona[4]}, \n\tExtensión: {persona[5]}, \n\tCelular: {persona[6]}, \n\tCorreo: {persona[7]}, \n\tEmpresa: {persona[8]}")
    print("")