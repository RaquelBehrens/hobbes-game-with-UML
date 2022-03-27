from tkinter import *
from controlador import Controlador
import os
import sys

BASE_DIR = os.path.realpath(os.path.dirname(sys.argv[0]))

class Interface():
    def __init__(self) -> None:
        self._janela = Tk()
        self._partidaAndamento = False
        self._controlador = None
        self._mainFrame = Frame(self._janela,width=520,height=420, bg="white")
        self._buttonFrame = Frame(self._janela,width=520,height=100,bg='green')
        self._mensagem = Frame(self._janela,width=520,height=70, bg="lightgrey")
        self._vazio = PhotoImage(file = os.path.join(BASE_DIR, "imagens", "vazio.png"))
        self._rei_1_d = PhotoImage(file = os.path.join(BASE_DIR, "imagens", "rei_1_direita.png"))
        self._rei_1_e = PhotoImage(file = os.path.join(BASE_DIR, "imagens", "rei_1_esquerda.png"))
        self._rei_1_b = PhotoImage(file = os.path.join(BASE_DIR, "imagens", "rei_1_baixo.png"))
        self._rei_1_c = PhotoImage(file = os.path.join(BASE_DIR, "imagens", "rei_1_cima.png"))
        self._rei_2_d = PhotoImage(file = os.path.join(BASE_DIR, "imagens", "rei_2_direita.png"))
        self._rei_2_e = PhotoImage(file = os.path.join(BASE_DIR, "imagens", "rei_2_esquerda.png"))
        self._rei_2_b = PhotoImage(file = os.path.join(BASE_DIR, "imagens", "rei_2_baixo.png"))
        self._rei_2_c = PhotoImage(file = os.path.join(BASE_DIR, "imagens", "rei_2_cima.png"))
        self._peao = PhotoImage(file = os.path.join(BASE_DIR, "imagens", "peao.png"))

    def fillMainWindow(self):
        self._janela.title("UM PEGA-PEGA ENTRE REIS")
        self._janela.iconbitmap(os.path.join(BASE_DIR, "imagens", "coroa_icon.ico"))
        self._janela.geometry("770x730")
        self._janela.resizable(False, False)
        self._janela["bg"]="lightgrey"

        self._mainFrame.place(x=110,y=200)
        self._buttonFrame.place(x=200, y=13)
        self._mensagem.place(x=185,y=120)

        botao_iniciar = Button(self._buttonFrame,text = "INICIAR",height = 4,width = 15,command=lambda:self.iniciarJogo(''))
        botao_desistir = Button(self._buttonFrame,text = "DESISTIR",height = 4,width = 15,command=self.desistirJogo)
        botao_sair_jogo = Button(self._buttonFrame,text = "SAIR DO JOGO",height = 4,width = 15,command=self._janela.destroy)
        botao_iniciar.grid(row= 0, column=0)
        botao_desistir.grid(row= 0, column=1)
        botao_sair_jogo.grid(row= 0, column=2)

        self._janela.bind('w', lambda event: self.atualizaInterface('w'))
        self._janela.bind('a', lambda event: self.atualizaInterface('a'))
        self._janela.bind('s', lambda event: self.atualizaInterface('s'))
        self._janela.bind('d', lambda event: self.atualizaInterface('d'))
        self._janela.bind('e', lambda event: self.atualizaInterface('e'))
        self._janela.bind('p', lambda event: self.atualizaInterface('p'))

        self._janela.mainloop()

    def iniciarJogo(self, acao):
        if not self._partidaAndamento:
            self._controlador = Controlador()
            self._partidaAndamento = True
        self.atualizaInterface(acao)

    def desistirJogo(self  ):

        if self._partidaAndamento:
            self._controlador.setPartidaEncerrada(True)

            if (self._controlador._jogadorDaVez == 1):
                self._controlador._jogadorDaVez = 2
            else:
                self._controlador._jogadorDaVez = 1
            self.atualizaInterface('')

        else:
            self.mostrarLabels('nao_andamento')

    def realizarJogada(self, acao):
        self._controlador.realizarJogada(acao)

    def mostrarLabels(self, acao):
        labelInstrucao = Label(self._mensagem, text='                           ' , font="Courier 21",bg = "lightgrey")
        labelInstrucao.grid(row=0, column=0)

        if (acao == 'e' or acao == 'p') and (self._controlador.getFlagJogada() == False):
            labelInstrucao = Label(self._mensagem, text='Jogada inválida' , font="Courier 21")
            labelInstrucao.grid(row=0, column=0)

        elif acao == 'nao_andamento':
            labelInstrucao = Label(self._mensagem, text='Partida nao esta em andamento' , font="Courier 15")
            labelInstrucao.grid(row=0, column=0)

    def mostrarTabuleiro(self):
        for y in range(5):
            for x in range(5):
                if self._controlador.getPosicoesTabuleiro() [x][y] == 0:
                    labelvazio = Label(self._mainFrame, bd = 2, relief="solid", image = self._vazio)
                    xLabel = labelvazio
                elif self._controlador.getPosicoesTabuleiro()  [x][y] == 3:
                    labelPeao = Label(self._mainFrame, bd = 2, relief="solid", image = self._peao)
                    xLabel = labelPeao
                elif self._controlador.getPosicoesTabuleiro()  [x][y] == 1:

                    imagem_r1 = self.atualiza_imagem_rei(self._controlador.getDirecaoJogador1(),1)
                    labelReiUm = Label(self._mainFrame, bd = 2, relief="solid", image = imagem_r1)
                    xLabel = labelReiUm
                else:
                    imagem_r2 = self.atualiza_imagem_rei(self._controlador.getDirecaoJogador2(),2)
                    labelReiDois = Label(self._mainFrame, bd = 2, relief="solid", image = imagem_r2)
                    xLabel = labelReiDois

                xLabel.grid(row=x , column=y)


    def atualiza_imagem_rei(self,direcao,jogador):
        if jogador == 1:
            if direcao == 'cima':
                return self._rei_1_c
            elif direcao == 'baixo':
                return self._rei_1_b
            elif direcao == 'direita':
                return self._rei_1_d
            else:
                return self._rei_1_e

        else:
            if direcao == 'cima':
                return self._rei_2_c
            elif direcao == 'baixo':
                return self._rei_2_b
            elif direcao == 'direita':
                return self._rei_2_d
            else:
                return self._rei_2_e

    def atualizaInterface(self,acao):
        partidaAndamento = self._controlador.getPartidaAndamento()
        if partidaAndamento:
            self.realizarJogada(acao)
            self.mostrarLabels(acao)

            partidaEncerrada = self._controlador.getPartidaEncerrada()
            if partidaEncerrada:
                if self._controlador._jogadorDaVez == 1:
                    texto = 'Jogador dourado venceu!'
                else:
                    texto = 'Jogador prata venceu!'
                labelInstrucao = Label(self._mensagem, text=texto , font="Courier 21")
                labelInstrucao.grid(row=0, column=0)
                self._controlador.setPosicoesTabuleiro(matriz = [[0,0,0,0,0],
                                                            [0,0,0,0,0],
                                                            [0,0,0,0,0],
                                                            [0,0,0,0,0],
                                                            [0,0,0,0,0]])
                self._partidaAndamento = False
            
            self.mostrarTabuleiro()
            