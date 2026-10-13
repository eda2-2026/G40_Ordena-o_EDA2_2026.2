# Merge Sort - vai ordenar os jogos pelas vendas totais do que foi mais vendido para o menor vendido

comparacoes = 0 

def dividir_e_juntar(lista):
    global comparacoes

    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = dividir_e_juntar(lista[:meio])
    direita = dividir_e_juntar(lista[meio:])

    # junta as duas metades 
    resultado = []
    i = 0
    j = 0
    while i < len(esquerda) and j < len(direita):
        comparacoes += 1
        # o >= faz o merge se possivel, caso for empate é para pegar o da esquerda primeiro
        if esquerda[i].total_sales >= direita[j].total_sales:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # o que sobrou de cada lado
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1
    while j < len(direita):
        resultado.append(direita[j])
        j += 1

    return resultado


def merge_sort(jogos):
    global comparacoes
    comparacoes = 0

    lista = dividir_e_juntar(jogos)

    return {
        "lista": lista,
        "comparacoes": comparacoes
    }
