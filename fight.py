from random import randint
from time import sleep


# Criaçõo de Barras de Energia
def barra_de_energia_cinza(qtd):
    print("\033[1;37m█\033[m" * qtd)


lutadores_lista_dic = [
    {"Nome": "Máximus", "Força": 5, "Dextreza": 8, "Velocidade": 3, "Energia": 100},
    {"Nome": "Commodus", "Força": 4, "Dextreza": 4, "Velocidade": 9, "Energia": 100},
    {"Nome": "Khal Drogo", "Força": 8, "Dextreza": 4, "Velocidade": 3, "Energia": 100},
    {"Nome": "Ryu", "Força": 9, "Dextreza": 5, "Velocidade": 4, "Energia": 100},
    {"Nome": "Ken", "Força": 8, "Dextreza": 4, "Velocidade": 5, "Energia": 100},
    {"Nome": "Aragorn", "Força": 4, "Dextreza": 9, "Velocidade": 6, "Energia": 100},
    ]



def linha_1_personalizavel(texto):
    tamanho = len(texto) + 6
    print(f"{'*' * tamanho}")
    print(f"   {texto}")
    print(f"{'*' * tamanho}")


def linha_2_personalizavel(texto):
    print("{}{}{}".format("*"*3, texto, "*"*3))


def gerador_ataque(força, velocidade):
    golpe_inicial = randint(0, 10)
    força_do_golpe = int(((força + velocidade) * golpe_inicial) / 10 )

    if 1 <= golpe_inicial <= 3:
        print(f"Força do golpe : {golpe_inicial}. Será causado um dano baixo.")
        print(f"Dano baixo causado : {força_do_golpe}")
        return força_do_golpe

    elif 4 <= golpe_inicial <= 7:
        print(f"Força do golpe : {golpe_inicial}. Será causado um dano razoável.")
        print(f"Dano razoável causado : {força_do_golpe}")
        return força_do_golpe

    elif 8 <= golpe_inicial <= 9:
        print(f"Força do golpe : {golpe_inicial}. Será causado um dano alto.")
        print(f"Dano alto causado : {força_do_golpe}")
        return força_do_golpe

    elif golpe_inicial == 10:
        print(f"Força do golpe : \033[1;36m{golpe_inicial} !\033[m \033[1;36mGOLPE ESPECIAL !\033[m")
        print(f"Golpe especial aplicado : \033[1;32m{força_do_golpe * 3}\033[m")
        return (força_do_golpe * 3)

    else:
        print(f"Força do golpe : \033[1;31m{golpe_inicial}\033[m. \033[1;37mNenhum dano será causado ao oponente\033[m.")
        print(f"Nenhum dano causado : {força_do_golpe}")
        return força_do_golpe

barra_de_energia_cinza(10)
linha_1_personalizavel(" BATALHA ENTRE HERÓIS 1.0 ")

continua_01 = True
while continua_01 == True:
    numero_lutador = 1
    lutador = 0

    for count in range(0, 2):
        print()
        print("{:>11}{:>30}{:>30}".format("LUTADOR", "LUTADOR", "LUTADOR"))
        print("{:>8}{:>30}{:>30}".format(numero_lutador, numero_lutador+1, numero_lutador+2))
        print("{:<12}{:<18}{:<12}{:<18}{:<12}{:<18}".format("Nome", lutadores_lista_dic[0+lutador]["Nome"], "Nome", lutadores_lista_dic[1+lutador]["Nome"], "Nome", lutadores_lista_dic[2+lutador]["Nome"]))
        print("{:<12}{:<18}{:<12}{:<18}{:<12}{:<18}".format("Força", lutadores_lista_dic[0+lutador]["Força"], "Força", lutadores_lista_dic[1+lutador]["Força"], "Força", lutadores_lista_dic[2+lutador]["Força"]))
        print("{:<12}{:<18}{:<12}{:<18}{:<12}{:<18}".format("Dextreza", lutadores_lista_dic[0+lutador]["Dextreza"], "Dextreza", lutadores_lista_dic[1+lutador]["Dextreza"], "Dextreza", lutadores_lista_dic[2+lutador]["Dextreza"]))
        print("{:<12}{:<18}{:<12}{:<18}{:<12}{:<18}".format("Velocidade", lutadores_lista_dic[0+lutador]["Velocidade"], "Velocidade", lutadores_lista_dic[1+lutador]["Velocidade"], "Velocidade", lutadores_lista_dic[2+lutador]["Velocidade"]))
        print("{:<12}{:<18}{:<12}{:<18}{:<12}{:<18}".format("Energia", lutadores_lista_dic[0+lutador]["Energia"], "Energia", lutadores_lista_dic[1+lutador]["Energia"], "Energia", lutadores_lista_dic[2+lutador]["Energia"]))
        lutador = 3
        numero_lutador = 4
        print()

    print("\nESCOLHA O SEU LUTADOR : ")
    player_choice = int(input("Opções ( 1 / 2 / 3 / 4 / 5 / 6 ) : "))
    if player_choice not in (1, 2, 3, 4, 5, 6):
        print("Escolha um dos lutadores disponíveis !")
        continua_01 = True
    else:
        linha_2_personalizavel(" LUTADOR DEFINIDO ")
        if player_choice == 1:
            print("Seu lutador :", lutadores_lista_dic[0]["Nome"])
        elif player_choice == 2:
            print("Seu lutador :", lutadores_lista_dic[1]["Nome"])
        elif player_choice == 3:
            print("Seu lutador :", lutadores_lista_dic[2]["Nome"])
        elif player_choice == 4:
            print("Seu lutador :", lutadores_lista_dic[3]["Nome"])
        elif player_choice == 5:
            print("Seu lutador :", lutadores_lista_dic[4]["Nome"])
        else:
            player_choice == 6
            print("Seu lutador :", lutadores_lista_dic[5]["Nome"])

        continua_01 = False


