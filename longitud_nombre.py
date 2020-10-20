def run():
    nombre = input('Escribe tu nombre: ')
    saludo = f'Hola, {nombre}'
    print(saludo)
    print(f'La longitud del saludo y tu nombre es: {len(saludo)}')


if __name__ == '__main__':
    run()