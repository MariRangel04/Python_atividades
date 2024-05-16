##manipulação lista
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]

maior = max(lista)
print('O maior numero:', maior)

menor=min(lista)
print('O menor valor:', menor)

for num in lista:
    if num % 2 == 0:
        print(num)

qtd = lista.count(lista[0])
print(f'qtd ocorrencias:{qtd}')
        
soma=0
i=0
while i < len(lista):
    soma+=lista[i]
    i+=1
print(f'Media: {soma/i}')

soma_neg=0

for num in lista:
    if num < 0:
        soma_neg+=num

print(f'Soma dos negativos:{soma_neg}')

    
