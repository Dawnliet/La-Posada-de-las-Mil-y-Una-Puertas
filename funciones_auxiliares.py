import datetime
import os
import json
from pathlib import Path

def while_opciones(element, *opciones):
    #Restringe las opciones para elegir
    while element not in opciones:
        print('Opcion no valida')
        element = input()
    return element
    
def while_int (num):
    #Obliga al usuario a escribir un int
    while True:
        try:
            num = int(num)
        except:
            print('Escriba un numero')
            num = input()
        else:
            break
            
    return num

def while_range_int(num, inicio, fin):
    #Restringe las opciones a un rango numerico
    while num < inicio or num > fin:
        print('Opcion no valida')
        num = input()
        num = while_int(num)
    return num       

def seleccionar_fecha():
    
    ok = preguntar_fecha_automatica()
    if ok:
        fecha = fecha_automatica()
        return fecha
        
    path = Path('eventos/eventos.json')
    end = False
    
    while not end:
        print('\nSeleccionar la fecha')
        day = while_int(input('Dia: '))
        month = while_int(input('Mes: '))
        year = while_int(input('Año: '))
        
        try:
            fecha = datetime.date(year, month, day)
        except:
            print('Esta fecha no existe en el calendario')
        else:
            end = fecha_unica(fecha, path)
    
    return fecha
           
def fecha_automatica():
    path = Path('eventos/eventos.json')
    
    if not path.exists():
        hoy = datetime.date.today()
        print(f'Fecha seleccionada: {hoy}')
        return hoy
    else:
        eventos = path.read_text()
        eventos = json.loads(eventos)
        set_eventos = set(eventos.keys())
        fecha = datetime.date.today()
        
        while fecha in set_eventos:
            fecha += datetime.timedelta(days=1)
            
        print(f'Fecha seleccionada: {fecha}')    
        return fecha   
            
def fecha_unica(fecha, path):
    
    if path.exists():
        eventos = path.read_text()
        eventos = json.loads(eventos)
         
        for fechas in eventos.keys():
            if fecha == fechas:
                print("Esta fecha ya esta ocupada")
                return False
        return True
    
    else:
        return True
         
def preguntar_fecha_automatica():
    
    print('\n Escriba (1) para seleccionar la fecha de manera automática. (2) Para seguir')
    num = while_opciones(input(), '1', '2')
    if num == '1':
        return True
    return False
         
def console_clear():
    os.system('cls')       

