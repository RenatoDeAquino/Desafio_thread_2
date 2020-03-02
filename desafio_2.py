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

from threading import Thread
import random
#inicio player 1[ninckname =  seu nome,valor = montante, = d1 e d2 = dados, tab = tabuleiro]
def jogo(nickname,valor,turno):
    tab = []
    pos = 0
    acabou = False
    preso = False
    andando = True
    ajuda = True
    rodada = 0
    valor = 0
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
            if pos % 2 == 0:
                montante = montante + 79.99
            else:
                montante = montante + 53.21
            if pos >= len(tab):
                acabou = True
                tab[len(tab)-1] = nickname
                print(tab)
            else:
                tab[pos] = nickname
                print(tab)
        ajuda = False
    print("O jogador:" +nickname+" ganhou em :"+str(rodada)+" rodadas\nSeu montante é: "+str(montante))
    return valor, rodada

persongem1 = Thread(target=jogo,args=["*Bot1*",0,0])
persongem2 = Thread(target=jogo,args=["*bot2*",0,0])
persongem3 = Thread(target=jogo,args=["*bot3*",0,0])
persongem4 = Thread(target=jogo,args=["*bott4*",0,0])

persongem1.start()
persongem2.start()
persongem3.start()
persongem4.start()
#implementação para checagem do mais rapido e do mais rico

#if persongem1.rodada < persongem2.rodada < persongem3.rodada < persongem4.rodada:
#    print("o persongame:"+persongem1.nickname+" foi mais rápido")
#elif persongem2.rodada < persongem1.rodada < persongem3.rodada < persongem4.rodada:
#    print("o persongame:"+persongem2.nickname+" foi mais rápido")
#elif persongem3.rodada < persongem1.rodada < persongem2.rodada < persongem4.rodada:
#    print("o persongame:"+persongem3.nickname+" foi mais rápido")
#elif persongem4.rodada < persongem1.rodada < persongem3.rodada < persongem2.rodada:
#    print("o persongame:"+persongem4.nickname+" foi mais rápido")
#if persongem1.valor > persongem2.valor > persongem3.valor > persongem4.valor:
#    print("o persongame:"+persongem1.nickname+" é o mais rico")


