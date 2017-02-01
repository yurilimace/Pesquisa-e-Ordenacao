from random import randint

def geralista(n):
    lista = []
    while n:
        lista.append(randint(0,100))
        n-=1
    return lista

def Bucketsort(lista):
    listaBucket = []
    for i in range(0,10):
        listaBucket.append([])
    divisor = max(lista)/len(listaBucket)
    if not isinstance(divisor,int):
        divisor = int(divisor)+1
    for i in lista:
        indice = int(i / divisor)
        listaBucket[indice].append(i)
    for i in listaBucket:
        if not i == []:
            for j in range(len(i)):
                for k in range(j+1,len(i)):
                    if i[j] > i[k]:
                        aux = i[j]
                        i[j] = i[k]
                        i[k] = aux
    indice = 0
    while indice < len(lista):
        for i in listaBucket:
            if not i == []:
                for j in i:
                    lista[indice] = j
                    indice+=1
    return lista



def Principal():
    lista=geralista(10)
    print(lista)
    Bucketsort(lista)
    print(lista)

Principal()
