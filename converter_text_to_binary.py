def run():
    text = input('Escribe el texto que deseas convertir a binario: ')

    def translate_to_binary(text):
        potency = [128, 64, 32, 16, 8, 4, 2, 1]
        ascii_code_array = []
        binary_result_array = []
        for caracter in text:
            ascii_code_array.append(ord(caracter))
        
        for codigo in ascii_code_array:
            comparador = codigo
            for i in potency:
                if comparador >= i:
                    binary_result_array.append('1')
                    comparador = comparador - i
                else:
                    binary_result_array.append('0')
            binary_result_array.append(' ')
        return print(f'Tu texto convertido a binario es: ' + ''.join(binary_result_array))

    translate_to_binary(text)

if __name__ == '__main__':
    run()