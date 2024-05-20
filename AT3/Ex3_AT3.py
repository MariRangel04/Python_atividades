## parenteses
expressao = input("Digite uma expressão: ")

pilha = []
erro = False

for char in expressao:
    if char == '(':  
        pilha.append(char)  
    elif char == ')':  
        if len(pilha) == 0:  
            erro = True
            break
        pilha.pop()  

if len(pilha) == 0 and not erro:
    print("OK")  
else:
    print("Erro")
