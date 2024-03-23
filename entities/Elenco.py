from entities.Jogador import Jogador
from entities.No import No


class Elenco:
    def __init__(self, nome):
        self.nome = nome
        self.primeiro = None

    def inserirJogador(self, nome, numeroCamisa, posicao):  # inserir
        if posicao not in ("GOLEIRO", "DEFENSOR", "MEIO CAMPO", "ATACANTE"):
            print("Posição inválida!")
            return

        if numeroCamisa > 100 or numeroCamisa < 1:
            print("Número de camisa inválido! Deve ser maior que 1 e menor que 100")
            return

        if self.buscarJogador(numeroCamisa) is not None:
            print("Jogador com essa camisa já existe! ")
            return

        jogador = Jogador(nome, numeroCamisa, posicao)
        novoNo = No(jogador)
        if self.primeiro is None:
            self.primeiro = novoNo
        else:
            aux = self.primeiro
            while aux.proximo is not None:
                aux = aux.proximo

            aux.proximo = novoNo

        print("Novo jogador inserido")

    def buscarJogador(self, numeroCamisa):  # busca
        if self.primeiro is not None:
            aux = self.primeiro
            while aux is not None:
                if aux.jogador.numeroCamisa == numeroCamisa:
                    return aux
                aux = aux.proximo
            return None
        else:
            return None

    def rescindirContrato(self, numeroCamisa):  # exclusão
        if self.primeiro is None:
            print("Elenco vazio")
            return

        aux = self.buscarJogador(numeroCamisa)
        if aux is not None:
            nodo = self.primeiro
            if aux.jogador.numeroCamisa != self.primeiro.jogador.numeroCamisa:
                while nodo.proximo is not aux:
                    nodo = nodo.proximo
                nodo.proximo = aux.proximo
            else:
                self.primeiro = aux.proximo

            print(f'O jogador {aux.jogador.nome} foi excluído')
            aux = None
        else:
            print("Jogador com este número não encontrado")

    def relatorioElenco(self):  # print
        if self.primeiro is not None:
            print(f'Time: {self.nome}')
            x = self.primeiro
            while x is not None:
                x.jogador.relatorioJogador()
                x = x.proximo
        else:
            print("Elenco vazio")
