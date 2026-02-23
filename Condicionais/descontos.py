print("Veja os descontos disponíveis de a" \
"Até de R$ 50,00 5% de desconto" \
"De R$ 50,01 a R$ 100,00 10% de desconto " \
"De 100,01 a R$ 200,00 20% de desconto" \
"De 200,01 a R$ 500,00 20% de desconto"
"Acima de R$ 500,00 30% de desconto")

print("Informe o valor da compra:")
valor_compra = float(input())

def calcular_desconto(valor):
    if valor <= 50:
        desconto = valor * 0.05
    elif valor <= 100:
        desconto = valor * 0.10
    elif valor <= 200:
        desconto = valor * 0.20
    elif valor <= 500:
        desconto = valor * 0.20
    else:
        desconto = valor * 0.30
    
    return desconto

desconto = calcular_desconto(valor_compra)
valor_final = valor_compra - desconto

print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_final:.2f}")