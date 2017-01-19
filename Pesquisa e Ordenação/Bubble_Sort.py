from random import randint

def Cria_lista(l):
    lista_nova = []
    for k in range(l):
        lista_nova.append(randint(0, 99))
    return lista_nova

def bubblesort(lista):
    for i in range(len(lista)):
        j = i + 1
        for j in range(len(lista) - 1):
            if ((lista[i] < lista[j])):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


def Main():
    lista=Cria_lista(int(input("digite o tamanho da lista:")))
    print(lista)
    bubblesort(lista)
    print(lista)

Main()
