peso_p = int(input("Digite o peso do peixe"))
peso_lei = 50

if peso_p > 50:
    conta = peso_p - peso_lei
    multa = conta * 4
    print("Você trouxe {}Kg de peixe acima do permitido, a sua multa é de R${}".format(conta, multa))
else:
    print("Você não execeu o limite de Kg permitido")
