A = set()

for i in range(5):
    A.add(i)
    
B = set()

for i in range(10):
    A.add(int(input("Digite um número para a aposta: ")))
    
C = A & B

print("Voce acertou", len(C), "números")