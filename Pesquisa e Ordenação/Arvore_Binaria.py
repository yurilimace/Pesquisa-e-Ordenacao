import os
from random import randint
import timeit
import matplotlib.pyplot as plt
os.system("clear")
 
def Cria_lista(l):
    lista_nova = []
    for k in range(l):
        lista_nova.append(randint(0, 1000))
    return lista_nova
 
def Tree_Search(value):
    ArvoreBin.pesquisa(raiz,value)
 
def Linear_Search(value):
    for i in range(len(lista)):
        if value == lista[i]:
            return 1
 
class Noh:  #definição da classe Nó
    dado,esquerdo,direito = 0,None,None
    def __init__(self, dado):
        self.esquerdo = None
        self.direito = None
        self.dado = dado
    def __str__(self):
        return "{",str(dado),"}"
  
# fim da classe Noh
  
class ArvoreBinaria:                # Definição da classe árvore
    def __init__(self):
        self.raiz = None            # inicializa a raiz
    def criaNoh(self, dado):        # cria um novo noh e o retorna
        return Noh(dado)
    def insere(self, raiz, dado):   # insere um novo dado
        if raiz == None:            # arvore vazia
            return self.criaNoh(dado)
        else:
            if dado <= raiz.dado:
                raiz.esquerdo = self.insere(raiz.esquerdo, dado)
            else:
                raiz.direito = self.insere(raiz.direito, dado)
        return raiz
          
    def pesquisa(self, raiz, valor): # Pesquisa um valor na árvore
        if raiz == None:
            return 0
        else:
            if valor == raiz.dado:
                return 1
            else:
                if valor < raiz.dado:
                    return self.pesquisa(raiz.esquerdo, valor)
                else:
                    return self.pesquisa(raiz.direito, valor)
    def imprimirArvore(self, raiz): # imprime a árvore
        if raiz == None:
            pass
        else:
            self.imprimirArvore(raiz.esquerdo)
            print("{",raiz.dado,"}", end=' ')
            self.imprimirArvore(raiz.direito)
    def imprimeArvoreInvertida(self, raiz): # imprime a árvore invertida
        if raiz == None:
            pass
        else:
            self.imprimeArvoreInvertida(raiz.direito)
            print("{",raiz.dado,"}", end=' ')
            self.imprimeArvoreInvertida(raiz.esquerdo)
    def imprimeNohs(self,raiz):
        if raiz == None: return
        a = raiz.dado
        if raiz.esquerdo != None:
            b = raiz.esquerdo.dado
        else:
            b = None
        if raiz.direito != None:
            c = raiz.direito.dado
        else:
            c = None
        print("{",a,"[",b,",",c,"]","}", end=' ')
        self.imprimeNohs(raiz.esquerdo)
        self.imprimeNohs(raiz.direito)
                      
 
 
size=[10, 100, 200, 400, 700, 1000, 5000, 6000, 10000, 15000]
TotaltimeSeq=[]
TotaltimeBinary=[]
i=0
while(i<len(size)):
    lista=Cria_lista(size[i])
    randNumbers=Cria_lista(size[i])
    Rootvalue=lista[0]
 
    ArvoreBin=ArvoreBinaria()
    raiz = ArvoreBin.criaNoh(Rootvalue)
 
    time_seq=[]
    time_tree=[]
 
    for k in lista:
      dado=k
      ArvoreBin.insere(raiz,dado)
    for j in randNumbers:
      time_seq.append(timeit.timeit("Linear_Search({})".format(i),setup="from __main__  import Linear_Search",
                          number=1))
      time_tree.append(
            timeit.timeit("Tree_Search({})".format(i), setup="from __main__ import Tree_Search", number=1))
    TotaltimeSeq.append(sum(time_seq))
    TotaltimeBinary.append(sum(time_tree))
    i+=1
 
 
plt.plot(size,TotaltimeSeq,"*-",label="Pesquisa Linear")
plt.plot(size,TotaltimeBinary,"o-",label="Pesquisa Arvore")
 
plt.legend(("Pesquisa Linear","Pesquisa Arvore"),loc='best')
plt.ylabel("tempo")
plt.xlabel("tamanho")
plt.show()
     
 
         
          
# fim do programa
