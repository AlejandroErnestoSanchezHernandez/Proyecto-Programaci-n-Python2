#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 11:06:52 2025

@author: Alejandro Ernesto Sanchez Herandez

Este modulo tiene la funcion de registrar empleado  en la base de datoss
"""

from datetime import datetime
import sqlite3
from rich.console import Console
from rich import print

# Funcionque agrega un empleado a la base de datos, el usuario pone sus datos  y el cursor lo agrega a la tabla 
def creaEmpleado():
    conx=sqlite3.connect("log_llamadas.db")
    cursor=conx.cursor()
    consola = Console()

    nombre = consola.input("[dark_cyan]Nombre(s): [/dark_cyan]")
    primerApellido = consola.input("[dark_cyan]Primer apellido: [/dark_cyan]")
    segundoApellido = consola.input("[dark_cyan]Segundo apellido: [/dark_cyan]")
    telefono = consola.input("[dark_cyan]Teléfono: [/dark_cyan]")
    extension = consola.input("[dark_cyan]Extensión: [/dark_cyan]")
    correo = consola.input("[dark_cyan]Correo electrónico: [/dark_cyan]")
    celular = consola.input("[dark_cyan]Celular: [/dark_cyan]")
    empresa = consola.input("[dark_cyan]Nombre de la empresa: [/dark_cyan]")
    calle = consola.input("[dark_cyan]Calle: [/dark_cyan]")
    numero = consola.input("[dark_cyan]Número: [/dark_cyan]")
    codigoPostal = consola.input("[dark_cyan]Código postal: [/dark_cyan]")
    estado = consola.input("[dark_cyan]Estado: [/dark_cyan]")
    pais = consola.input("[dark_cyan]País: [/dark_cyan]")
    puesto = consola.input("[dark_cyan]Puesto laboral: [/dark_cyan]")
    fechaRegistro = datetime.now().strftime('%Y-%m-%d')        
    cursor.execute('''
        INSERT INTO empleados (nombre, primer_apellido, segundo_apellido, telefono, extension, correo, celular, empresa, calle, numero, codigo_postal, estado, pais, puesto, fecha_registro)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nombre, primerApellido, segundoApellido, telefono, extension, correo, celular, empresa, calle, numero, codigoPostal, estado, pais, puesto, fechaRegistro))
    conx.commit()
    conx.close()
    print("\n [green]Registro exitoso.[/green]\n")
