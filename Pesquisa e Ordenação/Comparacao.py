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


questao = [1000,3000,6000,9000,12000,15000,18000,21000,24000]
selection_time = []
insertion_time = []
bubble_time = []
quick_time = []
merge_time = []
shell_time = []
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
 
 
    tempo.append(tempo_gera)
    selection_time.append(tempo_selection)
    insertion_time.append(tempo_insertion)
    bubble_time.append(tempo_bubble)
    quick_time.append(tempo_quick)
    merge_time.append(tempo_merge)
    shell_time.append(tempo_shell)
 
plt.figure(1)
plt.plot(questao,tempo, '+-', label='Tempo de geração')
plt.plot(questao,insertion_time, "*-", label='Insertion sort')
plt.plot(questao,selection_time, "o-", label='Selection sort')
plt.plot(questao, bubble_time, "x-", label='Bubble Sort')
plt.plot(questao, quick_time, "d-", label='Quick Sort')
plt.plot(questao, merge_time, "v-", label='Merge Sort')
plt.plot(questao, shell_time, "y-", label='Shell Sort')
 
 
plt.legend(('Tempo de geração','Selection sort','Insertion sort','Bubble Sort','Quick Sort', 'Merge Sort', 'Shell Sort'), loc='best')
plt.title('Seleção-Inserção-Bolha-Quick-Mistura- Shell')
plt.ylabel('Tempo de ordenação')
plt.xlabel('Número de itens na lista')
plt.show()
