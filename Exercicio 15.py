print("Calculadora de salário")
valores_h = float(input("Digite o valor do seu salário em hora:"))
horas_t = float(input("Quantas horas foram trabalhadas no mês:"))

salario_bruto = valores_h * horas_t
imposto_ir = salario_bruto * (11/100)
imposto_inss = salario_bruto * (8/100)
imposto_sind = salario_bruto * (5/100)
salario_liquido = salario_bruto - imposto_ir - imposto_inss - imposto_sind

print(f"===================================== \n|\n| Seu salário é R${salario_liquido}\n| Este é o valor dos descontos: \n| IR: R${imposto_ir}\n| INSS: R${imposto_inss}\n| Sindicato: R${imposto_sind}\n|\n=====================================")