from random import randint
import copy

def geralista(n):
    lista = []
    while n:
        lista.append(randint(0,100))
        n-=1
    return lista

def Countingsort(lista):
    lisWork = []
    lisCount = []
    lisSumCount = []
    for i in range (min(lista),max(lista)+1):
        lisWork.append(i)
    for i in lisWork:
        cont = 0
        for j in lista:
            if i == j:
                cont+=1
        lisCount.append(cont)
    cont = 0
    for i in lisCount:
        cont+=i
        lisSumCount.append(cont)
    lisCount.clear()
    for i in range(max(lisSumCount)):
        lisCount.append(" ")
    while cont :
        for i in range(len(lista)):
            for j in range(len(lisWork)):
                if lista[i] == lisWork[j]:
                    lisCount[lisSumCount[j]-1] = lista[i]
                    lisSumCount[j] = lisSumCount[j]-1
                    cont -=1
   
    lista.clear()
    for i in lisCount:
        lista.append(i)
    return lista


def Principal():
    lista=geralista(10)
    print(lista)
    Countingsort(lista)
    print(lista)

Principal()
