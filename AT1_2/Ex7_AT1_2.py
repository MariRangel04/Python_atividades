##le qtd segundo, minutos, horas e dias
segundos = int(input('Digite qtd de segundos:'))

minutos = segundos/60
horas = segundos/3600
dias = segundos/84600


print(f'{dias:.1f}', 'dias')
print(f'{horas:.1f}', 'horas')
print(f'{minutos:.1f}', 'minutos')
print(segundos, 'segundos')



