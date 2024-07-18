import numpy as np

x = 4

vetor = np.zeros(x)

for i in range(x):
    vetor[i] = float(input("Digite um valor: "))

menor = min(vetor)
maior = max(vetor)
posMenor = vetor.argmin()
posMaior = vetor.argmax()

print("O menor valor é: ", menor)
print("Sua posição: ", posMenor)  

print("\n")

print("O maior valor é: ", maior)
print("Sua posição: ", posMaior)  
