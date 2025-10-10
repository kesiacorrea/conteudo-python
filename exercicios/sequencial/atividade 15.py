valor_hora= float(input("digite o seu valor/hora: "))
qtd_horas= int(input("digite quantas horas voce trabalhou: "))

ir= 0.11
inss= 0.08
sindicato= 0.05

salario_bruto= valor_hora * qtd_horas

valor_ir= salario_bruto * ir
valor_inss= salario_bruto * inss
valor_sindicato= salario_bruto * sindicato

salario_liquido= salario_bruto - valor_ir - valor_inss - valor_sindicato

print("salario bruto:", salario_bruto)
print("desconto ir: ",valor_ir)
print("desconto inss:",valor_inss)
print("desconto sindicato:", valor_sindicato)
print("salario liquido:", salario_liquido)