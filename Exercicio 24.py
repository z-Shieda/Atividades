print("Comparador de precos")

produto1 = float(input("Informe o preço do produto 1"))
produto2 = float(input("Informe o preço do produto 2"))
produto3 = float(input("Informe o preço do produto 3"))


lista = [produto1,produto2,produto3]

mais_caro = max(lista)
mais_barato = min(lista)

comp_preco = mais_caro - mais_barato

print(f"Foi feita uma análise de preços e: \nO Produto mais barato custa R${mais_barato} \nE o produto mais caro custa R${mais_caro} \nA Diferença de preco entre esses dois é de R${comp_preco}")