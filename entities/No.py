class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrarNo(self):
        print(self.valor, end="")