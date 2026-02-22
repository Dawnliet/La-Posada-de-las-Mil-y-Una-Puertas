# Gestor de Eventos de Posada

## Descripción del proyecto
Este proyecto implementa un **gestor de eventos** para una posada utilizando Python.  
Permite:
- Crear eventos con recursos asociados.
- Listar eventos existentes y recursos disponibles.
- Eliminar eventos para liberar recursos.
- Actualizar el inventario de recursos (solo en modo administrador).

La idea es simular la dinámica de una posada, donde los eventos ocurren en diferentes habitaciones y requieren distintos tipos de recursos.

---

## Recursos
Los recursos se almacenan como **diccionarios** dentro de una lista. Cada recurso contiene:
- **Nombre**: `str` definido por el usuario.
- **Tipo principal**: `persona`, `servicio` u `objeto`.
- **Subtipo**: `str` definido por el usuario, usado para evitar conflictos entre recursos de distintos tipos.
- **Cantidad**: `int`. Si es menor que 1, el recurso se elimina automáticamente.

### Notas importantes:
- Los recursos se guardan en archivos `.json`.
- Al crear un evento, siempre deben existir recursos que dependan de otros.
- Los recursos con cantidad menor a 1 se eliminan automáticamente durante la ejecución.

---

## Eventos
Los eventos también se representan como **diccionarios** y contienen:
- **Nombre**: `str` definido por el usuario.
- **Descripción**: `str`.
- **Fecha**: lista con dos elementos (`fecha inicial`, `fecha final`), validados con la librería `datetime`.
- **Recursos asociados**: tres diccionarios, cada uno correspondiente a un tipo principal distinto (`persona`, `servicio`, `objeto`).

Los eventos se almacenan en archivos `.json`.

---

## Funcionalidades principales
1. **Modo usuario**  
   - Crear eventos.
   - Eliminar eventos (liberando sus recursos)
   - Listar eventos.  
   - Listar recursos.
   - Salir 

2. **Modo administrador**  
   - Todas las funciones del modo usuario.  
   - Crear nuevos recursos.  

3. **Gestión automática**  
   - Eliminación de recursos con cantidad < 1.  
   - Eliminación de eventos cuya fecha final ya pasó (liberando sus recursos).  

4. **Eventos inteligentes**  
   - Buscan recursos en su ubicación habitual.  
   - Si no están disponibles, reutilizan recursos de otros eventos.  
   - La fecha inicial se ajusta automáticamente después del evento más antiguo del cual se obtuvieron recursos.

---

## Estructura del proyecto
El proyecto consta de **5 archivos de código**.  
La ejecución comienza en `main.py`, donde se selecciona el modo de operación (usuario o administrador).

---

## Requisitos
- Python 3.8 o superior.
- Librerías estándar: `os`, `datetime`, `json`.

---

## Ejecución
1. Clonar el repositorio.  
2. Abrir el proyecto en un editor de código.  
3. Ejecutar:

```bash
python main.py
