import datetime
import os

def while_opciones(element, *opciones):
    #Restringe las opciones para elegir
    while element not in opciones:
        print('Opcion no valida')
        element = input()
    return element
    
def while_int (num, inicio=None, fin=None):
    #Obliga al usuario a escribir un int. Dicho int debe ser mayor a inicio y/o menor a fin en caso de que se especifiquen
    while True:
        try:
            num = int(num)
        except:
            print('Escriba un numero')
            num = input()
        else:
            break
    
    if type(inicio) == int:
        while num < inicio:
            console_clear()
            print('Valor incorrecto')
            num = while_int(input('\nEscriba un nuevo numero: '), inicio)
            
    if type(fin) == int:
        while num > fin:
            console_clear()
            print('Valor incorrecto')
            num = while_int(input('\nEscriba un nuevo numero: '), inicio)
    
    return num
     
def seleccionar_fecha():
    #Devuelve una tupla con la fecha inicial y la final, ambas en formato str
    print('Fecha inicial')
    inicial = validar_fecha(datetime.date.today())
    console_clear()
    
    print('Fecha final: ')
    final = validar_fecha(inicial)
    return(str(inicial), str(final))
           
def validar_fecha(hoy=None):
    #Funciona hasta que se escriba una fecha correcta y luego la devuelve
    while True:
        day = while_int(input('Dia: '), 1, 31)
        month = while_int(input('Mes: '), 1, 12)
        year = while_int(input('Año: '))
        try:
            fecha = datetime.date(year, month, day)
        except:
            print('Esta fecha no existe en el calendario. Pruebe otra vez')
        else:
            break
    
    if (hoy) and (fecha < hoy):
        print('Ha habido un error. Recuerde que la fecha de inicio no puede ser antes de hoy, y la final debe ser luego de la de inicio') 
        fecha = validar_fecha(hoy)   
        
    return fecha
         
def console_clear():
    os.system('cls')       
  
def no_encontrado(recurso):
    if not recurso:
        return True

def fecha_inteligente(*recursos):
    fechas = []
    output_fecha = 0
    
    for recurso in recursos:
        if type(recurso) == tuple:
            fechas.append(datetime.date.fromisoformat(recurso[1]))
            
    try:
        output_fecha = max(fechas)
    except:
        fecha_inicial = datetime.date.today()
        print('Fecha final:')
        fecha_final = validar_fecha(fecha_inicial)
        return (str(fecha_inicial), str(fecha_final))
    else:
        fecha_inicial = output_fecha + datetime.timedelta(days=1)
        print('Fecha final:')
        fecha_final = validar_fecha(fecha_inicial)
        return (str(fecha_inicial), str(fecha_final))
            
