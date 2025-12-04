from Cliente import Cliente
from ContaBancaria import ContaBancaria

# clientes = []
# clientes.append(Cliente())
# clientes[0].setIdentificacao("Guilherme", "850.409.910.53")
# clientes[0].setConta('123')

# clientes.append(Cliente())
# clientes[1].setIdentificacao("braian", "59825932532")
# clientes[1].setConta('456')

# clientes.append(Cliente())
# clientes[2].setIdentificacao("erik", "01583581")
# clientes[2].setConta('789')

# print(clientes)


conta1 = ContaBancaria()
conta1.transacao(500, conta1)
print(conta1.getSaldo())

