

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
    
    def mostrar_recursos():
        pass