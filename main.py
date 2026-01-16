from core import Operaciones as op

op.pantalla_seleccion_modo()
modo = op.seleccionar_modo()

op.pantalla_opciones_de_modo(modo)
opcion = op.opciones_validas(modo)
op.elegir_opcion_modo(opcion)

