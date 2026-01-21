import core as op
from funciones_auxiliares import console_clear

op.pantalla_seleccion_modo()
modo = op.seleccionar_modo()
end = False

while not end:
    console_clear()
    op.pantalla_opciones_de_modo(modo)
    opcion = op.opciones_validas(modo)
    console_clear()
    op.elegir_opcion_modo(opcion)
    
    end = op.preguntar_para_cerrar()

op.salir()

