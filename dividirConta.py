print("Informe o valor da conta e a quantidade de pessoas na mesa")

valor_conta = float((input("Valor da conta R$\n")))
qtd_pessoas = float((input("Informe a quantidade de pessoas: ")))

def dividirConta(valor_conta, qtd_pessoas):
    valor_por_pessoa = valor_conta / qtd_pessoas

    return valor_por_pessoa

valor = dividirConta(valor_conta, qtd_pessoas)

print(f"O valor de unitário é de R$ {valor:.2f}")