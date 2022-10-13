print('-------------------------')
print('Olá, seja bem vindo à nossa calculadora!')

print('Escolha uma operação para continuar:')
print('1- Adição')
print('2- Subtração')
print('3- Multiplicação')
print('4- Divisão')
print('')
escolha = input('Digite a opção desejada:')

match escolha:
    case "1": #ADIÇÃO
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 + num2
        print('A sua soma é: ', resultado)
        print('')

    case "2": #SUBTRAÇÃO
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 - num2
        print('A sua soma é: ', resultado)
        print('')
    
    case "3": #MULTIPLICAÇÃO
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 * num2
        print('A sua soma é: ', resultado)
        print('')
    
    case "4": #DIVISÃO
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 / num2
        print('A sua soma é: ', resultado)
        print('')
