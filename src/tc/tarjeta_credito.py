class tarjeta_credito:
    def __init__(self, tasa:float):
        self.__tasa = tasa

    def get_tasa(self)->float:
        return self.__tasa
    
    def set_tasa(self,tasa:float):
        self.__tasa = tasa