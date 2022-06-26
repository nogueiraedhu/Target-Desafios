import json

arquivo = open('dados.json')

dados = json.load(arquivo)

dias_mes = 0
dias_maior = 0
soma = 0
maior = 0

for i in dados:
    if (i['valor'] > 0):
        dias_mes += 1
        soma += i['valor']

    if (i['valor'] > maior):
        maior = i['valor']

media = soma/dias_mes
menor = maior

for i in dados:
    if (i['valor'] > media):
        dias_maior += 1

    if (i['valor'] < menor) and (i['valor'] != 0):
        menor = i['valor']

print(f'O maior valor de faturamento foi: {maior}')
print(f'O menor valor de faturamento foi: {menor}')
print(f'Houveram {dias_mes} dias com faturamento superior à média mensal.')

arquivo.close()