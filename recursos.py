import json
from pathlib import Path

import core

def crear_recurso():
    nombre = input('Nombre: ')
    tipo = input('Tipo: ')
    cantidad = core.FuncionesAuxiliares.while_int(input('Cantidad: '))
    
    print('\nEscriba (1) para guardar el siguiente recurso o (2) para volver')
    print(f'Nombre: {nombre}\nTipo: {tipo}\nCantidad: {cantidad}')
    num = core.FuncionesAuxiliares.while_range(input(), '1', '2')
    
    if num == '1':
        recurso = {'nombre': nombre, 'tipo' : tipo, 'cantidad' : cantidad }
        path_txt = Path('recursos/recursos.txt')
        path_json = Path(f'recursos/{nombre}.json')
        
        if path_txt.exists():
            temp = path_txt.read_text()
            temp += ' ' + nombre
            path_txt.write_text(temp)
            
            recurso = json.dumps(recurso)
            path_json.write_text(recurso)  
        else:
            path_txt.write_text(nombre)
            
            recurso = json.dumps(recurso)
            path_json.write_text(recurso)
    else:
        crear_recurso()
       
def listar_recursos():
    #Muestra en pantalla todos los recursos disponibles
    path_txt = Path('recursos/recursos.txt')
    
    if path_txt.exists():
        nombres_recursos = path_txt.read_text().split()
        print('\nLista De Recursos: ')
        for nombre_recurso in nombres_recursos:
            path_json = Path(f'recursos/{nombre_recurso}.json')
            temp = path_json.read_text()
            temp = json.loads(temp)
            
            print(f'\nNombre: {temp['nombre']}')
            print(f'Tipo: {temp['tipo']}')
            print(f'Cantidad: {temp['cantidad']}')
    else:
        print("No se han encontrado recursos")

def seleccionar_recursos():
    pass


    