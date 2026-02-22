print("Bem-vindos ao Bar do Boca\nTemos uma taxa fixa do couvert de R$ 8,00.\nInforme o valor total da conta para adicionar os 20% do garçom")
valorTotal = float(input("Valor Total: \n"))

def calcularValor(valorTotal):
    taxa_garçom = valorTotal *0.20
    couvert = 8
    valorFinal = valorTotal + couvert + taxa_garçom

    return taxa_garçom, valorFinal

taxa, valor = calcularValor(valorTotal)


print(f"\nPorcentagem Garçom R$ {taxa:.2f}\nValor Total R$ {valor:.2f}")    