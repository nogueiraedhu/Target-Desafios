print('Percentual por estado:')

faturamento = [
    ['SP', 67836.43],
    ['RJ', 36678.66],
    ['MG', 29229.88],
    ['ES', 27165.48],
    ['Outros', 19849.53]
]

total = 0

for i in range(0, 5):
    total += faturamento[i][1]

for i in range(0, 5):
    porc = (faturamento[i][1] * 100) / total
    print(f'{faturamento[i][0]} representa aproximadamente {round(porc, 2)}%.')