continua_02 = True
while continua_02 == True:
    numero_lutador = 1
    lutador = 0

    for count in range(0, 2):
        print()
        print("{:>11}{:>30}{:>30}".format("LUTADOR", "LUTADOR", "LUTADOR"))
        print("{:>8}{:>30}{:>30}".format(numero_lutador, numero_lutador+1, numero_lutador+2))
        print("{:<12}{:<18}{:<12}{:<18}{:<12}{:<18}".format("Nome", lutadores_lista_dic[0+lutador]["Nome"], "Nome", lutadores_lista_dic[1+lutador]["Nome"], "Nome", lutadores_lista_dic[2+lutador]["Nome"]))
        print("{:<12}{:<18}{:<12}{:<18}{:<12}{:<18}".format("Força", lutadores_lista_dic[0+lutador]["Força"], "Força", lutadores_lista_dic[1+lutador]["Força"], "Força", lutadores_lista_dic[2+lutador]["Força"]))
        print("{:<12}{:<18}{:<12}{:<18}{:<12}{:<18}".format("Dextreza", lutadores_lista_dic[0+lutador]["Dextreza"], "Dextreza", lutadores_lista_dic[1+lutador]["Dextreza"], "Dextreza", lutadores_lista_dic[2+lutador]["Dextreza"]))
        print("{:<12}{:<18}{:<12}{:<18}{:<12}{:<18}".format("Velocidade", lutadores_lista_dic[0+lutador]["Velocidade"], "Velocidade", lutadores_lista_dic[1+lutador]["Velocidade"], "Velocidade", lutadores_lista_dic[2+lutador]["Velocidade"]))
        print("{:<12}{:<18}{:<12}{:<18}{:<12}{:<18}".format("Energia", lutadores_lista_dic[0+lutador]["Energia"], "Energia", lutadores_lista_dic[1+lutador]["Energia"], "Energia", lutadores_lista_dic[2+lutador]["Energia"]))
        lutador = 3
        numero_lutador = 4
        print()

    print("\nESCOLHA O SEU ADVERSÁRIO : ")
    oponent_choice = int(input("Opções ( 1 / 2 / 3 / 4 / 5 / 6 ) : "))

    if oponent_choice not in (1, 2, 3, 4, 5, 6):
        print("Escolha um dos lutadores disponíveis !")
        continua_02 = True
    else:
        if oponent_choice == player_choice:
            print("O lutador {} já foi escolhido para ser o seu lutador. Escolha outro lutador para ser o seu adversário...".format(lutadores_lista_dic[player_choice-1]["Nome"]))
            continua_02 = True
        else:
            linha_2_personalizavel(" ADVERSÁRIO DEFINIDO ")
            print("Seu adversário :", lutadores_lista_dic[oponent_choice-1]["Nome"])
            continua_02 = False

print("\n\n")
sleep(1)

