import core 
from funciones_auxiliares import console_clear
from recursos import validar_recursos

validar_recursos()
core.pantalla_seleccion_modo()
modo = core.seleccionar_modo()
end = False

while not end:
    validar_recursos()
    console_clear()
    core.pantalla_opciones_de_modo(modo)
    opcion = core.opciones_validas(modo)
    console_clear()
    core.elegir_opcion_modo(opcion)
    
    end = core.preguntar_para_cerrar()

core.salir()

