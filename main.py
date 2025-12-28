import json
from pathlib import Path

from core import Operaciones as op
from core import FuncionesAuxiliares as fa

bool_key = op.modo()
opcion = op.opciones_de_modo(bool_key)
op.elegir_opcion_modo(opcion)