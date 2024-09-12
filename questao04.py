
faturamento_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

valorTotal = faturamento_mensal["SP"] + faturamento_mensal["RJ"] + faturamento_mensal["MG"] + faturamento_mensal["ES"] + faturamento_mensal["Outros"]
print("Percentual de representação de cada estado:")
for estado in faturamento_mensal:
    valor = faturamento_mensal[estado]
    percentual = (valor / valorTotal) * 100
    print(f"{estado}: {percentual:.2f}%")