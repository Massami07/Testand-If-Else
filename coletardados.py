import jogadores


def coletaDados():
    id = int(input("Qual o Id do jogador?"))
    nome = input("Qual é o nome do jogador?")
    vitorias = int(input("Quantas vitorias o jogador tem?"))
    jogador = jogadores.Jogadores(id, nome, vitorias)
    return jogador
