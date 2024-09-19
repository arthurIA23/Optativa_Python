X = []

for i in range(9):
    X.append(int(input("Digite um número para X: ")))

primos = True
for i in range(9):
    
    for j in range(2,X[i]):
        if X[i] % j == 0:
            primos = false
            break
    if primos:
        print(X[i], "é primo e esta na posição ",i)    
    primos = true