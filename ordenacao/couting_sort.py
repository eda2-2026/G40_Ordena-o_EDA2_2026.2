# Counting Sort - vai ordenar os jogos pelos ano de lancamento

def counting_sort(jogos):

    comparacoes = 0 

    # os jogos que não tiverem ano, vão ficar separados e vão pro final
    com_ano = []
    sem_ano = []
    for jogo in jogos:
        if jogo.year_of_release is None:
            sem_ano.append(jogo)
        else:
            com_ano.append(jogo)

    if len(com_ano) == 0:
        return {"lista": sem_ano, "comparacoes": comparacoes}

    # acha o menor e o maior ano e separa
    menor = com_ano[0].year_of_release
    maior = com_ano[0].year_of_release
    for jogo in com_ano:
        comparacoes += 2
        if jogo.year_of_release < menor:
            menor = jogo.year_of_release
        if jogo.year_of_release > maior:
            maior = jogo.year_of_release

    # vetor de contagem
    tamanho = maior - menor + 1
    contagem = []
    for i in range(tamanho):
        contagem.append(0)

    # conta quantos jogos tem em cada ano
    for jogo in com_ano:
        contagem[jogo.year_of_release - menor] += 1

    # soma acumulada 
    for i in range(1, tamanho):
        contagem[i] = contagem[i] + contagem[i - 1]

    resultado = []
    for i in range(len(com_ano)):
        resultado.append(None)

    i = len(com_ano) - 1
    while i >= 0:
        ano = com_ano[i].year_of_release
        contagem[ano - menor] -= 1
        resultado[contagem[ano - menor]] = com_ano[i]
        i -= 1

    for jogo in sem_ano:
        resultado.append(jogo)

    return {
        "lista": resultado,
        "comparacoes": comparacoes
    }
