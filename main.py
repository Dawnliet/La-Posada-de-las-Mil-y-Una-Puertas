import core as op
    
op.pantalla_seleccion_modo()
modo = op.seleccionar_modo()
end = False

while not end:
    op.pantalla_opciones_de_modo(modo)
    opcion = op.opciones_validas(modo)
    op.elegir_opcion_modo(opcion)
    
    end = op.preguntar_para_cerrar()

op.salir()
