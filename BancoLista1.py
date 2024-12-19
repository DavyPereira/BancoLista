# Arquivo: banco_lista.py

class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return True
        return False

    def __str__(self):
        return f"Conta {self.numero} - Titular: {self.titular} - Saldo: R${self.saldo:.2f}"


class BancoLista:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        if isinstance(conta, Conta):
            self.contas.append(conta)
            return True
        return False

    def remover_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                self.contas.remove(conta)
                return True
        return False

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

    def listar_contas(self):
        return [str(conta) for conta in self.contas]



if __name__ == "__main__":
    banco = BancoLista()

    conta1 = Conta(1, "Alice", 1000)
    conta2 = Conta(2, "Bob", 500)

    banco.adicionar_conta(conta1)
    banco.adicionar_conta(conta2)

    print("\nContas no banco:")
    for conta in banco.listar_contas():
        print(conta)

    print("\nBuscando a conta 1:")
    print(banco.buscar_conta(1))

    print("\nRemovendo a conta 2:")
    banco.remover_conta(2)

    print("\nContas no banco após remoção:")
    for conta in banco.listar_contas():
        print(conta)
