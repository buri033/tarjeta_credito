class compra:
    def __init__(self, tasa:float, valor:float, cuotas:int):
       self.__tasa = tasa
       self.__valor = valor
       self.__numero_cuotas=cuotas
       #self.__cuotas = List[com]

    def get_tasa(self)->float:
        return self.__tasa
    
    def set_tasa(self,tasa:float):
        self.__tasa = tasa
    
    def set_valor(self,valor:float):
        if valor < 0:
            print("ADVERTENCIA EL valor no debe ser negativo")
        self.__valor = valor

    def get_valor(self)->float:
        return self.__valor

    def set_numero_cuotas(self,valor:int):
        self.__numero_cuotas = valor

    def get_numero_cuotas(self)->int:
        return self.__numero_cuotas
    
    def __calcular_cuota(self)->float:
        return (self.__valor*self.__tasa)/(1-(1+self.__tasa)**(-self.__numero_cuotas))
    
    def __calcular_intereses(self)->float:
        cuota = self.__calcular_cuota()
        return (cuota*self.__numero_cuotas)-self.__valor
    
    def calcular_plan_amortizacion(self):
        print("calcular plan")
        
