lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 1, 6, 7, 8]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

valores_comuns = conjunto1.intersection(conjunto2)
print("Valores que tem nas duas listas:", valores_comuns)

valores_primeira = conjunto1.difference(conjunto2)
print("Valores apenas da primeira lista:", valores_primeira)

valores_segunda = conjunto2.difference(conjunto1)
print("Valores que só existem na segunda lista:", valores_segunda)

repetidos = list(conjunto1.union(conjunto2))
print("Elementos não repetidos das duas listas:", repetidos)

sem_repetidos = list(conjunto1.difference(conjunto2))
print("A primeira lista sem os elementos repetidos na segunda:", sem_repetidos)
