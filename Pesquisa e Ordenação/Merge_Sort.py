from random import randint

def Cria_lista(l):
    lista_nova = []
    for k in range(l):
        lista_nova.append(randint(0, 99))
    return lista_nova

def merge(lista):
    if len(lista) > 1:
        meio = int(len(lista) / 2)
        LE = lista[:meio]
        LD = lista[meio:]
        merge(LE)
        merge(LD)
        i = 0
        j = 0
        k = 0
        while i < len(LE) and j < len(LD):
            if LE[i] < LD[j]:
                lista[k] = LE[i]
                i += 1
            else:
                lista[k] = LD[j]
                j += 1
            k += 1
        while i < len(LE):
            lista[k] = LE[i]
            i += 1
            k += 1
        while j < len(LD):
            lista[k] = LD[j]
            j += 1
            k += 1


def Main():
    lista=Cria_lista(int(input("digite o tamanho da lista:")))
    print(lista)
    merge(lista)
    print(lista)


Main()
