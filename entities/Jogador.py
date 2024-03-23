class Jogador:
    def __init__(self, nome, numeroCamisa, posicao):
        self.nome = nome
        self.numeroCamisa = numeroCamisa
        self.posicao = posicao

    def relatorioJogador(self):
        print(f'Nome: {self.nome} | Número da Camisa: {self.numeroCamisa} | Posição: {self.posicao}')
