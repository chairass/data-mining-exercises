print("Informe um numero de 1 a 13 para escolher uma carta do baralho: ")

numero_carta = int(input())
if numero_carta == 1:
    print("Ás")

if numero_carta == 11:
    print("Valete")

if numero_carta == 12:
    print("Dama")  

if numero_carta == 13:
    print("Rei")        

if numero_carta > 1 and numero_carta < 11:
    print("Carta: ", numero_carta)
    