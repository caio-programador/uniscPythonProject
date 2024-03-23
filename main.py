from entities.Time import Time
from time import sleep


def menu(time):
    print(f'Gerencie o {time.nome} aqui:')
    print("1 - Novo jogador para o elenco")
    print("2 - Buscar jogador pelo número da camisa")
    print("3 - Rescindir contrato de jogador")
    print("4 - Mudar número de jogador")
    print("5 - Relatório de elenco")
    print("0 - Fechar programa")


def insere(time):
    nome = input("Nome do jogador: ")
    numeroCamisa = int(input("Número da camisa: "))
    posicao = input("Posição: ")
    time.inserirJogador(nome, numeroCamisa, posicao)


def buscarJogador(time):
    numeroCamisa = int(input("Informe o número da camisa do jogador que deseja buscar: "))
    jogador = time.buscarJogador(numeroCamisa)
    if jogador is None:
        print("Nenhum jogador com este número existe!")
    else:
        jogador.jogador.relatorioJogador()


def editarNumero(time):
    numeroCamisa = int(input("Informe o número da camisa do jogador que deseja editar: "))
    jogador = time.buscarJogador(numeroCamisa)
    if jogador is None:
        print("Nenhum jogador com este número existe!")
    else:
        jogador.numeroCamisa = int(input("Novo número do jogador: "))
        print("Jogador alterado com sucesso")


def main():
    nome = input("Bem vindo! Qual seu nome? ")
    time = Time(input(f'{nome}, qual o nome do seu time? '))
    sleep(0.6)
    while True:
        menu(time)
        option = int(input())
        if option == 1:
            insere(time)
        elif option == 2:
            buscarJogador(time)
        elif option == 3:
            numeroCamisa = int(input("Informe o número da camisa do jogador que deseja rescindir o contrato: "))
            time.rescindirContrato(numeroCamisa)
        elif option == 4:
            editarNumero(time)
        elif option == 5:
            time.relatorioElenco()
        elif option == 0:
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida")


main()

