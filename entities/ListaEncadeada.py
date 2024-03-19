from entities.No import No


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def inserirFim(self, valor):
        novoNo = No(valor)
        if self.primeiro is None:
            self.primeiro = novoNo
        else:
            x = self.primeiro
            while x.proximo is not None:
                x = x.proximo

            x.proximo = novoNo
        print(f'Show!!! {novoNo.mostrarNo()} Inserido!!!')


    def mostrarLista(self):
        x = self.primeiro
        while x.proximo is not None:
            print(x.mostrarNo())
            x = x.proximo