import rankeamento
import coletardados


jogador = coletardados.coletaDados()
rankeamento.rankear(jogador.nome, jogador.vitorias)
