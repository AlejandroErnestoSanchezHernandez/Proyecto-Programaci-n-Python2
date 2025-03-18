#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 13:14:52 2025

@author: Alejandro Ernesto Sanchez Hernandez 

Este modulo tiene la función de crear una base de datos de sql 
para almacenar los registros de las llamadas de una empresa
"""

import sqlite3

def creaTabla():
    conx=sqlite3.connect("log_llamadas.db")
    cursor=conx.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empleados(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            primer_apellido TEXT NOT NULL,
            segundo_apellido TEXT NOT NULL,
            telefono TEXT NOT NULL,
            extension TEXT,
            correo TEXT,
            celular TEXT,
            empresa TEXT,
            calle TEXT,
            numero TEXT,
            codigo_postal TEXT,
            estado TEXT,
            pais TEXT,
            puesto TEXT,
            fecha_registro TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS llamadasTelefonicas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_persona INTEGER NOT NULL,
            fecha_llamada TEXT NOT NULL,
            hora_llamada TEXT NOT NULL,
            resumen TEXT NOT NULL,
            FOREIGN KEY (id_persona) REFERENCES empleados (id)
        )
    ''')
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = cursor.fetchall()

    #print("Tablas en la base de datos:")
    #for tabla in tablas:
    #    print(tabla[0])
    
    conx.commit()
    conx.close()
    
    