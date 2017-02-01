def Cria_lista(l):
    lista_nova = []
    for k in range(l):
        lista_nova.append(randint(0, 99))
    return lista_nova
 
 
def insertion_sort(lista_coral):
    for i in range(1, len(lista_coral)):
        x = lista_coral[i]
        j = i - 1
        while (lista_coral[j] > x and j >= 0):
            lista_coral[j + 1] = lista_coral[j]
            j = j - 1;
        lista_coral[j + 1] = x
 
 
def selection_sort(lista):
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            if (lista[j] < lista[menor]):
                menor = j
 
        aux = lista[menor]
        lista[menor] = lista[i]
        lista[i] = aux
 
        # print(lista)
 
 
def bubble_sort(lista):
    for i in range(len(lista) - 2):
        j = i + 1
        for j in range(len(lista) - 1):
            if ((lista[i] > lista[j])):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
 
 
def quick_sort(vetor, inicio, fim):
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
 
def merge_sort(lista):
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

def shell_sort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)
 
      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap
        alist[position]=currentvalue


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




questao = [1000,3000,6000,9000,12000,15000,18000,21000,24000]
selection_time = []
insertion_time = []
bubble_time = []
quick_time = []
merge_time = []
shell_time = []
radix_time=[]
bucket_time=[]
counting_time=[]
heap_time=[]
tempo = []
 
 
for i in questao:
    lista = lista_aleatoria(i)
 
    tempo_gera = timeit.timeit("lista_aleatoria({})".format(i), setup="from __main__ import lista_aleatoria",number=1)
    tempo_selection = timeit.timeit("selection_sort({})".format(lista[:]), setup="from __main__ import selection_sort",number=1)
    tempo_insertion = timeit.timeit("insertion_sort({})".format(lista[:]), setup="from __main__ import insertion_sort",number=1)
    tempo_bubble = timeit.timeit("bubble_sort({})".format(lista[:]), setup="from __main__ import bubble_sort",number=1)
    tempo_quick = timeit.timeit("quick_sort({})".format(lista[:]), setup="from __main__ import quick_sort",number=1)
    tempo_merge = timeit.timeit("merge_sort({})".format(lista[:]), setup="from __main__ import merge_sort",number=1)
    tempo_shell = timeit.timeit("shell_sort({})".format(lista[:]), setup="from __main__ import shell_sort",number=1)
    tempo_radix = timeit.timeit("Radix({})".format(lista[:]), setup="from __main__ import Radix",number=1)
    tempo_bucket = timeit.timeit("Bucketsort({})".format(lista[:]), setup="from __main__ import Bucketsort",number=1)
    tempo_counting = timeit.timeit("Countingsort({})".format(lista[:]), setup="from __main__ import Countingsort",number=1)
    tempo_heap = timeit.timeit("HeapSort({})".format(lista[:]), setup="from __main__ import HeapSort",number=1)
 
    tempo.append(tempo_gera)
    selection_time.append(tempo_selection)
    insertion_time.append(tempo_insertion)
    bubble_time.append(tempo_bubble)
    quick_time.append(tempo_quick)
    merge_time.append(tempo_merge)
    shell_time.append(tempo_shell)
    radix_time.append(tempo_radix)
    bucket_time.append(tempo_bucket)
    counting_time.append(tempo_counting)
    heap_time.append(tempo_heap)
 
plt.figure(1)
plt.plot(questao,tempo, '+-', label='Tempo de geração')
plt.plot(questao,insertion_time, "*-", label='Insertion sort')
plt.plot(questao,selection_time, "o-", label='Selection sort')
plt.plot(questao, bubble_time, "x-", label='Bubble Sort')
plt.plot(questao, quick_time, "d-", label='Quick Sort')
plt.plot(questao, merge_time, "v-", label='Merge Sort')
plt.plot(questao, shell_time, "y-", label='Shell Sort')
plt.plot(questao, radix_time, "t-", label='Radix Sort')
plt.plot(questao, bucket_time, "i-", label='bucket Sort')
plt.plot(questao, counting_time, "l-", label='bucket Sort')
plt.plot(questao, heap_time, "k-", label='heap Sort')
 
 
plt.legend(('Tempo de geração','Selection sort','Insertion sort','Bubble Sort','Quick Sort', 'Merge Sort', 'Shell Sort','Radix Sort','bucket Sort','bucket Sort','heap Sort'), loc='best')
plt.title('Seleção-Inserção-Bolha-Quick-Shell-Merge-bucket-radix-counting-heap')
plt.ylabel('Tempo de ordenação')
plt.xlabel('Número de itens na lista')
plt.show()
