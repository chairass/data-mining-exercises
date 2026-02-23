print("Informe um numero para ver a tabuada do mesmos:")

num = int(input())

def tabuada(num):
    return[f"{num} x {i} = {num * i}" for i in range(1, 11)]
    
resultado = tabuada(num)

for linha in resultado:
    print(linha)

