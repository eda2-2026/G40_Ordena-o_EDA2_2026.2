# Quick Sort - Vai ordenar os jogos por nome em ordem alfabetica

comparacoes = 0  # contador de comparações


def particionar(lista, inicio, fim):
    global comparacoes

    # usamos o elemento do meio como pivo
    # (com o ultimo elemento dava problema quando a lista ja estava ordenada,
    # e o nosso csv ja vem em ordem alfabetica)
    meio = (inicio + fim) // 2
    lista[meio], lista[fim] = lista[fim], lista[meio]
    pivo = lista[fim].name.lower()

    i = inicio - 1
    for j in range(inicio, fim):
        comparacoes += 1
        if lista[j].name.lower() <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1


def ordenar(lista, inicio, fim):
    if inicio < fim:
        p = particionar(lista, inicio, fim)
        ordenar(lista, inicio, p - 1)
        ordenar(lista, p + 1, fim)


def quick_sort(jogos):
    global comparacoes
    comparacoes = 0

    lista = jogos[:]  # aqui vai copiar a lista pra nao mexer na lista original
    ordenar(lista, 0, len(lista) - 1)

    return {
        "lista": lista,
        "comparacoes": comparacoes
    }

