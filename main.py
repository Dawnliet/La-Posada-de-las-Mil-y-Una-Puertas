import json
from pathlib import Path

from core import Operaciones as op
from core import FuncionesAuxiliares as fa

op.pantalla_seleccion_modo()
modo = op.seleccionar_modo()

op.pantalla_opciones_de_modo(modo)
opcion = op.opciones_validas(modo)

