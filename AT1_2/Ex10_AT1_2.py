##verificar se é primo ou não
numero = int(input('Digite um valor:'))

aux = numero
contador = 0 

while aux>0:
    if numero%aux == 0:
        contador +=1
    aux-=1

if contador == 2:
    print('É primo!')
else: 
    print('Não é primo')
    
