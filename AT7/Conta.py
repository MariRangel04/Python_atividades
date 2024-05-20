from datetime import datetime

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def dados_cliente(self):
        return f"Nome: {self.nome} {self.sobrenome}\nCPF: {self.cpf}"
    
class Historico:
    def __init__(self):
        self.data_da_abertura = datetime.now()
        self.transacoes = []

    def imprime(self):
        for transacao in self.transacoes:
            print(transacao)

class ContaBancaria:
    def __init__(self, numero_agencia, tipo_conta, saldo, limite):
        self.numero_agencia = numero_agencia
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
        

    def consultar_saldo(self):
        return self.saldo

    def saca(self, valor):
        if self.saldo - valor >= -self.limite:
            self.saldo -= valor
            self.historico.transacoes.append(f"Saque: R${valor}")
            return True
        else:
            return False

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f"Deposito: R${valor}")

    def transfere_para(self, destino, valor):
        if self.saca(valor):
            destino.deposita(valor)
            self.historico.transacoes.append(f"Transferencia para {destino.numero_agencia}: R${valor}")
            destino.historico.transacoes.append(f"Transferencia recebida de {self.numero_agencia}: R${valor}")
            return True
        else:
            return False

    def obter_extrato(self):
        self.historico.imprime()

    def alterar_titular(self, novo_titular):
        self.titular = novo_titular

    def fechar_conta(self):
        self.titular = None
        self.saldo = 0

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_agencia, tipo_conta, saldo, limite, aniversario_conta):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.aniversario_conta = aniversario_conta

    def calcular_juros_mensal(self):
        pass

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_agencia, tipo_conta, saldo, limite, cheque_especial):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.cheque_especial = cheque_especial

    def utilizar_cheque_especial(self, valor):
        if self.cheque_especial:
            self.saldo -= valor
            self.historico.transacoes.append(f"Utilizacao do cheque especial: R${valor}")
            return True
        else:
            return False

cliente1 = Cliente("Alexandre", "Macedo", "999.222.343-10")

conta_corrente1 = ContaCorrente("001", "corrente", 2000.0, 1100.0, True)

conta_corrente1.deposita(900.0)

conta_poupanca1 = ContaPoupanca("001", "poupança", 2000.0, 0.0, "20/08")

conta_corrente1.transfere_para(conta_poupanca1, 600.0)

conta_corrente1.utilizar_cheque_especial(400.0)

print("Extrato da Conta Corrente:")
conta_corrente1.obter_extrato()

print("\nExtrato da Conta Poupanca:")
conta_poupanca1.obter_extrato()

print("\nDados do Cliente:")
print(cliente1.dados_cliente())
