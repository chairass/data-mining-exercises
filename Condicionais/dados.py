import random

print('Gerando um número aleatório entre 1 e 6...')

numero = random.randint(1, 6)


print(f'O número gerado foi: {numero}')

jogador2 = random.randint(1, 6)

print(f'O número do jogador 2 é: {jogador2}')
if numero < jogador2:
    print("Você pode jogar a partida!")

else:
    print("Você não pode jogar a partida.")