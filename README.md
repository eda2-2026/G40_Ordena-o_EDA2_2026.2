# G40_Ordenacao_EDA2_2026.2
Repositório dedicado ao Trabalho 2 de Estruturas de Dados 2 do 2º semestre de 2026.

O projeto tem como objetivo implementar e analisar diferentes **algoritmos de ordenação**, utilizando como base uma tabela contendo informações sobre jogos.

## Alunos

| Matrícula | Nome |
| --- | --- |
| 202023805 | João Paulo Barros de Cristo |

**Disciplina:** Estrutura de Dados 2  
**Professor:** Mauricio Serrano  
**Semestre:** 2026.2

---

## 🎯 Objetivo

O objetivo deste projeto é implementar quatro algoritmos de ordenação estudados na disciplina de Estruturas de Dados 2, utilizando uma base de dados de jogos como conjunto de dados para os testes.

Cada algoritmo foi aplicado sobre o atributo do jogo que mais combina com a sua forma de funcionar, e os algoritmos são comparados considerando:

- Funcionamento;
- Quantidade de comparações;
- Tempo de execução.

---

## 🎮 Base de Dados

A aplicação utiliza o arquivo `dados/csv de jogos.csv`, com **1000 jogos** e informações como nome, ano de lançamento, plataforma, vendas por região e notas da crítica e dos usuários.

Alguns registros possuem dados faltando (`NULL`, `N/A` ou `tbd`). Esses jogos não entram na ordenação do campo que está faltando e são colocados no final da lista.

---

## 📊 Algoritmos de Ordenação

| Algoritmo | Campo ordenado | Por que esse campo | Complexidade | Status |
| --- | --- | --- | --- | --- |
| Counting Sort | Ano de lançamento | Inteiros em um intervalo pequeno (1980 a 2016) | O(n + k) | ✅ Implementado |
| Bucket Sort | Nota dos usuários | Valores decimais distribuídos de 0 a 10 (um balde por ponto) | O(n + k) no caso médio | ✅ Implementado |
| Quick Sort | Nome do jogo | Ordenação geral de texto (ordem alfabética) | O(n log n) médio / O(n²) pior caso | ✅ Implementado |
| Merge Sort | Vendas totais | Algoritmo estável: jogos com vendas iguais mantêm a ordem | O(n log n) | ✅ Implementado |

---

## 🗂️ Estrutura do Projeto

```text
G40_Ordenacao_EDA2_2026.2/
│
├── README.md
├── main.py
├── dados/
│   └── csv de jogos.csv
├── modelos/
│   └── jogos.py
├── utils/
│   └── carregador.py
│
└── ordenacao/
    ├── counting_sort.py
    ├── bucket_sort.py
    ├── quick_sort.py
    └── merge_sort.py
```

---

## ▶️ Como Executar

Não é necessário instalar nenhuma biblioteca externa. Na pasta do projeto, execute:

```bash
python main.py
```

O programa mostra um menu para escolher o algoritmo. A opção **5** roda todos e mostra uma tabela comparando o número de comparações e o tempo de cada um.

---

## 🚧 Status do Projeto

Atualmente, foram implementados:

- ✅ Counting Sort
- ✅ Bucket Sort
- ✅ Quick Sort
- ✅ Merge Sort

## Apresentação

[(link do vídeo)](https://youtu.be/3OJVAf5S_j8)]
