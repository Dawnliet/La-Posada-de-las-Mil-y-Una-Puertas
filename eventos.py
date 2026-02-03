import json
import datetime
from pathlib import Path

from recursos import seleccionar_recursos_principales
from recursos import aumentar_recurso
from funciones_auxiliares import seleccionar_fecha
from funciones_auxiliares import console_clear
from funciones_auxiliares import while_opciones

def crear_evento(requisitos):
    
    if requisitos:
        fecha = seleccionar_fecha()
        nombre = input('Nombre del evento: ')
        descripcion = input('Descripcion: ')
        console_clear()
        persona = seleccionar_recursos_principales('persona')
        console_clear()
        servicio = seleccionar_recursos_principales('servicio')
        console_clear()
        objeto = seleccionar_recursos_principales('objeto')
        console_clear()
        
        nuevo_evento = {nombre: {'descripcion': descripcion, 'fecha': fecha,  'recurso (P)': persona, 
                            'recurso (S)': servicio, 'recurso (O)': objeto }}
        del nuevo_evento[nombre]['recurso (P)']['cantidad']
        del nuevo_evento[nombre]['recurso (S)']['cantidad']
        del nuevo_evento[nombre]['recurso (O)']['cantidad']
        
        tipos = [nuevo_evento[nombre]['recurso (P)']['subtipo'], nuevo_evento[nombre]['recurso (S)']['subtipo'], 
                      nuevo_evento[nombre]['recurso (O)']['subtipo']]
        
        mismo_tipo = tipos[0]
        for tipo in tipos:
            if mismo_tipo != tipo:
                print('Los recursos principales del evento no son del mismo tipo')
                return None
        
        path = Path('eventos/eventos.json')
        ok = confirmar_evento(nuevo_evento)
        
        if ok:
            guardar_evento(path, nuevo_evento, nombre)
        else:
            print('No se ha guardado el evento')
            aumentar_recurso(nuevo_evento['recurso (P)'])
            aumentar_recurso(nuevo_evento['recurso (S)'])
            aumentar_recurso(nuevo_evento['recurso (O)'])
        
    else:
        print('Actualmente no se pueden crear eventos por falta de recursos principales')

def requisitos_evento():
        path_persona = Path('recursos/persona.json')
        path_servicio = Path(f'recursos/servicio.json')
        path_objeto = Path(f'recursos/objeto.json')
        
        if not path_objeto.exists() or not path_persona.exists() or not path_servicio.exists():
            return False
        return True

def borrar_evento(nombre=None):
    #Elimina un evento y permite utilizar sus recursos
    path = Path('eventos/eventos.json')
    
    if not nombre:
        print('Escriba el nombre del evento que desea eliminar')
        nombre = input('Nombre: ')  
        
    if path.exists():
        eventos = path.read_text()
        eventos = json.loads(eventos)
        
        try:
            eventos[nombre]
        except:
            print('No existe evento con ese nombre')
        else:
            aumentar_recurso(eventos[nombre]['recurso (P)'])
            aumentar_recurso(eventos[nombre]['recurso (S)'])
            aumentar_recurso(eventos[nombre]['recurso (O)'])
        
            eventos.pop(nombre, None)
            eventos = json.dumps(eventos)
            path.write_text(eventos)
    else:
        print('No hay eventos para eliminar')

def ver_lista_eventos():
    
    path = Path('eventos/eventos.json')
    if path.exists():
        
        eventos = path.read_text()
        eventos = json.loads(eventos)

        for fecha, evento in eventos.items():
            print(f'\nFecha: {fecha}')
            print(f'Nombre del evento: {evento['nombre']}')
            print(f'Descripcion: {evento['descripcion']}')
            print(f'Tipo: {evento['recurso (P)']['subtipo']}')
            print('Recursos: ')
            print(f'Persona: {evento['recurso (P)']['nombre']}')
            print(f'Servicio: {evento['recurso (S)']['nombre']}')
            print(f'Objeto: {evento['recurso (O)']['nombre']}')
    else:
        print('Actualmente no hay eventos ')

def guardar_evento(path, nuevo_evento, nombre):
    
    if path.exists():
        eventos = path.read_text()
        eventos = json.loads(eventos)
        eventos [nombre] = nuevo_evento[nombre]
        eventos = json.dumps(eventos)
        path.write_text(eventos)
    else:
        nuevo_evento = json.dumps(nuevo_evento)
        path.write_text(nuevo_evento)
        
def confirmar_evento(eventos):
    print('\nPresione (1) para guardar este evento o (2) para cancelar')
    for nombre,evento in eventos.items():
        
        print(f'\nFecha: {evento['fecha']}')
        print(f'Nombre del evento: {nombre}')
        print(f'Descripcion: {evento['descripcion']}')
        print(f'Tipo: {evento['recurso (P)']['subtipo']}')
        print('Recursos: ')
        print(f'Persona: {evento['recurso (P)']['nombre']}')
        print(f'Servicio: {evento['recurso (S)']['nombre']}')
        print(f'Objeto: {evento['recurso (O)']['nombre']}')
    
    num = while_opciones(input(), '1', '2')
    if num == '1':
        return True
    return False

def validar_eventos():
    path = Path('eventos/eventos.json')
    eventos = path.read_text()
    eventos = json.loads(eventos)
    nombres = []
    
    for nombre, evento in eventos.items():
        fecha = datetime.date.fromisoformat (evento['fecha'][1])
        if fecha < datetime.date.today():
            nombres.append(nombre)
            
    for nombre in nombres[::-1]:
        borrar_evento(nombre)