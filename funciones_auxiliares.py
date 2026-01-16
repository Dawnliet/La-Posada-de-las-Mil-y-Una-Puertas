
def while_range(num, *opciones):
    #Restringe las opciones para elegir
    while num not in opciones:
        print('Opcion no valida')
        num = input()
    return num
    
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
            
