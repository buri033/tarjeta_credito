class Cuota:
    def __init__(self, numero:int, valor:float, valor_capital:float, valor_interes:float):
        self.__numero = numero
        self.__valor = valor
        self.__valor_capital = valor_capital 
        self.__valor_capita = valor_capital

    def get_numero(self)->int:
        return self.__numero