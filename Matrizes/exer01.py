matriz = []
for i in range(5):
    linha = []
    for x in range(5):
        valor = int(input(f"Digite o valor para a posição [{i}][{x}]: "))
        linha.append(valor)
    matriz.append(linha)

print("Matriz digitada:")
for linha in matriz:
    for valor in linha:
        print(f"{valor:4}", end=" ")
    print()
