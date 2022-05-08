def heapify(matriz, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2
  
    if esquerda < n and matriz[i] < matriz[esquerda]:
        maior = esquerda
  
    if direita < n and matriz[maior] < matriz[direita]:
        maior = direita
  
    if maior != i:
        matriz[i], matriz[maior] = matriz[maior], matriz[i]
        heapify(matriz, n, maior)
  
  
def heapSort(matriz):
    n = len(matriz)
    for i in range(n//2, -1, -1):
        heapify(matriz, n, i)
  
    for i in range(n-1, 0, -1):
        matriz[i], matriz[0] = matriz[0], matriz[i]
        heapify(matriz, i, 0)
  
matriz = []
for x in range(0, 10):
    add = int(input('Insira os valores (MAX 10): '))
    matriz.append(add)
print("\nValores desorganizados:")
print(matriz)
heapSort(matriz)
n = len(matriz)
print("\nValores organizados:")
print(matriz)

