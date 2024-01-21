class Funciones:
    def __init__(self,lista_entrada) -> None:
        self.lista=lista_entrada
        pass
    
    def es_primo(self): 
        for i in self.lista:
            if (self.__es_primo(i)):
                print(i,"es numero primo")
            else:   
                print(i,"no es numero primo")

    def conversion(self,origen,destino):
        for i in self.lista:
            print(i,'grados',origen,'son',self.__conversion(i,origen,destino),'grados',destino)

    def numero_repetido(self,list):
        for i in self.lista:
            A ,B= self.__numero_repetido(list)

        print("el mas repetido de la lista es",A,'se repite',B,'veces')
        
    def __es_primo(self,numero):
        
        if (numero < 1):
            return False
        for i in range(2,int(numero**0.5)+1):
            if numero % i == 0:
                return False
        return True
    
    def __numero_repetido(self,lista):
        
        numero_de_repetiones = 0
        i= 0
        lista_de_repetidos = []
        lista_de_no_repetidos = []
        contador_local=[]
        for componente in lista:
            if componente not in lista_de_no_repetidos:
                lista_de_no_repetidos.append(componente)
            else:
                lista_de_repetidos.append(componente)
        for componente in lista_de_repetidos:
            contador_local.append(lista_de_repetidos.count(componente))

        contador = max(contador_local)+1
        i = contador_local.index(max(contador_local))
        mas_repetido = lista_de_repetidos[i]
        return mas_repetido,contador
    
    def __conversion(self,valor,origen,destino):

        if origen == "C" and destino == "C":
            resul = valor
            return resul
        if origen == "C" and destino == "F":
            resul = valor * (9/5) + 32
            return resul
        if origen == "C" and destino == "K":
            resul = valor + 273.15
            return resul
        if origen == "F" and destino == "F":
            resul = valor
            return resul
        if origen == "F" and destino == "C":
            resul = (valor - 32) / (9/5)
            return resul
        if origen == "F" and destino == "K":
            resul = (valor - 32) *(5/9) + 273.15
            return resul
        if origen == "K" and destino == "K":
            resul = valor
            return resul
        if origen == "K" and destino == "F":
            resul = (valor-273.15)*(9/5) + 32
            return resul
        if origen == "K" and destino == "C":
            resul = valor + 273.15
            return resul