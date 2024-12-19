class Conta:

  def __init__(self, numero):
    self.numero = numero
    self.saldo = 0

  def creditar(self, amount):
    self.saldo += amount
    print(f"Valor creditado: {amount}")
    return self.saldo

  def debitar(self, amount):
    if self.tem_saldo() and self.saldo >= amount:
      self.saldo -= amount
      print(f"Valor Debitado: {amount}")
    else:
      print("Sem Saldo Suficiente na Conta.")
    return self.saldo

  def tem_saldo(self):
    return self.saldo > 0

  def ver_saldo(self):
    return self.saldo

  def ver_numero(self):
    return self.numero

  def set_saldo(self, saldo):
    self.saldo = saldo
    print(f"Valor do Saldo Setado para: {saldo}")


class Banco:

    def __init__(self):
        self.contas = [None] * 100
        self.indice = 0

    def cadastrar(self, conta: Conta):
        self.contas[self.indice] = conta
        self.indice += 1
    
    def procurar_conta(self,numero):
        i = 0
        achou = False
        while achou is False and i < self.indice:
            if self.contas[i].get_numero() == numero:
                achou = True

            else:
                i += 1
        if achou is True:
            return self.contas[i]

        else:
            return None

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)

        else:
            print("Conta Inexistente")


    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditartar(valor)

        else:
            print("Conta Inexistente")

    def transferir(self, origem, destino, valor):
        conta_origem = self.procurar_conta(origem)
        conta_destino = self.procurar_conta(destino)

        if conta_origem and conta_destino:
            if conta_origem.get_saldo() >= valor:
                conta_origem.debitar(valor)
                conta_destino.creditar(valor)
                print("Transferência realizada com sucesso!")
            else:
                print("Saldo insuficiente na conta de origem.")
        else:
            print("Conta de origem ou destino inexistente.")

    def saldo(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            return conta.get_saldo()
        else:
            print("Conta Inexistente")
            return None
            

  