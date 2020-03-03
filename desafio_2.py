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
def jogo(nickname):
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
        print("Eu "+nickname+"tirei no primeiro dado: "+str(d1)+"\nE no segundo dado: "+str(d2)+"\n")
        rodada += 1
        if d1 == d2 and andando == True:
            preso = True
            andando = False
            ajuda = True
            
            print("man to preso na casa:" +str(pos)+"\n")

        elif d1 == d2 and preso == True and ajuda == False:
            preso = False
            print("O "+nickname+" pagou a propina pras pessoas certas e saiu da prisão\n")
        elif(d1 != d2 and preso == True):
            print("O "+nickname+" ta tentando sair mas estelionatario não sai tão rapido assim não\n")
        elif d1 != d2 and preso == False:
            pos = pos + (d1 + d2)
            if pos % 2 == 0:
                valor = valor + 79.99
            else:
                valor = valor + 53.21
            if pos >= len(tab):
                acabou = True
                print("tudo tem um fim e esse foi o fim do "+nickname+"\n")
            else:
                print("eu "+nickname+"estou na casa "+str(pos)+" com "+str(valor)+" reais\n")
        ajuda = False
    print("O jogador:" +nickname+" ganhou em :"+str(rodada)+" rodadas\nSeu montante é: "+str(valor)+"\n")

persongem1 = Thread(target=jogo,args=["*Bot1*"])
persongem2 = Thread(target=jogo,args=["*bot2*"])
persongem3 = Thread(target=jogo,args=["*bot3*"])
persongem4 = Thread(target=jogo,args=["*bott4*"])

persongem1.start()
persongem2.start()
persongem3.start()
persongem4.start()
