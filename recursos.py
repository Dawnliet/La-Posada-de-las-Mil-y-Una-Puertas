import json
from pathlib import Path

import funciones_auxiliares

def crear_recurso():
    nombre = input('Nombre: ')
    funciones_auxiliares.console_clear()
    tipo_principal = seleccionar_tipo_principal()
    funciones_auxiliares.console_clear()
    subtipo = input('Subtipo: ').lower()
    funciones_auxiliares.console_clear()
    cantidad = funciones_auxiliares.while_int(input('Cantidad: '), 1)
    funciones_auxiliares.console_clear()
    planificado = False
    
    print('\nEscriba (1) para guardar el siguiente recurso o (2) para empezar nuevamente')
    print(f'Nombre: {nombre}\nTipo principal: {tipo_principal}\nSubtipo: {subtipo}\nCantidad: {cantidad}')
    num = funciones_auxiliares.while_opciones(input(), '1', '2')
    
    if num == '1':
        recurso = {'nombre': nombre, 'tipo principal': tipo_principal, 'subtipo': subtipo, 'cantidad': cantidad}
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
    
    num = funciones_auxiliares.while_int(input(), 0, count-1)
    output_recurso = recursos[num]
    del output_recurso['cantidad']
    
    return output_recurso
       
def listar_recursos():
    #Muestra en pantalla todos los recursos disponibles
    tipos_principales = ['persona', 'servicio', 'objeto']
    
    for tipo in tipos_principales:
        path = Path(f'recursos/{tipo}.json')
        
        if not path.exists():
            print(f'No existen recursos del tipo principal: {tipo}')
    
    for tipo in tipos_principales:
        path = Path(f'recursos/{tipo}.json')

        if path.exists():
            lista_recurso = path.read_text()
            lista_recurso = json.loads(lista_recurso)
            
            for recurso in lista_recurso:
                print(f'\nNombre: {recurso['nombre']}')
                print(f'Tipo principal: {recurso['tipo principal']}')
                print (f'Subtipo: {recurso['subtipo']}')
                print(f'Cantidad: {recurso['cantidad']}')

def validar_recursos():
    recursos_validos = ['persona', 'servicio', 'objeto']
    for recurso_valido in recursos_validos:
        path = Path(f"recursos/{recurso_valido}.json")
        if path.exists():
            recursos = path.read_text()
            recursos = json.loads(recursos)
            
            fin = len(recursos) - 1
            inicio = -1
            
            for posicion in range(fin, inicio, -1):
                recurso = recursos[posicion]
                if recurso['cantidad'] < 1:
                    recursos.pop(posicion)
            
            if recursos == []:
                path.unlink()
            else:
                recursos = json.dumps(recursos)
                path.write_text(recursos)

def sumar_restar_recurso(recurso, operacion): 
    #Aumenta o disminuye un recurso dependiendo del valor de operacion
    tipo = recurso['tipo principal']
    path = Path(f'recursos/{tipo}.json')     
    
    if operacion == 'mas':
        encontrado = False
        if path.exists():
            recursos = path.read_text()
            recursos = json.loads(recursos)

            for posicion,elemento in enumerate(recursos):
                if elemento['nombre'] == recurso['nombre']:
                    recursos[posicion]['cantidad'] += 1
                    encontrado = True
                    break
                
            if not encontrado:
                recurso['cantidad'] = 1
                recursos.append(recurso)
            
            recursos = json.dumps(recursos)
            path.write_text(recursos)
            
        else:
            recurso['cantidad'] = 1
            recurso = [recurso]
            recurso = json.dumps(recurso)
            path.write_text(recurso)    
                 
    elif operacion == 'menos':
        if path.exists():
            recursos = path.read_text()
            recursos = json.loads(recursos)

            for posicion, elemento in enumerate(recursos):
                    if elemento['nombre'] == recurso['nombre']:
                        recursos[posicion]['cantidad'] -= 1
                        encontrado = True
                        break
                    
            recursos = json.dumps(recursos)
            path.write_text(recursos)
        
def buscar_recurso_principal(tipo, tipo_evento):
    #Revisa los .json para sacar cada recurso. De no existir dicho recurso revisa en los eventos creados; y de lo contrario devuelve un 
    #mensaje donde explica que dicho recurso no existe
    path_recursos = Path (f'recursos/{tipo}.json')
    path_eventos = Path('eventos/eventos.json')
    
    print(f'Escriba el nombre para el recurso principal de tipo {tipo}')
    nombre = input(f'{tipo}: ')
    
    if path_recursos.exists():
        recursos = path_recursos.read_text()
        recursos = json.loads(recursos)

        for recurso in recursos:
            if recurso['nombre'] == nombre:
                return recurso
        
    if path_eventos.exists():
        eventos = path_eventos.read_text()
        eventos = json.loads(eventos)
        
        for nombres, evento in eventos.items():
            if evento[f'{tipo_evento}']['nombre'] == nombre:
                recurso = evento[f'{tipo_evento}']
                fecha_final = evento['fecha'][1]
                return (recurso, fecha_final)
    
    return False

def recursos_validos(lista_de_recursos):
    for posicion, elemento in enumerate(lista_de_recursos):
        if type(elemento) == tuple:
            lista_de_recursos[posicion] = elemento[0]
    
    return tuple(lista_de_recursos)

