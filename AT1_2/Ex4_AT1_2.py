##separar os digitos com um espaço
numero = input('Digite com 5 dígitos:')
i = 0

if len(numero)!= 5:
    print('Por Favor, digite um número válido, com 5 dígitos:')
else:
    for digito in numero:
        print(digito, end='  ')
