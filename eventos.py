import json
from pathlib import Path

from recursos import seleccionar_recursos_principales

def crear_evento(bool_opcion):
    
    if bool_opcion:
        nombre = input('Nombre: ')
        descripcion = input('Descripcion: ')
        persona = seleccionar_recursos_principales('persona')
        servicio = seleccionar_recursos_principales('servicio')
        objetos = seleccionar_recursos_principales('objeto')
        fecha = str( ('r', 'm', 'a') )
        
        nuevo_evento = {fecha: {'nombre' : nombre, 'descripcion': descripcion, 'recurso (P)': persona, 
                            'recurso (S)': servicio, 'recurso (O)': objetos }}
        path = Path('eventos/eventos.json')
        
        if path.exists():
            eventos = path.read_text()
            eventos = json.loads(eventos)
            eventos [fecha] = nuevo_evento[fecha]
            eventos = json.dumps(eventos)
            path.write_text(eventos)
        else:
            nuevo_evento = json.dumps(nuevo_evento)
            path.write_text(nuevo_evento)
    else:
        print('Actualmente no se pueden crear eventos por falta de recursos principales')

def validar_evento():
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
