from random import randint

def geralista(n):
    lista = []
    while n:
        lista.append(randint(0,100))
        n-=1
    return lista

def Radix(lista):
    Lista_copia = []
    Max_termos_na_Lista = len(str(max(lista)))
    for i in lista:
        zeroNum = str(i)
        zeroNum = str("0" * (Max_termos_na_Lista - len(zeroNum)))+ zeroNum
        Lista_copia.append(zeroNum)
    while Max_termos_na_Lista > 0:
        listaBucket = []
        for i in range(len(Lista_copia)):
            for j in Lista_copia:
                if int (j[Max_termos_na_Lista- 1]) == i:
                    listaBucket.append(j)
        Lista_copia = listaBucket.copy()
        listaBucket.clear()
        Max_termos_na_Lista-=1
        lista.clear()
    for i in Lista_copia:
        lista.append(int(i))
    return lista

def Principal():
    lista=geralista(10)
    print(lista)
    Radix(lista)
    print(lista)

Principal()
