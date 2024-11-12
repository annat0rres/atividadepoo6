# Anna Clara Melo e Hellen Vitória Matos, INFO2V

class Fatura:
    def __init__ (self, num, qtd, price):
        self.numero = num
        self.quantidade = qtd
        self.preco = price

    def getNum (self):
        return self.numero
    
    def setNum (self, num):
        self.numero = num

    def getQuant (self):
        return self.quantidade
    
    def setQuant (self, qtd):
        self.quantidade = qtd

    def getPreco (self):
        return self.preco
    
    def setPreco (self, price):
        self.preco = price 

    
    def getTotal (self):
        total = self.preco * self.quantidade
        return f'total -> R$ {total}'

class TestarFatura:
    @staticmethod
    def main():
        n = int(input('digite o número da fatura: '))
        q = int(input('digite a quantidade de itens: '))
        p = float(input('digite o preço unitário do item: '))

        fatura = Fatura(n, q, p)
        print(f'fatura n° {fatura.getNum()}:')
        print(fatura.getTotal())
        q = int(input('digite a nova quantidade de itens: '))
        fatura.setQuant(q)
        print(fatura.getTotal())

TestarFatura.main()