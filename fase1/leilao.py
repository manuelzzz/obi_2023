pessoas = int(input())
nomes = []
numeros = []

for i in range(0, pessoas):
    nomes.append(input())
    numeros.append(int(input()))

resp = 0
for i in range(0, len(numeros)):
    if i+1 < len(numeros):
        if numeros[i] > numeros[i+1] and numeros[i] > numeros[resp]:
            resp = i
        elif numeros[i+1] > numeros[resp]:
            resp = i+1

print(nomes[resp])
print(numeros[resp])