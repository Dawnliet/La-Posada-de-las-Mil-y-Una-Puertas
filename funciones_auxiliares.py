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
    
def while_int (num, inicio=None, fin=None):
    #Obliga al usuario a escribir un int
    while True:
        try:
            num = int(num)
        except:
            print('Escriba un numero')
            num = input()
        else:
            break
    
    if type(inicio) == int:
        while num < inicio:
            console_clear()
            print('Valor incorrecto')
            num = while_int(input('\nEscriba un nuevo numero: '), inicio)
            
    if type(fin) == int:
        while num > fin:
            console_clear()
            print('Valor incorrecto')
            num = while_int(input('\nEscriba un nuevo numero: '), inicio)
    
    return num

def while_range_int(num, inicio, fin):
    #Restringe las opciones a un rango numerico
    while num < inicio or num > fin:
        print('Opcion no valida')
        num = input()
        num = while_int(num)
    return num       

def seleccionar_fecha():
    #Devuelve una tupla con la fecha inicial y la final
    print('Fecha inicial')
    inicial = validar_fecha(datetime.date.today())
    console_clear()
    
    print('Fecha final: ')
    final = validar_fecha(inicial)
    return(str(inicial), str(final))
           
def validar_fecha(hoy=None):
    #Funciona hasta que se escriba una fecha correcta
    while True:
        day = while_int(input('Dia: '))
        month = while_int(input('Mes: '))
        year = while_int(input('Año: '))
        try:
            fecha = datetime.date(year, month, day)
        except:
            print('Esta fecha no existe en el calendario. Pruebe otra vez')
        else:
            break
    
    if (hoy) and (fecha < hoy):
        print('Ha habido un error. Recuerde que la fecha de inicio no puede ser antes de hoy, y la final debe ser luego de la de inicio') 
        fecha = validar_fecha(hoy)   
        
    return fecha

         
def preguntar_fecha_automatica():
    
    print('\n Escriba (1) para seleccionar la fecha de manera automática. (2) Para seguir')
    num = while_opciones(input(), '1', '2')
    if num == '1':
        return True
    return False
         
def console_clear():
    os.system('cls')       

