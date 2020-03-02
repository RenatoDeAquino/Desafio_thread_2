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
def jogo(nickname):
    tab = []
    pos = 0
    acabou = False
    preso = False
    andando = True
    ajuda = True
    rodada = 0
    for x in range(0,100):
        tab.append("[]")
    tab[0] = nickname
    print(tab)
    print(len(tab))
    while acabou == False:
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        rodada += 1
        if d1 == d2 and andando == True:
            preso = True
            andando = False
            ajuda = True
            print("man to preso")
        elif d1 == d2 and preso == True and ajuda == False:
            preso = False
            print("a liberdade cantou")
        elif d1 != d2 and preso == False:
            tab[pos] = "[]"
            pos = pos + (d1 + d2)
            if pos >= len(tab):
                acabou = True
                tab[len(tab)-1] = nickname
                print(tab)
            else:
                tab[pos] = nickname
                print(tab)
        ajuda = False
        print(rodada)

#falta colocar em threads agora

