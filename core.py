
class Operaciones:
    #Una clase para agrupar las distintas pantallas y sus respectivas operaciones
    
    def modo():
        #Permite entrar en modo administrador o usuario
        print('En este momento se encuentra en el gestor de eventos de La Posada de las Mil y Una Puertas')
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
            num = FuncionesAuxiliares.while_range(input(), '1', '2', '3', '4', '5')
            return num
        
        num = FuncionesAuxiliares.while_range(input(), '1', '2', '3', '4')
        return num
        
    def elegir_opcion_modo(num):
        if num == '1':
            pass
        if num == '2':
            pass
        if num == '3':
            Operaciones.crear_evento()
        if num == '4':
            pass
        if num == '5':
            pass   
        
    def salir():
        print('Ha salido satisfactoriamente')
    
         
class FuncionesAuxiliares:
    # Un conjunto de funciones que validan operaciones
    
    def while_range(num, *opciones):
        #Restringe las opciones para elegir
        while num not in opciones:
            print('Opcion no valida')
            num = input()
        return num
    
    def while_int (num):
        while True:
            try:
                num = int(num)
            except:
                print('Escriba un numero')
                num = input()
            else:
                break
            
        return num
            
        
