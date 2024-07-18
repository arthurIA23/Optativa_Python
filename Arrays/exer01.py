import numpy as np

x = 10

vetor = np.zeros(x)

for i in range(x):
    vetor[i] = float(input("Digite um valor: "))

print(vetor)