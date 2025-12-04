class Cliente:
    def __init__(self):
        self.__nome__ = ''
        self.__cpf__ = ''
        self.__conta__ = False

    def __validaCPF__(self, cpf):
        return True

    def setIdentificacao(self, __nome__, cpf):
        self.__nome__ = __nome__
        if self.__validaCPF__(cpf):
            self.__cpf__ = cpf

    def __repr__(self):
        saida = f'Cliente: {self.__nome__} de CPF {self.__cpf__}'
        if self.__conta__ != False:
            saida += f' e conta {self.__conta__}'
        return saida
    
    def setConta(self, conta):
        self.__conta__ = conta
    
    def getNome(self):
        return self.__nome__
    
    def getCPF(self):
        return self.__cpf__



