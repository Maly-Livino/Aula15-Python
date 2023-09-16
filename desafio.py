class Elevador:
    def __init__(self, qtd_andares, andar_atual, capacidade,
                 qtd_pessoas):
        self.qtd_andares = qtd_andares
        self.andar_atual = andar_atual
        self.capacidade = capacidade
        self.qtd_pessoas = qtd_pessoas

    def subir(self):
        if self.andar_atual + 1 <= self.qtd_andares:
            self.andar_atual += 1
            print(f"Subindo... Andar atual: {self.andar_atual}")
        else:
            print("Estamos no ultimo andar! Não podemos subir!")
    def descer(self):
        if self.andar_atual - 1 >= 0:
            self.andar_atual -= 1
            print(f"Descendo... Andar atual: {self.andar_atual}")
        else:
            print(f"Estamos no terreo! Não podemos descer!")
    def entrar(self, qtd):
        if self.qtd_pessoas + qtd <= self.capacidade:
            self.qtd_pessoas += qtd
            print(f"Entrando... Quantidade atual: {self.qtd_pessoas}")
        else:
            print(f"Limite máximo de pessoas atingido!")
    def sair(self, qtd):
        if self.qtd_pessoas - qtd >= 0:
            self.qtd_pessoas -= qtd
            print(f"Saindo... Quantidade de pessoas: {self.qtd_pessoas}")
        else:
            self.qtd_pessoas = 0
            print(f"Saindo... Quantidade de pessoas: {self.qtd_pessoas}")