def inicio():
    print('En este momento se encuentra en el gestor de eventos de La Posada de las Mil y Una Puertas')
    
def modo():
    print("Elija una opcion: ")
    print('\n(1) - Entrar en modo administrador')
    print('(cualquier numero) - Entrar en modo usuario')
    print("\nModo: ")
    
    num = FuncionesAuxiliares.while_valor(1)
    if num == 1:
        return True
    return False
    

    
class FuncionesAuxiliares:
    # Un conjunto de funciones que validan operaciones
    
    def while_valor(ejemplo):
        #Permite que el usuario coloque un tipo de dato especifico
        
        valor = input()
        try:
            valor = int(valor)
        except:
            pass
        
        while type(valor) != type(ejemplo):
            print('Valor incorrecto')
            valor = input()
            try:
                valor = int(valor)
            except:
                pass
        
        return valor
            
            