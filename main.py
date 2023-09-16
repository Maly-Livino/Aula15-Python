# Como criar uma classe

class Carro:
    # Metodo/Função construtor
    def __init__(self,m,c,a,quatro_p):
        # Como criar Atributos/Caracteristicas de um objrto
        self.modelo = m
        self.cor = c
        self.ano = a
        self.quatro_portas = quatro_p
        print(f"Modelo do objeto criado:{self.modelo}")
        # self => Representação abstrata do objeto criado
        self.velocidade_atual = 0

    #Criando ações para o objeto Carro
    def acelerar(self,velocidade):
        self.velocidade_atual += velocidade
        print(f"Acelerando...Velocidade Atual = {self.velocidade_atual}")


# Como criar um objeto
carro1 =  Carro("Corsa", "Vermelho",2015,False)
carro2 = Carro("Palio","Branco",2018,True)


# Como acessar e alterar caracteristicas/propriedades de um objeto
print(f"Cor do carro 1 :{carro1.cor}")
carro1.cor= "Azul"
print(f"Cor do carro 1 agora:{carro1.cor}")

# Acessando o metodo Acelerar

print("Carro 1")
carro1.acelerar(15)
carro1.acelerar(20)
carro1.acelerar(25)
carro1.acelerar(30)
carro1.acelerar(35)
carro1.acelerar(40)
carro1.acelerar(45)
carro1.acelerar(50)
carro1.acelerar(60)
print("Carro 2")
carro2.acelerar(70)
carro2.acelerar(75)
carro2.acelerar(80)
carro2.acelerar(85)
carro2.acelerar(90)
carro2.acelerar(95)
carro2.acelerar(100)












