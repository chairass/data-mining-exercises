print("Informe os valores encontrado")

def calcularMedia():
    # Criação de uma lista vazia que armazenará os valores digitados
    valores = []
    print("Digite os valores encontrados (em R$):")
    for i in range(5):
        # Solicita ao usuário um valor numérico
        # i + 1 é usado para começar a contagem em 1 (mais intuitivo para o usuário)
        numero = float(input(f"{i+1}° R$ "))
        # Adiciona o valor digitado à lista
        valores.append(numero)

    # Retorna a lista preenchida
    return valores

# Chamada da função para capturar os valores
valores = calcularMedia()

media = sum(valores) / len(valores)

def verificarPrecos(media, valores):
    return [v for v in valores if v > media]


valores_acima_media = verificarPrecos(media, valores)

# Cria uma nova representação formatada com R$ e duas casas decimais
# join() une os valores em uma única string separada por vírgula
valores_formatados = ", ".join(f"R$ {v:.2f}" for v in valores)

print("Valores encontrados: \n", valores_formatados)
print(f"O preço médio é de R$ {media:.2f}")
print("Valores acima da média: \n", ", ".join(f"R$ {v:.2f}" for v in valores_acima_media))  
