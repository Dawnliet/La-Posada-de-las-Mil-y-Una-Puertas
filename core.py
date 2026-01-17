from recursos import crear_recurso
import funciones_auxiliares
from eventos import crear_evento
from eventos import validar_evento

class Operaciones:
    #Una clase para agrupar las distintas pantallas y sus respectivas operaciones
    
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
    
    def pantalla_opciones_de_modo(bool_opcion):
        #Muestra las opciones correspondientes de cada modo
        
        print("Escriba un numero para elegir una opcion: ")
        print('\n(1) - Salir')
        print('(2) - Ver lista de eventos')
        print('(3) - Crear evento')
        print('(4) - Eliminar evento')
        if bool_opcion:
            print('(5) - Obtener recursos')
        
    def opciones_validas(bool_opcion):
        
        if bool_opcion:
            num = funciones_auxiliares.while_opciones(input('\nOpcion: '), '1', '2', '3', '4', '5')
            return num
        else:
            num = funciones_auxiliares.while_opciones(input('\nOpcion: '), '1', '2', '3', '4')
            return num
        
    def elegir_opcion_modo(num):
        if num == '1':
            Operaciones.salir()
        if num == '2':
            pass
        if num == '3':
            crear_evento(validar_evento())
        if num == '4':
            pass
        if num == '5':
              crear_recurso()
        
    def salir():
        print('Ha salido satisfactoriamente')
      

