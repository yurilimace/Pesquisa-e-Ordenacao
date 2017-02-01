from random import randint

def heapaux(lista, primeiro,ultimo):
    valor_max = 2 * primeiro + 1
    while (valor_max <= ultimo):
        if ( valor_max < ultimo ) and ( lista[valor_max] < lista[valor_max + 1] ):
            valor_max += 1
        if lista[valor_max] > lista[primeiro]:
            lista[valor_max], lista[primeiro] = lista[primeiro], lista[valor_max]
            primeiro = valor_max
            valor_max = 2 * primeiro + 1
        else:
            return
 
def HeapSort(lista):
  valor_min = len( lista ) - 1
  ultimoFilho = int (valor_min/2)
  for i in range ( ultimoFilho, -1, -1 ):
    heapaux(lista,i,valor_min)
  for i in range(valor_min,0,-1 ):
    if lista[0] > lista[i]:
      lista[0],lista[i] = lista[i], lista[0]
      heapaux(lista,0,i-1)


def Principal():
    lista=[]
    for i in range(0,10):
        lista.append(randint(0,1000))
    print(lista)
    HeapSort(lista)
    print(lista)


Principal()
