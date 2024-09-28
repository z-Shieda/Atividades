genero = input("Você pertence ao grupo F (feminino) ou M (masculino) ?")
genero_r = (genero.lower())

if  genero_r == "f" :
    print("Você faz parte do grupo feminino")
elif genero_r == "m" :
    print("Você faz parte do grupo masculino")
else:
    print("Grupo inválido")
