## menu, calculadora
while True:
    num = int(input('Digite um valor:'))
    print('------MENU------')
    print('  1. adição     ')
    print('  2. subtração  ')
    print('  3. divisão    ')
    print('4. multiplicação')
    print('  5. saída      ')
    print('----------------')
    
    opcao = int(input('Digite uma das opções do menu:'))
    
    i = 0
    if opcao >= 1 and opcao <= 5:
        if opcao == 1:
            for i in range(0,11):
                print(num, '+', i, '=', num + i)
        elif opcao == 2:
            for i in range(0,11):
                print(num,'-', i,'=', num - i)
        elif opcao == 3:
            for i in range(1,11):
               resultado = num / i
               print(f'{num} / {i} = {resultado:.1f}')
        elif opcao == 4:
             for i in range(0,11):
                print(num, '*', i, '=',num*i)
        elif opcao == 5:
            breakpoint
        else:
            print('Opção inválida! Digite uma opação válida.')

