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

#sys.path.append("../verRegistros/")
#from verRegistros.verLlamadas import  verLlamadas


sys.path.append("../..")  # Agregar el directorio padre de 'verRegistros'
from registroLlamadas.verRegistros.verLlamadas import verLlamadas
#from registroLlamadas.verRegistros.verLlamadas import verLlamadas


def elimnarLlamada():
    conx = sqlite3.connect("log_llamadas.db")
    cursor = conx.cursor()
    verLlamadas()
    #cursor.execute("SELECT id, nombre, primer_apellido, segundo_apellido FROM llamadasTelefonicas")
    
    
    while True:
        idLlamada = input("Ingrese el ID de la llamada a elimnar: ")
        cursor.execute("SELECT id FROM llamadasTelefonicas WHERE id = ?", (idLlamada ,))
        if cursor.fetchone():
            break
        print("ID no válido. Intenta nuevamente.")

    cursor.execute("DELETE FROM llamadasTelefonicas WHERE id = ?", (idLlamada ,))
    conx.commit()
    conx.close()
    
    print(f"La llamada con ID {idLlamada} ha sido eliminada correctamente.")

    
def modLlamada():
    conx= sqlite3.connect("log_llamadas.db")
    cursor = conx.cursor()
    verLlamadas()
    #cursor.execute("SELECT id, nombre, primer_apellido, segundo_apellido FROM llamadasTelefonicass")
    
    while True:
        idLlamada = input("Ingrese el ID de la llamada a modificar: ")
        cursor.execute("SELECT id FROM llamadasTelefonicas WHERE id = ?", (idLlamada ,))
        if cursor.fetchone():
            break
        print("ID no válido. Intenta nuevamente.")
        
    fechaLlamada = input(f"Fecha de la llamada (YYYY-MM-DD) [Por defecto: {datetime.now().strftime('%Y-%m-%d')}]: ") or datetime.now().strftime('%Y-%m-%d')
    horaLlamada = input(f"Hora de la llamada (HH:MM) [Por defecto: {datetime.now().strftime('%H:%M')}]: ") or datetime.now().strftime('%H:%M')
    resumen = input("Resumen de la llamada: ")
    
    cursor.execute("""
        UPDATE llamadasTelefonicas 
        SET fecha_llamada = ?, hora_llamada = ?, resumen = ?
        WHERE id = ?
    """, (fechaLlamada, horaLlamada, resumen, idLlamada))
    conx.commit()
    conx.close()
    