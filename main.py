from ClassBanco import Banco
from ClassBanco import Conta
banco = Banco()
conta = Conta(5)
conta.creditar(2000)
conta.debitar(1000)

print(f"Acões Disponíveis /n 1 - Cadastrar Conta: /n 2 - Creditar: 3 - Debitar: 4 - Saldo:/n5 - Transferir: /n6 - Sair:")