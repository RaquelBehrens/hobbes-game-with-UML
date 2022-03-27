class Jogador():
    def __init__(self, id:int, posicao, direcaoAtual:str) -> None:
        self._id = id
        self._posicao = posicao
        self._direcaoAtual = direcaoAtual

    def getDirecaoJogador(self):
        return self._direcaoAtual

    def mudarDirecaoJogador(self, direcao):
        self._direcaoAtual = direcao

