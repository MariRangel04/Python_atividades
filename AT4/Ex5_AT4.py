##pessoas lista, dicionario
p1 = {
    "first_name": "Alexandre",
    "last_name": "Fernandes",
    "age": 24,
    "city": "São Paulo"
}

p2 = {
    "first_name": "Vitoria",
    "last_name": "Macedo",
    "age": 25,
    "city": "São Paulo"
}

p3 = {
    "first_name": "Matheus",
    "last_name": "Oliveira",
    "age": 28,
    "city": "Rio de Janeiro"
}

pessoas = [p1, p2, p3]

for pessoa in pessoas:
    print("Nome:", pessoa["first_name"], pessoa["last_name"])
    print("Idade:", pessoa["age"])
    print("Cidade:", pessoa["city"])
    print() 
