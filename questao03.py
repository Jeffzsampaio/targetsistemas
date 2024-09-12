


faturamentoDiario = [1000, 2000, 0, 3000, 0, 0, 4000, 5000, 0, 6000]
diasComFaturamento = []
for valor in faturamentoDiario:
    if valor > 0:
        diasComFaturamento.append(valor)
if diasComFaturamento:
    menorValor = diasComFaturamento[0]
    maiorValor = diasComFaturamento[0]
    for valor in diasComFaturamento:
     if valor < menorValor:
        menorValor = valor
     if valor > maiorValor:
        maiorValor = valor
soma = 0
for valor in diasComFaturamento:
    soma += valor
mediaMensal = soma / len(diasComFaturamento)+1

diasAcimaDaMedia = 0
for valor in diasComFaturamento:
    if valor > mediaMensal:
        diasAcimaDaMedia += 1


print(f"Faturamento Diario {faturamentoDiario}")
print(f"Dias Com Faturamento {diasComFaturamento}")
print(f"Menor valor de faturamento: {menorValor}")
print(f"Maior valor de faturamento: {maiorValor}")
print(f"Número de dias com faturamento acima da média: {diasAcimaDaMedia}")
