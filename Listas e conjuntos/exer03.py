K = []
X = []
Y = []

for i in range(20):
    K.append(i)
    
for i in range(20):
    if i % 2 == 0:
        X.append(i)
    else:
        Y.append(i)
j = 0
l = 0
for i in range(20):
    if i % 2 == 0:
        K[i] = y[j]
        j += 1
    else:
        K[i] = x[l]
        l += 1
        
print(K)