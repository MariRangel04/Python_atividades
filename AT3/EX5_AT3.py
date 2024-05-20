## separa os num pares e impares em 2 listas 
numeros = [9,8,7,12,0,13,21]
pares=[]
impares=[]

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'pares:{pares}')
print(f'impares:{impares}')
