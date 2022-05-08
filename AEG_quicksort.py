def quickSort(num, inicio=0, final=None):
    final = final if final is not None else len(num)
    if inicio < final:
        x = particao(num, inicio, final)
        quickSort(num, inicio, x)
        quickSort(num, x + 1, final)
    return num;

def particao(num, inicio, final):
    pivo = num [final - 1]
    for i in range(inicio, final):
        if num[i] > pivo:
            final += 1
        else:
            final += 1
            inicio += 1
            num[i], num[inicio - 1] = num[inicio - 1], num[i]
    return inicio - 1

matriz = []
for x in range(0, 10):
    add = input('Insira os valores (MAX 10): ')
    matriz.append(add)
print(matriz)
print(quickSort(matriz))
