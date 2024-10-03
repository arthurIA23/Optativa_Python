m = [[0 for _ in range(5)] for _ in range(5)]

valores = input("Digite os valores da matriz separados por vírgula: ").split(',')

valores = [int(valor) for valor in valores]

index = 0
for coluna in range(5):
    for linha in range(5):
        m[linha][coluna] = valores[index]
        index += 1

for linha in m:
    print(' '.join(map(str, linha)))