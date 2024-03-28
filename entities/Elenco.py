import random

from entities.Jogador import Jogador
from entities.No import No
from faker import Faker


class Elenco:
    def __init__(self, nome):
        self.nome = nome
        self.primeiro = None
        self.POSICOES_PRIORIDADE = {
            "ATACANTE": 1,
            "MEIO CAMPO": 2,
            "DEFENSOR": 3,
            "GOLEIRO": 4
        }

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

    def gerarDados(self):
        faker = Faker()
        numeroEmUso = set()  # set é um Conjunto sem elementos duplicados

        for i in range(11):
            # adiciona apenas 1 goleiro
            if i == 0:
                posicao = "GOLEIRO"
            else:
                posicao = random.choice(["DEFENSOR", "MEIO CAMPO", "ATACANTE"])

            nome = faker.name()
            numeroCamisa = random.randint(1, 99)
            while numeroCamisa in numeroEmUso:
                numeroCamisa = random.randint(1, 99)
            numeroEmUso.add(numeroCamisa)

            self.inserirJogador(nome, numeroCamisa, posicao)

        print("\nDados inseridos com sucesso!\n")

    def ordena(self):
        if self.primeiro is None:
            print("Elenco vazio")
            return

        if self.primeiro.proximo is None:
            print("Temos apenas um jogador no elenco")
            return

        anterior = self.primeiro

        while anterior.proximo is not None:
            atual = anterior.proximo
            while atual is not None:
                comparaPosicao = (self.POSICOES_PRIORIDADE[anterior.jogador.posicao] >
                                  self.POSICOES_PRIORIDADE[atual.jogador.posicao])
                comparaNumero = atual.jogador.numeroCamisa < anterior.jogador.numeroCamisa

                if comparaPosicao or (comparaNumero and self.POSICOES_PRIORIDADE[anterior.jogador.posicao] ==
                      self.POSICOES_PRIORIDADE[atual.jogador.posicao]):
                    temp = atual.jogador
                    atual.jogador = anterior.jogador
                    anterior.jogador = temp
                atual = atual.proximo
            anterior = anterior.proximo

        print("Elenco ordenado")
