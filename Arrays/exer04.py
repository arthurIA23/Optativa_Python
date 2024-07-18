import numpy as np

valores = []
x = 5

vetor = np.zeros(x)

for i in range(x):
    vetor[i] = float(input("Digite um valor: "))

menor = min(vetor)
maior = max(vetor)

print("O menor valor é: ", menor)
print("O maior valor é: ", maior)