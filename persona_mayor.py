def run():
    nombre_persona1 = input('Escribe el nombre de la primer persona: ')
    edad_persona1 = int(input('Escribe la edad de la pimera persona: '))

    nombre_persona2 = input('Escribe el nombre de la segunda persona: ')
    edad_persona2 = int(input('Escribe la edad de la segunda persona: '))

    if edad_persona1 > edad_persona2:
        print(f'{nombre_persona1} tiene una edad mayor que {nombre_persona2}')
    elif edad_persona1 < edad_persona2:
        print(f'{nombre_persona2} tiene una edad mayor que {nombre_persona1}')
    else:
        print(f'{nombre_persona1} y {nombre_persona2} tienen la misma edad')

if __name__ == '__main__':
    run()