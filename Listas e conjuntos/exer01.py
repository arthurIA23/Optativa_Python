A = set()
B = set()

for i in range(5):
    A.add(float(input("Digite um número para A: ")))
    
for i in range(5):
    B.add(float(input("Digite um número para B: ")))
    
C = A & B
print("A:", A)
print("B:", B)
print("C:", C)
    