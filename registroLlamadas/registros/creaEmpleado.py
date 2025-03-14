#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 11:06:52 2025

@author: Alejandro Ernesto Sanchez Herandez

Este modulo tiene la funcion de registrar empleado  en la base de datoss
"""

from datetime import datetime
import sqlite3

def creaEmpleado():
    conx=sqlite3.connect("log_llamadas.db")
    cursor=conx.cursor()
    

    nombre = input("Nombre(s): ")
    primerApellido = input("Primer apellido: ")
    segundoApellido = input("Segundo apellido: ")
    telefono = input("Teléfono: ")
    extension =input("Extensión: ")
    correo = input("Correo electrónico: ")
    celular = input("Celular: ")
    empresa = input("Nombre de la empresa: ")
    calle = input("Calle: ")
    numero = input("Número: ")
    codigoPostal =input("Código postal: ")
    estado = input("Estado: ")
    pais = input("País: ")
    puesto = input("Puesto laboral: ")
    fechaRegistro = datetime.now().strftime('%Y-%m-%d')        
    cursor.execute('''
        INSERT INTO empleados (nombre, primer_apellido, segundo_apellido, telefono, extension, correo, celular, empresa, calle, numero, codigo_postal, estado, pais, puesto, fecha_registro)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nombre, primerApellido, segundoApellido, telefono, extension, correo, celular, empresa, calle, numero, codigoPostal, estado, pais, puesto, fechaRegistro))
    conx.commit()
    conx.close()
    print("\n Registro exitoso.\n")
