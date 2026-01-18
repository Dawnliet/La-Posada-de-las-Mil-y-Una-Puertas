import datetime

def while_opciones(element, *opciones):
    #Restringe las opciones para elegir
    while element not in opciones:
        print('Opcion no valida')
        element = input()
    return element
    
def while_int (num):
    #Obliga al usuario a escribir un int
    while True:
        try:
            num = int(num)
        except:
            print('Escriba un numero')
            num = input()
        else:
            break
            
    return num

def while_range_int(num, inicio, fin):
    #Restringe las opciones a un rango numerico
    while num < inicio or num > fin:
        print('Opcion no valida')
        num = input()
        num = while_int(num)
    return num       

def seleccionar_fecha():
    
    while True:
        print('\nSeleccionar la fecha')
        day = while_int(input('Dia: '))
        month = while_int(input('Mes: '))
        year = while_int(input('Año: '))
        
        try:
            fecha = datetime.date(year, month, day)
        except:
            print('Esta fecha no existe en el calendario')
        else:
            return str(fecha)
        