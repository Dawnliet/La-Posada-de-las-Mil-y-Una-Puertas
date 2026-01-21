import json
from pathlib import Path

from recursos import seleccionar_recursos_principales
from funciones_auxiliares import seleccionar_fecha
from funciones_auxiliares import console_clear
from funciones_auxiliares import while_opciones

def crear_evento(requisitos):
    
    if requisitos:
        fecha = str(seleccionar_fecha())
        nombre = input('Nombre del evento: ')
        descripcion = input('Descripcion: ')
        console_clear()
        persona = seleccionar_recursos_principales('persona')
        console_clear()
        servicio = seleccionar_recursos_principales('servicio')
        console_clear()
        objeto = seleccionar_recursos_principales('objeto')
        console_clear()
        
        nuevo_evento = {fecha: {'nombre' : nombre, 'descripcion': descripcion, 'recurso (P)': persona, 
                            'recurso (S)': servicio, 'recurso (O)': objeto }}
        path = Path('eventos/eventos.json')
        ok = confirmar_evento(nuevo_evento)
        
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
    print('Escriba la fecha del evento que desea eliminar')
    fecha = seleccionar_fecha()
    path = Path('eventos/eventos.json')
    
    if path.exists():
        evento = path.read_text()
        evento = json.loads(evento)
        evento.pop(fecha, None)
        evento = json.dumps(evento)
        path.write_text(evento)
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
            print(f'Persona: {evento['recurso (P)']['nombre']}, ({evento['recurso (P)']['cantidad']})')
            print(f'Servicio: {evento['recurso (S)']['nombre']}, ({evento['recurso (S)']['cantidad']})')
            print(f'Objeto: {evento['recurso (O)']['nombre']}, ({evento['recurso (O)']['cantidad']})')
    else:
        print('Actualmente no hay eventos ')

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
        
def confirmar_evento(eventos):
    print('\nPresione (1) para guardar este evento o (2) para cancelar')
    for fecha,evento in eventos.items():
        
        print(f'\nFecha: {fecha}')
        print(f'Nombre del evento: {evento['nombre']}')
        print(f'Descripcion: {evento['descripcion']}')
        print(f'Tipo: {evento['recurso (P)']['subtipo']}')
        print('Recursos: ')
        print(f'Persona: {evento['recurso (P)']['nombre']}, ({evento['recurso (P)']['cantidad']})')
        print(f'Servicio: {evento['recurso (S)']['nombre']}, ({evento['recurso (S)']['cantidad']})')
        print(f'Objeto: {evento['recurso (O)']['nombre']}, ({evento['recurso (O)']['cantidad']})')
    
    num = while_opciones(input(), '1', '2')
    if num == '1':
        return True
    return False
