import numpy as np

valores = []
x = 5

vetor = np.zeros(x)

for i in range(x):
    vetor[i] = float(input("Digite um valor: "))
    if vetor[i] > 0:
        valores.append(vetor[i])
    
soma = sum(valores)

print(soma)