turno = 1
while True:

    print("{:^50}".format("A BATALHA VAI COMEÇAR !!!"))

    while lutadores_lista_dic[player_choice-1]["Energia"] > 0 and lutadores_lista_dic[oponent_choice-1]["Energia"] > 0:
        print()
        print("{:>25}{}".format("Round ", turno))
        turno += 1

        print(f"Lutador {lutadores_lista_dic[player_choice-1]['Nome']} executa um ataque !")
        dano_de_ataque = gerador_ataque(lutadores_lista_dic[player_choice-1]["Força"], lutadores_lista_dic[player_choice-1]["Velocidade"])
        lutadores_lista_dic[oponent_choice-1]["Energia"] = ( lutadores_lista_dic[oponent_choice-1]["Energia"] - dano_de_ataque )
        print("{:^46}".format("- - -"))
        print(f"Lutador {lutadores_lista_dic[oponent_choice-1]['Nome']} executa um ataque !")
        dano_de_ataque = gerador_ataque(lutadores_lista_dic[oponent_choice-1]["Força"], lutadores_lista_dic[oponent_choice-1]["Velocidade"])
        lutadores_lista_dic[player_choice-1]["Energia"] = ( lutadores_lista_dic[player_choice-1]["Energia"] - dano_de_ataque )
        print("{:^46}".format("- - -"))
        if lutadores_lista_dic[player_choice-1]['Energia'] >= 50 :
            print(f"Energia do lutador {lutadores_lista_dic[player_choice-1]['Nome']} : {lutadores_lista_dic[player_choice-1]['Energia']}")
            print("\033[1;33m█\033[m" * int(lutadores_lista_dic[player_choice-1]['Energia'] / 2 ))
        else:
            print(f"Energia do lutador {lutadores_lista_dic[player_choice-1]['Nome']} : {lutadores_lista_dic[player_choice-1]['Energia']}")
            print("\033[1;31m█\033[m" * int(lutadores_lista_dic[player_choice-1]['Energia'] / 2 ))

        if lutadores_lista_dic[oponent_choice-1]['Energia'] >= 50 :
            print(f"Energia do lutador {lutadores_lista_dic[oponent_choice-1]['Nome']} : {lutadores_lista_dic[oponent_choice-1]['Energia']}")
            print("\033[1;33m█\033[m" * int(lutadores_lista_dic[oponent_choice-1]['Energia'] / 2 ))
        else:
            print(f"Energia do lutador {lutadores_lista_dic[oponent_choice - 1]['Nome']} : {lutadores_lista_dic[oponent_choice - 1]['Energia']}")
            print("\033[1;31m█\033[m" * int(lutadores_lista_dic[oponent_choice - 1]['Energia'] / 2 ))

        print()

        sleep((0.5))

    break

print("-" * 60)
linha_2_personalizavel(" A BATALHA TERMINOU !!! ")
print("\nRESUMO DA BATALHA :")

if lutadores_lista_dic[oponent_choice-1]['Energia'] <= 0 and lutadores_lista_dic[player_choice-1]['Energia'] > 0:
    print("Energia final do lutador ---> {:<10}{:>2}{:>3} | {:<25}".format(lutadores_lista_dic[player_choice-1]['Nome'], ":", lutadores_lista_dic[player_choice-1]['Energia'], "\033[1;32m█\033[m VENCEDOR" ))
    print("Energia final do lutador ---> {:<10}{:>2}{:>3} | {:<25}".format(lutadores_lista_dic[oponent_choice-1]['Nome'], ":", lutadores_lista_dic[oponent_choice-1]['Energia'], "\033[1;31m█\033[m DERROTADO" ))

elif lutadores_lista_dic[player_choice-1]['Energia'] <= 0 and lutadores_lista_dic[oponent_choice-1]['Energia'] > 0:
    print("Energia final do lutador ---> {:<10}{:>2}{:>3} | {:<25}".format(lutadores_lista_dic[oponent_choice-1]['Nome'], ":", lutadores_lista_dic[oponent_choice-1]['Energia'], "\033[1;32m█\033[m VENCEDOR" ))
    print("Energia final do lutador ---> {:<10}{:>2}{:>3} | {:<25}".format(lutadores_lista_dic[player_choice-1]['Nome'], ":", lutadores_lista_dic[player_choice-1]['Energia'], "\033[1;31m█\033[m DERROTADO" ))

else:
    print("\nBATALHA TERMINOU SEM VENCEDOR ...")
    print("Energia final do lutador ---> {:<10}{:>2}{:>3} | {:<25}".format(lutadores_lista_dic[player_choice-1]['Nome'], ":", lutadores_lista_dic[player_choice-1]['Energia'], "\033[1;31m█\033[m DERROTADO"))
    print("Energia final do lutador ---> {:<10}{:>2}{:>3} | {:<25}".format(lutadores_lista_dic[oponent_choice-1]['Nome'], ":", lutadores_lista_dic[oponent_choice-1]['Energia'], "\033[1;31m█\033[m DERROTADO"))
