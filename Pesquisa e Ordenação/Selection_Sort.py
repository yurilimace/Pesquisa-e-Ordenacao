from random import randint

def Cria_lista(l):
    lista_nova = []
    for k in range(l):
        lista_nova.append(randint(0, 99))
    return lista_nova

def selection(lista):
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            if (lista[j] < lista[menor]):
                menor = j
 
        aux = lista[menor]
        lista[menor] = lista[i]
        lista[i] = aux

def Main():
    lista=Cria_lista(int(input("digite o tamanho da lista:")))
    print(lista)
    selection(lista)
    print(lista)

Main()
