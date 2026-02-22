print("Para calcular a velocidade por hora informe a distancia e o tempo.")

# Solicita ao usuário a distância em metros
distancia = float(input("Ditancia(metros): "))
# Solicita ao usuário o tempo em horas
tempo = float(input("Tempo(horas): "))

# Definição da função responsável pelo cálculo
def calcularDistancia(distancia, tempo):
    distancia_km = distancia / 1000  # converte metros para km
    velocidade = distancia_km / tempo

    return velocidade, distancia_km

# A função retorna dois valores (tupla)
# Cada variável recebe um deles
distancia, velocidade = calcularDistancia(distancia, tempo)


# Impressão formatada usando f-string e string multilinha (""" """)
# :.2f formata para duas casas decimais
print(f"""
Distância percorrida: {distancia:.2f} km
Velocidade média: {velocidade:.2f} km/h
""")