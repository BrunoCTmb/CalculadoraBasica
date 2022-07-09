class Calculadora:
    def __init__(self):
        self.lista_conta = []  
        self.total = 0
        self.sinal = '+'

    def main(self):
        while True:
            num = int(input('valor: '))

            if self.sinal == '+':
                self.total += num
            elif self.sinal == '-':
                self.total -= num
            elif self.sinal == '*':
                self.total *= num
            elif self.sinal == '/':
                self.total /= num
            elif self.sinal == '=':
                break
            
            self.sinal = input('sinal: ')
            print(self.total)

        print('total da conta:', self.total)

calculadora = Calculadora()
calculadora.main()
