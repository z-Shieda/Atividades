altura = float(input("Digite sua altura: \n(Exemplo 1.80)"))
print("Você se identifica como Homem ou Mulher ?")
sexo = input("Digite 1 para Homem e 2 para Mulher")

while True:
    if sexo == "1":
        f_homem = (72.7 * altura) - 58
        print("Seu peso ideal é {}".format(f_homem))
        break
    elif sexo == "2":
        f_mulher = (62.1 * altura) - 44.7
        print("Seu peso ideal é {}".format(f_mulher))
        break
    else:
        print("Opção errada, tente novamente")
        break
