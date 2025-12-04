class ContaBancaria:
    def __init__(self):
        self.__id__ = ''
        self.__saldo__ = 0
    
    def getSaldo(self) -> int:
        return self.__saldo__
    
    def transacao(self, valor, destino: 'ContaBancaria'):
        if valor <= 0:
            return False
        destino.__setSaldo__(destino.getSaldo() + valor)
        return True

    def __setSaldo__(self, valor: int):
        self.__saldo__ = valor
    
    def setId(self, id):
        self.__id__ = id

    def __repr__(self):
        return f'Conta bancária de ID {self.id}'