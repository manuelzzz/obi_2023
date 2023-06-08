resp = 0
st = input()
tuneis = st.split(" ")

ligacoes = []
for i in range(0, int(tuneis[1])):
    ligacao = input().split(" ")
    ligacoes.append(ligacao)

t = int(input())
sugestoes = []

for i in range(0, t):
    ligSugestoes = input().split(" ")
    sugestao = []
    for i in range(1, len(ligSugestoes)):
        sugestao.append(ligSugestoes[i])
    sugestoes.append(sugestao)

for sugestao in sugestoes:
    possivel = 1

    for i in range(0, len(sugestao)):
        if i+1 < len(sugestao):
            possivel1 = [sugestao[i], sugestao[i+1]]
            possivel2 = [sugestao[i+1], sugestao[i]]

            for ligacao in ligacoes:
                if possivel1 == ligacao or possivel2 == ligacao:
                    possivel += 1

    if possivel == len(sugestao):
        resp += 1


print(resp)
