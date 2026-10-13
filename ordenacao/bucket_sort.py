# Bucket Sort - vai ordena os jogos pela nota que cada usuario colocou

def bucket_sort(jogos):

    comparacoes = 0  

    # os jogos sem nota vão ficar separados e vao pro final
    com_nota = []
    sem_nota = []
    for jogo in jogos:
        if jogo.user_score is None:
            sem_nota.append(jogo)
        else:
            com_nota.append(jogo)

    # cria 10 baldes vazios
    baldes = []
    for i in range(10):
        baldes.append([])

    # coloca cada jogo no balde certo
    for jogo in com_nota:
        indice = int(jogo.user_score)
        if indice == 10: 
            indice = 9
        baldes[indice].append(jogo)

    # vai ordena cada balde com insertion sort e junta no fianl
    resultado = []
    for balde in baldes:

        for i in range(1, len(balde)):
            atual = balde[i]
            j = i - 1
            while j >= 0:
                comparacoes += 1
                if balde[j].user_score > atual.user_score:
                    balde[j + 1] = balde[j]
                    j -= 1
                else:
                    break
            balde[j + 1] = atual

        for jogo in balde:
            resultado.append(jogo)

    for jogo in sem_nota:
        resultado.append(jogo)

    return {
        "lista": resultado,
        "comparacoes": comparacoes
    }
