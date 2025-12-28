class Operaciones:
    #Una clase para agrupar las distintas pantallas y sus respectivas operaciones
    
    def inicio():
        print('En este momento se encuentra en el gestor de eventos de La Posada de las Mil y Una Puertas')
    
    def modo():
        #Permite entrar en modo administrador o usuario
        print("Escriba un numero para elegir una opcion: ")
        print('\n(1) - Entrar en modo administrador')
        print('(2) - Entrar en modo usuario')
        print("\nModo: ")

        num = FuncionesAuxiliares.while_range(input(), '1', '2')
        if num == '1':
            print('\nHa entrado en modo administrador')
            return True
        print('\nHa entrado en modo usuario')
        return False
    
    def opciones_de_modo(bool_opcion):
        #Muestra las opciones correspondientes de cada modo
        
        print("Escriba un numero para elegir una opcion: ")
        print('\n(1) - Salir')
        print('(2) - Ver lista de eventos')
        print('(3) - Crear evento')
        print('(4) - Eliminar evento')
        
        if bool_opcion:
            print('(5) - Obtener recursos')
        
    

    
class FuncionesAuxiliares:
    # Un conjunto de funciones que validan operaciones
    
    def while_range(num, *opciones):
        #Restringe las opciones para elegir
        while num not in opciones:
            print('Opcion no valida')
            num = input()
        return num
            
class Recursos:           
    def __init__(self, nombre, tipo, cantidad):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        
    def variar_cantidad(self, bool_opcion, cantidad):
        #Aumenta o disminuye la cantidad de este recurso
        if bool_opcion:
            self.cantidad += cantidad
        else:
            self.cantidad -= cantidad
            
