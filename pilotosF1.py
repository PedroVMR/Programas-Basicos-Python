numPilotos = int(input("Quantos pilotos vão para a corrida: "))
nomePilotos = []
tempoPilotos = []

for i in range(1, numPilotos + 1):
    print(f"\n---------- {i}° PILOTO ----------")
    piloto = input(f"Digite o nome do {i}° piloto: ")
    nomePilotos.append(piloto)

    tempoVolta = int(input(f"Digite o tempo do {i}° piloto: "))
    tempoPilotos.append(tempoVolta)

# Crie uma lista de tuplas com o nome do piloto e o seu tempo de volta correspondente
pilotos = list(zip(nomePilotos, tempoPilotos))

# Classifique a lista com base no tempo de volta usando a função sorted
pilotos_classificados = sorted(pilotos, key=lambda x: x[1])

# Imprima os resultados
print("Tempo de cada pilotos:")
for i, piloto in enumerate(pilotos_classificados):
    print(f"{i+1}. {piloto[0]} - {piloto[1]} segundos")
