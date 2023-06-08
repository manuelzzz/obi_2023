caixa = int(input())

valores = []
for i in range(0, 3):
    valores.append(int(input()))

resp = 0

if caixa - (valores[0]+valores[1]+valores[2]) >= 0:
    resp = 3
elif caixa-(valores[0]+valores[1]) >= 0 or caixa-(valores[1]+valores[2]) >= 0 or caixa-(valores[0]+valores[2]) >= 0:
    resp = 2
elif caixa-valores[0] >= 0 or caixa-valores[1] >= 0 or caixa-valores[2] >= 0:
    resp = 1

print(resp)