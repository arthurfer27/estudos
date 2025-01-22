
def jogador(jog='<desconhecido>', gol=0):
    print(f"O jogador {jog} fez {g} gol(s) no campeonato.")

n=input("Nome do jogador: ").title()
g=input("Número de gols: ")
if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip() == "":
    jogador(gol=0)
else:
    jogador(n,g)
