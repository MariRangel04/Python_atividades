lista = [1, 2, 3, 4, 5]
alterada = [3, 4, 6, 7, 8]

inicial = set(lista)
alterada = set(alterada)
semAlteracao = inicial.intersection(alterada)
novos = alterada.difference(inicial)
removidos = inicial.difference(alterada)

print("Elementos que não mudaram:", semAlteracao)
print("Elementos novos:", novos)
print("Elementos removidos:", removidos)
