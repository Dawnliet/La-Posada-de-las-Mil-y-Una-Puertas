from core import Operaciones as op

while True:
    
    op.pantalla_seleccion_modo()
    modo = op.seleccionar_modo()

    op.pantalla_opciones_de_modo(modo)
    opcion = op.opciones_validas(modo)
    op.elegir_opcion_modo(opcion)
    
    end = input()
    if end == 'q':
        break
