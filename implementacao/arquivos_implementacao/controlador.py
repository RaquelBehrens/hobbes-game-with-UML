
from tabuleiro import Tabuleiro
import random

class Controlador():
    def __init__(self):
        self._tabuleiro = Tabuleiro()
        self._jogadorDaVez = 0
        self._vencedores = []
        self._acao = ''
        self._partidaAndamento = False
        self._partidaEncerrada = False
        self._jogadaObrigatoriaRealizada = False
        self._flagJogada = False
        self.preencherTabuleiro()
        self.definirJogadorDaVez()
        self.setPartidaAndamento(True)

    def preencherTabuleiro(self):
        self._tabuleiro.criarTabuleiro()

    def definirJogadorDaVez(self):
        self._jogadorDaVez = random.randint(1, 2)

    def getPartidaEncerrada(self):
        return self._partidaEncerrada

    def setPartidaEncerrada(self, boolean):
        self._partidaEncerrada = boolean

    def getPosicoesTabuleiro(self):
        return self._tabuleiro.getMatrizPosicoes()

    def setPosicoesTabuleiro(self, matriz):
        self._tabuleiro.setMatrizPosicoes(matriz)

    def getPartidaAndamento(self):
        return self._partidaAndamento

    def determinarVencedor(self):
        if self._jogadorDaVez == 1:
            self._vencedores.append(2)
        else:
            self._vencedores.append(1)

        self._partidaEncerrada = True

    def verificarAcao(self, input):
        if input == 'w':
            self._acao = 'cima'
        elif input == 'a':
            self._acao = 'esquerda'
        elif input == 's':
            self._acao = 'baixo'
        elif input == 'd':
            self._acao = 'direita'
        elif input == 'p':
            self._acao = 'puxar'
        elif input == 'e':
            self._acao = 'empurrar'
        else:
            self._acao = ''

    def realizarJogada(self, input):
        self.verificarAcao(input)
        direcao = self.getDirecaoJogadorDaVez()

        #jogada opcional
        if (self._acao == 'cima') or(self._acao == 'direita') or (self._acao == 'esquerda') or (self._acao == 'baixo'):
            if self._acao == direcao:
                self.moverRei(self._jogadorDaVez, direcao)
            else:
                direcao = self._acao
                self.mudarDirecaoRei(self._jogadorDaVez, direcao)

        #jogada obrigatoria
        elif (self._acao == 'puxar') or (self._acao == 'empurrar'):
            if self._acao == 'puxar':
                self._jogadaObrigatoriaRealizada=self.puxarPeao(self._jogadorDaVez, direcao)
            else:
                self._jogadaObrigatoriaRealizada=self.empurrarPeao(self._jogadorDaVez, direcao)  #MUDAR DIAGRAMA DE SEQUENCIA DE PUXAR E 
                                                                                   #EMPURRAR PEAO POIS ELES DEVEM INFORMAR QUE NAO EH POSSIVEL REALIZAR MOVIMENTO
                                                                                   #ELES RETORNAM TRUE SE FOI POSSIVEL E FALSO CASO NAO FOI POSSIVEL

            if self._jogadaObrigatoriaRealizada:

                self.verificarVencedores(self._jogadorDaVez)
                vencedores = self._tabuleiro.getVencedores()

                if vencedores:
                    self._partidaEncerrada = True
                else:
                    self._jogadorDaVez = self.mudarJogadorDaVez(self._jogadorDaVez)
                    self._flagJogada = True
                    self._jogadaObrigatoriaRealizada = False
            else:
                self._flagJogada = False
        else:
            pass

    def getDirecaoJogadorDaVez(self):
        return self._tabuleiro.getDirecaoJogadorDaVez(self._jogadorDaVez)

    def moverRei(self, jogador, direcao):
        self._tabuleiro.moverPeca(jogador, direcao)

    def mudarDirecaoRei(self, jogador, direcao):
        self._tabuleiro.mudarDirecaoPeca(jogador, direcao)

    def puxarPeao(self, jogador, direcao):
        return self._tabuleiro.puxarPeao(jogador, direcao)

    def empurrarPeao(self, jogador, direcao):
        return self._tabuleiro.empurrarPeao(jogador, direcao)

    def verificarVencedores(self, jogador):
        self._tabuleiro.verificarEncerramentoDaPartida(jogador)

    def mudarJogadorDaVez(self, jogador):
        if jogador == 1:
            return 2
        else:
            return 1

    def getVencedores(self):
        return self._vencedores()

    def setPartidaAndamento(self,partida_iniciada):
        self._partidaAndamento = partida_iniciada

    def getJogadorDaVez(self):
        return self._jogadorDaVez

    def getPartidaEncerrada(self):
        return self._partidaEncerrada

    def setJogadaObrigatoriaRealizada(self,jogada_obrigatoria):
        self._jogadaObrigatoriaRealizada = jogada_obrigatoria

    def getJogadaObrigatoriaRealizada(self):
        return self._jogadaObrigatoriaRealizada

    def getFlagJogada(self):
        return self._flagJogada

    def getDirecaoJogador1(self):
        return self._tabuleiro._jogadorUm.getDirecaoJogador()
    def getDirecaoJogador2(self):
        return self._tabuleiro._jogadorDois.getDirecaoJogador()
