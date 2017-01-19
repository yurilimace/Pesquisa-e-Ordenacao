from random import randint

def Cria_lista(l):
    lista_nova = []
    for k in range(l):
        lista_nova.append(randint(0, 99))
    return lista_nova
 
 
def Insertion(lista_coral):
    for i in range(1, len(lista_coral)):
        x = lista_coral[i]
        j = i - 1
        while (lista_coral[j] > x and j >= 0):
            lista_coral[j + 1] = lista_coral[j]
            j = j - 1;
        lista_coral[j + 1] = x


def Main():
    lista=Cria_lista(int(input("digite o tamanho da lista:")))
    print(lista)
    Insertion(lista)
    print(lista)

Main()
    
