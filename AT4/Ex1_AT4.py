##qtd caracteres
frase = input('Digite uma frase:')
contagem = {}

for char in frase:
    if char in contagem:
        contagem[char] += 1
    else:
        contagem[char] = 1

print(contagem)
