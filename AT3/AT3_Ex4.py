## verifica max e min temperatura
temperatura =[-10, -8, 0, 1, 2, 5, -2,-4]
i=0
soma=0

max_temp= max(temperatura)
min_temp=min(temperatura)

while i < len(temperatura):
    soma+= temperatura[i]
    i+=1
    
print(f'Temperatura Maxima:{max_temp}')
print(f'Temperatura Minima:{min_temp}')
print(f'Media de Temperatura:{soma/i}')
