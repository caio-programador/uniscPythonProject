class Jogador:
    def __init__(self, nome, numeroCamisa, posicao):
        self.nome = nome
        self.numeroCamisa = numeroCamisa
        self.posicao = posicao

    def relatorioJogador(self):
        print(f'Posição: {self.posicao} | Número da Camisa: {self.numeroCamisa} | Nome: {self.nome}')
