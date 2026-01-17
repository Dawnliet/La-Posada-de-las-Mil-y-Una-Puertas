import json
from pathlib import Path

import funciones_auxiliares

def crear_recurso():
    nombre = input('Nombre: ')
    tipo_principal = seleccionar_tipo_principal()
    subtipo = input('Subtipo: ').lower()
    cantidad = funciones_auxiliares.while_int(input('Cantidad: '))
    
    print('\nEscriba (1) para guardar el siguiente recurso o (2) para volver')
    print(f'Nombre: {nombre}\nTipo principal: {tipo_principal}\nSubtipo: {subtipo}\nCantidad: {cantidad}')
    num = funciones_auxiliares.while_opciones(input(), '1', '2')
    
    if num == '1':
        recurso = {'nombre': nombre, 'tipo principal' : tipo_principal, 'subtipo' : subtipo, 'cantidad' : cantidad }
        path_recurso = Path(f'recursos/{tipo_principal}.json')
        
        if path_recurso.exists():
            recursos = path_recurso.read_text()
            recursos = json.loads(recursos)
            recursos.append(recurso)
            recursos = json.dumps(recursos)
            
            path_recurso.write_text(recursos)
            
        else:
            temp_list = []
            temp_list.append(recurso)
            temp_list = json.dumps(temp_list)
            path_recurso.write_text(temp_list)
            
    else:
        crear_recurso()
       
def seleccionar_tipo_principal():
    print('Seleccionar el tipo principal de este recurso:')
    print('(1) - Persona \n(2) - Servicio \n(3) - Objeto')
    temp = funciones_auxiliares.while_opciones(input(), '1', '2', '3')
    
    if temp == '1':
        return 'persona'
    elif temp == '2':
        return 'servicio'
    else :
        return 'objeto'
    
def seleccionar_recursos_principales(nombre):
    path = Path(f'recursos/{nombre}.json')
    recursos = path.read_text()
    recursos = json.loads(recursos)
    count = 0
    
    print('Seleccionar recurso: ')
    print('')
    
    for recurso in recursos:
        print(f'({count}) - {recurso['nombre']} ({recurso['subtipo']})')
        count += 1
    
    num = funciones_auxiliares.while_int(input())
    num = funciones_auxiliares.while_range_int(num, 0, count)
    output_recurso = recursos[num]
    
    return output_recurso

def seleccionar_recurso_servicio():
    path = Path('recursos/servicio.json')
    servicios = path.read_text()
    servicios = servicios.splitlines()
    count = 0
    
    print('Seleccionar recurso: ')
    print('')
    
    for servicio in servicios:
        servicio = json.loads(servicio)
        print(f'({count}) - {servicio['nombre']} ({servicio['subtipo']})')
        count += 1
    
    num = funciones_auxiliares.while_int(int(input()), 0, count)
    recurso = servicios[num]
    recurso = json.loads(recurso)
    
    return recurso

def seleccionar_recurso_objeto():
    path = Path('recursos/objeto.json')
    objetos = path.read_text()
    objetos = objetos.split()
    count = 0
    recursos = set()
    
    print('Seleccionar recursos: ')
    print('')
    
    for objeto in objetos:
        print(f'({count}) - {objeto['nombre']} ({objeto['subtipo']})')
        count += 1
        
    while True:
        num = funciones_auxiliares.while_int(int(input()), 0, count)
        recursos.add(objetos[int(num)])
        end = input('Para agregar otro objeto presiona q')
        if end != 'q':
            break
    recurso = json.loads(recurso)
    
    return recursos
       
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

