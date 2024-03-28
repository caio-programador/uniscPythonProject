from entities.Elenco import Elenco
from time import sleep


def menu(elenco):
    print(f'Gerencie o {elenco.nome} aqui:')
    print("1 - Novo jogador para o elenco")
    print("2 - Buscar jogador pelo número da camisa")
    print("3 - Rescindir contrato de jogador")
    print("4 - Mudar número de jogador")
    print("5 - Relatório de elenco")
    print("6 - Gerar o elenco automaticamente")
    print("7 - Ordenar elenco")
    print("0 - Fechar programa")


def insere(elenco):
    nome = input("Nome do jogador: ")
    numeroCamisa = int(input("Número da camisa: "))
    posicao = input("Posição (GOLEIRO, DEFENSOR, MEIO CAMPO, ATACANTE): ").upper()
    elenco.inserirJogador(nome, numeroCamisa, posicao)


def buscarJogador(elenco):
    numeroCamisa = int(input("Informe o número da camisa do aux que deseja buscar: "))
    aux = elenco.buscarJogador(numeroCamisa)
    if aux is None:
        print("Nenhum aux com este número existe!")
    else:
        aux.jogador.relatorioJogador()


def editarNumero(elenco):
    numeroCamisa = int(input("Informe o número da camisa do jogador que deseja editar: "))
    aux = elenco.buscarJogador(numeroCamisa)
    if aux is None:
        print("Nenhum jogador com este número existe!")
    else:
        novoNumeroCamisa = int(input("Novo número do jogador: "))
        if novoNumeroCamisa > 100 or novoNumeroCamisa < 1 or elenco.buscarJogador(novoNumeroCamisa) is not None:
            print("Número de camisa inválido")
            return

        aux.jogador.numeroCamisa = novoNumeroCamisa
        print("Jogador alterado com sucesso")


def main():
    nome = input("Bem vindo! Qual seu nome? ")
    elenco = Elenco(input(f'{nome}, qual o nome do seu time? '))
    sleep(0.6)
    while True:
        menu(elenco)
        option = int(input())
        if option == 1:
            insere(elenco)
        elif option == 2:
            buscarJogador(elenco)
        elif option == 3:
            numeroCamisa = int(input("Informe o número da camisa do jogador que deseja rescindir o contrato: "))
            elenco.rescindirContrato(numeroCamisa)
        elif option == 4:
            editarNumero(elenco)
        elif option == 5:
            elenco.relatorioElenco()
        elif option == 6:
            elenco.gerarDados()
        elif option == 7:
            elenco.ordena()
            elenco.relatorioElenco()
        elif option == 0:
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida")


main()
