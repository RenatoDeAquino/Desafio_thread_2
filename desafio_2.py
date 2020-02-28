#tabuleiro
#numero de casas = 100
#numero de jogadores = 4
#cada jogador possui 2 d6
#jogador começa com 0 reais
#regra 1: se o jogador tirar numeros iguais nos dados ele fica preso
#somente saindo caso tire novamente o dado porém só pode sair na próxima rodada
#a cada vez que ele fizer uma ação deverá ser impresso seu nome,numero dos dados,total dinheiro e 
# status no jogo
#status: andando,preso,punido,libertado
#o jogo termina quando todos chegarem na casa de numero 100
#quando terminar imprimir o nome do jogador, total de jogadas e o valor arrecadado
#marcar o jogador mais rapido e o mais rico


import random
#inicio player 1[ninckname =  seu nome,valor = montante, = d1 e d2 = dados, tab = tabuleiro]
def player1(self,nickname,valor,d1,d2,tab):
    #declaração de variaveis
    self.nickname = nickname
    self.valor = valor
    self.d1 = d1
    self.d2 = d2
    self.tab = []
    game_end = False
    livre = True
    nickname = "Ash"
    valor = 0
    jogadas = 0
    game_crash = 0
    #criação do tabuleiro
    for x in range (0,100):
        self.tab.append("[ ]")
    #o jogo em si
    while game_end == True:
        if game_crash < 101:
            if livre == True:
                d1 = random.randint(1,6)
                d2 = random.randint(1,6)
                if d1 == d2:
                    print(""+nickname+" fui preso por tirar no d1:"+d1+" e no d2:"+d2+"\nstatus: Preso\n dinheiro:"+valor) 
                            
def player2(self,nickname,valor,d1,d2,tab):
    pass
def player3(self,nickname,valor,d1,d2,tab):
    pass

 

