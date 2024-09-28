tamanho_d = int(input("Informe o tamanho do Download em MB"))
velocidade = int(input("Agora informe a velocidade da sua internet em Mbps"))

tempo = tamanho_d / velocidade / 8

print(f"O Tempo necessário para o Download é de: {tempo} segundos")

