print("Informe o preço dos produtos \n Digite 0 para encerrar a compra")

def mercado():
    total = 0

    valor_produto = float(input("R$ "))

    while valor_produto != 0:
        total += valor_produto
        valor_produto = float(input("R$ "))

    return total

total_compra = mercado()

print(f"TOTAL R$ {total_compra:.2f}")