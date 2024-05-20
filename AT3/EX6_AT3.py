## sala de cinema
lugares = [10, 2, 1, 3, 0]

while True:
    sala = int(input("Digite o número da sala 1-5 ou 0 para sair: "))
    if sala == 0:
        break
    if sala < 1 or sala > 5:
        print("Sala inválido, tente novamente.")
        continue
    solicitados = int(input("Digite a quantidade lugares desejados: "))

    indice_sala = sala - 1
    if solicitados <= lugares[indice_sala]:
        lugares[indice_sala] -= solicitados
        print(f"Venda realizada! {lugares[indice_sala]} lugares restantes na sala {sala}.")
    else:
        print("Não há lugares disponíveis.")

    print("Lugares atualizados:", lugares)
