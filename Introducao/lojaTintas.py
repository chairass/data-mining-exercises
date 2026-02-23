print("Informe a area a ser pintada em metros quadrados:")
area = float(input())

def calcular_tinta(area):
    latas = 18
    galao = 3.6
    cobertura = 6

    litros_necessarios = (area / cobertura) * 1.1  # Adiciona 10% de folga

    latas_necessarias = litros_necessarios // latas
    litros_restantes = litros_necessarios % latas

    galao_necessarios = litros_restantes // galao
    litros_restantes = litros_restantes % galao 

    if litros_restantes > 0:
        galao_necessarios += 1 
    
    return latas_necessarias, galao_necessarios

latas, galao = calcular_tinta(area)

def calcular_custo(latas, galao):    
    custo_lata = 80
    custo_galao = 25

    custo_total = (latas * custo_lata) + (galao * custo_galao)
        
    return custo_total
    

custo_total = calcular_custo(latas, galao)
    
print(f"Serão necessárias {int(latas)} latas de 18 litros e "
      f"{int(galao)} galões de 3.6 litros para pintar "
      f"{area:.2f} metros quadrados.\n"
      f"Custo total: R$ {custo_total:.2f}")



    