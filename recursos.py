import json
from pathlib import Path

from core import FuncionesAuxiliares as fa

def crear_recurso():
    nombre = input('Nombre: ')
    tipo = input('Tipo: ')
    cantidad = fa.while_int(input('Cantidad: '))
    
    print('\nEscriba (1) para guardar el siguiente recurso o (2) para volver')
    print(f'Nombre: {nombre}\nTipo: {tipo}\nCantidad: {cantidad}')
    num = fa.while_range(input(), '1', '2')
    
    if num == '1':
        recurso = {'nombre': nombre, 'tipo' : tipo, 'cantidad' : cantidad }
        path_txt = Path('recursos/recursos.txt')
        path_json = Path(f'recursos/{nombre}.json')
        
        if path_txt.exists():
            temp = path_txt.read_text().split()
            temp += '' + nombre
            path_txt.write_text(temp)
            
            recurso = json.dumps(recurso)
            path_json.write_text(recurso)  
        else:
            path_txt.write_text(nombre)
            
            recurso = json.dumps(recurso)
            path_json.write_text(recurso)
    else:
        crear_recurso()
       

crear_recurso()