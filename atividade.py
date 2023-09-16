#1. Crie uma classe para representar uma conta bancária, com os seguintes atributos
#-> número conta
#-> nome do cliente
#-> saldo
#2. Em seguida crie um objeto da classe conta bancária


class Banco:
    def __init__(self,n,nome,s):
        self.numero_da_conta = n
        self.nome_do_cliente = nome
        self.saldo = s

cliente1 = Banco(123, "Jonatha", 1500)
cliente2 = Banco(456, "Agatha", 34400)

print(f"Nome do Cliente 1:{cliente1.nome_do_cliente}")

"""
3. Crie um método para deposito na conta bancária. Essa função recebe o valor de deposito por parametro, e este valor
 é acrescido ao saldo.


4. Crie um método para saque na conta bancária. Essa função recebe o valor de saque e este valor é retirado do saldo.
 Obs: Não pode realizar o saque se o valor de retirada for maior que o saldo.
"""

class Banco:
    def __init__(self,n,nome,s):
        self.numero_da_conta = n
        self.nome_do_cliente = nome
        self.saldo = s

    def depositar(self,valor):
        self.saldo += valor
        print(f"Deposito Realizado com Sucesso")
        print(f"Saldo Atual: {self.saldo}")

    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque realizado com sucesso")
            print(f"Saldo Atual: {self.saldo}")
        else:
            print("Saldo Insuficiente")
            print(f"Seu Saldo: {self.saldo}")



conta1 = Banco(1,"Jonatha", 1500)
conta1.depositar(55)
conta1.sacar(300)
conta1.sacar(300)