import funciones_auxiliares
from recursos import crear_recurso
from recursos import listar_recursos
from eventos import crear_evento
from eventos import requisitos_evento
from eventos import ver_lista_eventos
from eventos import borrar_evento


def pantalla_seleccion_modo():
    #Muestra los modos disponibles para acceder
    print('En este momento se encuentra en el gestor de eventos de La Posada de las Mil y Una Puertas')
    print("Escriba un numero para elegir una opcion: ")
    print('\n(1) - Entrar en modo administrador')
    print('(2) - Entrar en modo usuario')

def seleccionar_modo():
    #Permite entrar en modo administrador o usuario
    print("\nModo: ")
    num = funciones_auxiliares.while_opciones(input(), '1', '2')
    
    if num == '1':
        print('\nHa entrado en modo administrador')
        return True
    print('\nHa entrado en modo usuario')
    return False
    
def pantalla_opciones_de_modo(admin):
    #Muestra las opciones correspondientes de cada modo
    msg_0 = '(0) - Salir'
    msg_1 = '(1) - Crear evento'
    msg_2 = '(2) - Ver lista de recursos'
    msg_3 = '(3) - Ver lista de eventos'
    msg_4 = '(4) - Eliminar evento'
    msg_5 = '(5) - Obtener recurso'
    print(msg_0 + '\n' + msg_1 + '\n' + msg_2 + '\n' + msg_3 + '\n' + msg_4 )
    
    if admin:
        print(msg_5)    
    
def opciones_validas(admin):
    
    if admin:
        num = funciones_auxiliares.while_opciones(input('\nOpcion: '), '0', '1', '2', '3', '4', '5')
        return num
    else:
        num = funciones_auxiliares.while_opciones(input('\nOpcion: '), '0', '1', '2', '3', '4')
        return num
    
def elegir_opcion_modo(num):
    if num == '0':
        print('Confirme su respuesta')
    if num == '1':
        requisitos = requisitos_evento()
        crear_evento(requisitos)
    if num == '2':
        listar_recursos()
    if num == '3':
        ver_lista_eventos()
    if num == '4':
        borrar_evento()
    if num == '5':
              crear_recurso()
        
def salir():
    print('Ha salido satisfactoriamente')

def preguntar_para_cerrar():
    print('\nPara salir presione (1), para seguir presione (2)')
    opcion = funciones_auxiliares.while_opciones(input(), '1', '2')
    
    if opcion == '1':
        return True
    return False
