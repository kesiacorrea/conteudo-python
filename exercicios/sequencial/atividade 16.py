import math
area= float(input("informe a area a ser pintada: "))

cob_por_metro= 3
qtd_tinta_lata= 18
valor_lata=  80.0

litros_neceessarios= area/cob_por_metro
print("sao necessaios", litros_necessarios,"L de tinta")

qtd_latas= litros_necessarios/ qtd_tinta_lata
print("sao necessarios", qtd_latas,"latas de tinta")

print("### com o valor exato ###")
valor= qtd_latas * valor_lata
print("o valor necessario da tinta, é R$", round(valor,2))

print("### com quantidades inteiras de latas ###")
qtd_latas= math.ceil(qtd_latas)
print("sao necessarios", qtd_latas,"latas de tinta")
valor=qtd_latas * valor_lata
print("o valor necessario da tinta, é R$",valor)