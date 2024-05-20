## pets dicionario

cachorro = {"tipo": "cachorro", "dono": "José"}
gato = {"tipo": "gato", "dono": "Alexandre"}
coelho = {"tipo": "coelho", "dono": "Vitória"}
passarinho = {"tipo": "passarinho", "dono": "Matheus"}

pets = [cachorro, gato, coelho, passarinho]

for pet in pets:
    print("Nome:", list(pet.keys())[0])  
    print("Tipo:", pet["tipo"])
    print("Dono:", pet["dono"])
    print()  
