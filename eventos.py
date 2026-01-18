import json
from pathlib import Path

from recursos import seleccionar_recursos_principales
from funciones_auxiliares import seleccionar_fecha

def crear_evento(requisitos):
    
    if requisitos:
        nombre = input('Nombre: ')
        descripcion = input('Descripcion: ')
        persona = seleccionar_recursos_principales('persona')
        servicio = seleccionar_recursos_principales('servicio')
        objeto = seleccionar_recursos_principales('objeto')
        fecha = seleccionar_fecha()
        
        nuevo_evento = {fecha: {'nombre' : nombre, 'descripcion': descripcion, 'recurso (P)': persona, 
                            'recurso (S)': servicio, 'recurso (O)': objeto }}
        path = Path('eventos/eventos.json')
        ok = validar_evento()
        
        if ok:
            guardar_evento(path, nuevo_evento, fecha)
        else:
            print('No se ha guardado el evento')
        
    else:
        print('Actualmente no se pueden crear eventos por falta de recursos principales')

def requisitos_evento():
        path_persona = Path('recursos/persona.json')
        path_servicio = Path(f'recursos/servicio.json')
        path_objeto = Path(f'recursos/objeto.json')
        
        if not path_objeto.exists() or not path_persona.exists() or not path_servicio.exists():
            return False
        return True

def borrar_evento():
    pass

def ver_lista_eventos():
    pass

def guardar_evento(path, nuevo_evento, fecha):
    
    if path.exists():
        eventos = path.read_text()
        eventos = json.loads(eventos)
        eventos [fecha] = nuevo_evento[fecha]
        eventos = json.dumps(eventos)
        path.write_text(eventos)
    else:
        nuevo_evento = json.dumps(nuevo_evento)
        path.write_text(nuevo_evento)
        
def validar_evento():
    return True

