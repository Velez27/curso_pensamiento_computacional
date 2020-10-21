def run():
    def fibonacci(n):
        if n == 0 or n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci( n - 2)

    numero = int(input('Escribe un numero: '))

    print(fibonacci(numero))

if __name__ == '__main__':
    run()