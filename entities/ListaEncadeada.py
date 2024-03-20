from entities.No import No


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def inserirFim(self, valor):
        novoNo = No(valor)
        if self.primeiro is None:
            self.primeiro = novoNo
        else:
            aux = self.primeiro
            while aux.proximo is not None:
                aux = aux.proximo

            aux.proximo = novoNo

    def busca(self, valor):
        if self.primeiro is not None:
            aux = self.primeiro
            while aux is not None:
                if aux.valor is valor:
                    return aux
                aux = aux.proximo
            print("Não achou")
        else:
            print("Não tem nada na lista")

    def exclusao(self, valor):
        aux = self.busca(valor)
        if aux is not None:
            nodo = self.primeiro
            if nodo is not aux:
                while nodo.proximo is not aux:
                    nodo = nodo.proximo
                nodo.proximo = aux.proximo
            else:
                self.primeiro = aux.proximo
            aux = None

    def mostrarLista(self):
        if self.primeiro is not None:
            x = self.primeiro
            while x is not None:
                x.mostrarNo()
                x = x.proximo
        else:
            print("Lista vazia")
