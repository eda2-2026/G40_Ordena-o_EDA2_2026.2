import random
import time

from utils.carregador import carregar_dados
from ordenacao.counting_sort import counting_sort
from ordenacao.bucket_sort import bucket_sort
from ordenacao.quick_sort import quick_sort
from ordenacao.merge_sort import merge_sort

caminho_arquivo = 'dados/csv de jogos.csv'

jogos_listados = carregar_dados(caminho_arquivo)

print(f"Total de jogos carregados: {len(jogos_listados)}")

# o csv ja vem em ordem alfabetica, entao embaralhamos antes de ordenar
random.shuffle(jogos_listados)

print("\nPrimeiros 5 jogos (embaralhados):")
for jogo in jogos_listados[:5]:
    print(jogo)


while True:
    print("\n===== ORDENAÇÃO DE JOGOS =====")
    print("1 - Counting Sort (por ano de lançamento)")
    print("2 - Bucket Sort (por nota dos usuários)")
    print("3 - Quick Sort (por nome)")
    print("4 - Merge Sort (por vendas totais)")
    print("5 - Rodar todos e comparar")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "0":
        break

    elif opcao == "1":
        inicio = time.time()
        resultado = counting_sort(jogos_listados)
        fim = time.time()
        print("\n10 jogos mais antigos:")
        for jogo in resultado["lista"][:10]:
            print(jogo)

    elif opcao == "2":
        inicio = time.time()
        resultado = bucket_sort(jogos_listados)
        fim = time.time()
        # os jogos sem nota ficam no fim, entao pegamos so os que tem nota
        com_nota = [jogo for jogo in resultado["lista"] if jogo.user_score is not None]
        print("\n10 jogos com maior nota dos usuários:")
        for jogo in com_nota[::-1][:10]:
            print(jogo)

    elif opcao == "3":
        inicio = time.time()
        resultado = quick_sort(jogos_listados)
        fim = time.time()
        print("\n10 primeiros jogos em ordem alfabética:")
        for jogo in resultado["lista"][:10]:
            print(jogo)

    elif opcao == "4":
        inicio = time.time()
        resultado = merge_sort(jogos_listados)
        fim = time.time()
        print("\n10 jogos mais vendidos:")
        for jogo in resultado["lista"][:10]:
            print(jogo)

    elif opcao == "5":
        algoritmos = [
            ("Counting Sort", "ano", counting_sort),
            ("Bucket Sort", "nota usuário", bucket_sort),
            ("Quick Sort", "nome", quick_sort),
            ("Merge Sort", "vendas", merge_sort),
        ]
        print(f"\n{'Algoritmo':<15}{'Campo':<15}{'Comparações':>12}{'Tempo (ms)':>12}")
        for nome, campo, funcao in algoritmos:
            inicio = time.time()
            resultado = funcao(jogos_listados)
            fim = time.time()
            print(f"{nome:<15}{campo:<15}{resultado['comparacoes']:>12}{(fim - inicio) * 1000:>12.3f}")
        continue

    else:
        print("Opção inválida.")
        continue

    print(f"\nTotal de comparações realizadas: {resultado['comparacoes']}")
    print(f"Tempo: {(fim - inicio) * 1000:.3f} ms")
