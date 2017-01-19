from random import randint

def Cria_lista(l):
    lista_nova = []
    for k in range(l):
        lista_nova.append(randint(0, 99))
    return lista_nova

 
def quickSort(vetor, inicio, fim):
    if (inicio < fim):
        q = Quebralista(vetor, inicio, fim)
        quickSort(vetor, q[1], q[0] - 1)
        quickSort(vetor, q[0] + 1, q[2])
 
 
def Quebralista(vetor, inicio, fim):
    pivo = vetor[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if (vetor[j] <= pivo):
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
    vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]
    return i + 1, inicio, fim

def Main():
    lista=Cria_lista(int(input("digite o tamanho da lista:")))
    print(lista)
    quickSort(lista,0,len(lista)-1)
    print(lista)


Main()
