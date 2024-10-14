class Ascii_Palavras():
    #inicializa colocando as letras do alfabeto na lista
    def __init__(self):
        self.lista2=[]
        for i in range(0,26):
            self.lista2.append(chr(97+i))
    #transforma as letras da palavra em sua posicao no alfabeto, ex.: a=1,b=2,c=3...
    def criptografia(self,palavra):
        criptar=list(palavra)
        for j in range(0,len(palavra)):
            for i in range(0,len(self.lista2)):
                if criptar[j]==self.lista2[i]:
                   print(i+1,end=' ')
                   break
                

#chama a classe 
cripto=Ascii_Palavras()
palavra_escolhida=str(input("digite uma palavra para criptografar:"))
cripto.criptografia(palavra_escolhida)  
#Desafio do criascript, Desafiando devs 8



