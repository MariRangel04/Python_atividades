numero = input('Digite com 10 dígitos:')

if len(numero)!= 10:
    print('Por Favor, digite um número válido, com 10 dígitos:')
else:
    for digito in numero:
        print(digito, end='  ')
