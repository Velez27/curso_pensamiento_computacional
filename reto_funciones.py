def enumeracion_exhaustiva():
    objetivo = int(input('Escribe un entero: '))
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1
    
    if respuesta**2 == objetivo:
        return print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        return print(f'{objetivo} no tiene una raiz cuadrada exacta')


def aproximacion_soluciones():
    objetivo = int(input('Escribe un numero: '))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
    
    if abs(respuesta**2 - objetivo) >=  epsilon:
        return print(f'No se encontro la raiz cuadrada de {objetivo}')
    else:
        return print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def busqueda_binaria():
    objetivo = int(input('Escribe un numero: '))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2

    return print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def run():
    opcion = int(input("""Selecciona el algoritmo que deseas utilizar para calcular la raiz cuadrada de tu numero.
Escoge 1, 2 o 3 segun el algoritmo que desees:  
1.- Algoritmo Enumeracion Exhaustiva
2.- Algoritmo Aproximacion de Soluciones
3.- Algoritmo de Busqueda Binaria
4.- Salir
Opcion Elegida: """))

    if opcion ==  1:
        enumeracion_exhaustiva()
        print('')
        run()
    elif opcion == 2:
        aproximacion_soluciones()
        print('')
        run()
    elif opcion == 3:
        busqueda_binaria()
        print('')
        run()
    elif opcion == 4:
        exit()
    else:
        print("""
Error! - Selecciona una opcion valida.
""")
        run()


if __name__ == '__main__':
    run()