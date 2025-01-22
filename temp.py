# NÃO APAGAR NÃO APAGAR NÃO APAGAR NÃO APAGAR NÃO APAGAR NÃO APAGAR NÃO APAGAR NÃO APAGAR NÃO APAGAR NÃO APAGAR
# NÃO APAGAR NÃO APAGAR NÃO APAGAR NÃO APAGAR NÃO APAGAR NÃO APAGAR NÃO APAGAR NÃO APAGAR NÃO APAGAR NÃO APAGAR


senha = "abcdefghijklmnopqrstuvxz"

contra_senha = str(input("Digite a senha desejada : "))

if contra_senha in senha :
    print("ERRO ! A SENHA NÃO PODE SER USADA !")

else :
    print("OK ! SENHA CONFIRMADA")








""""

print("ELEIÇÕES ANOS 2000\n")

bolsonaro = 0
lula = 0
vota = True

while vota == True:
    print("Eleitor, escolha o seu candidato :")
    print("DIGITE 22 PARA votar em Bolsonaro")
    print("DIGITE 13 PARA votar em Lula")
    voto = str(input("NUMERO : "))

    if voto not in ["22", "13"]:
        print("Candidato inválido ! Tente novamente !")
    else :
        if voto == "22":
            bolsonaro += 1
        if voto == "13":
            lula += 1

    esc_02 = True
    while esc_02 == True:
        esc_01 = str(input("Deseja continuar a votação ?")).strip()[0:1]
        if esc_01 == "s":
            vota = True
            esc_02 = False
            continue
        if esc_01 == "n":
            vota = False
            esc_02 = False
            break
        else:
            print("opção inválida !")
            esc_02 = True

print("VOTAÇÃO ENCERRADA")
print("\nContagem de votos")
print(f"Bolsonaro : {bolsonaro}")
print(f"Lula : { ( lula + bolsonaro + lula ) * 8 }")





cars_data = [

    # gold
    ['BMW X6', 5, 5, 'auto', 'suv', 'gold', True, 'https://purepng.com/public/uploads/large/purepng.com-bmw-x6-blue-carcarbmwvehicletransport-9615246630450hbgr.png'],
    ['Mercedes GLE coupe', 5, 5, 'auto', 'suv', 'gold', True, 'https://www.mercedes-benz.pt/content/dam/hq/passengercars/cars/gle/gle-coupe-c167-fl-pi/modeloverview/01-2023/images/mercedes-benz-gle-coupe-c167-modeloverview-696x392-01-2023.png'],
    ['Audi Q8', 5, 5, 'auto', 'suv', 'gold', True, 'https://www.pngmart.com/files/22/Audi-Q8-PNG-Isolated-Image.png'],
    ['Jaguar I-Pace', 5, 5, 'auto', 'suv', 'gold', True, 'https://ymimg1.b8cdn.com/resized/car_model/7913/pictures/7416563/mobile_listing_main_Jaguar_I-Pace_2019__1_.png'],
    ['Porsche Cayenee Coupe',5, 5, 'auto', 'suv', 'gold', True, 'https://www.pngmart.com/files/22/Porsche-Cayenne-PNG-Clipart.png'],
    ['BWM i7', 5, 5, 'auto', 'sedan', 'gold', True, 'https://prod.cosy.bmw.cloud/bmwweb/cosySec?COSY-EU-100-7331cqgv2Z7d%25i02uCaY3MuO2kOHUtWPfbYfQn8N10tLhu1XzWVo7puMLWFmdkAj5DOPitIqZ8XgY1nTNIowJ4HO3zkyXq%25sGM8snpq6v6ODubLz2aKqfkYvjmB2fJj5DOP5Eagd%25kcWExHWpbl8FO2k3Hy2o24tXATQBrXpFkahlZ24riIqM8scpF4HvmnU0KiIFJG7dUABHvIT91QsO2JGvloRqCgpT9GsLxSQUilo90yWdBbHsLoACeV%25hJ0yLOEjkpqTACygN6nmmlOECUkw5O7sgNEbn%257b10UkNh5ucSVAbnkq83aBzOh5nmPXRYagq857Mrv1RUmP81D5Pixb7MPVY8%25MWh1DMztPOpeqVYDafuiwjmztYRS3Qc67aftxdXZiw1RSfWQxy%25%25VxdSeZLjYuzWQdjcnmj3aeZQ6KjPpXRjcZwB81vrx6Kc%252PVQ4WsKokGpc1Q8CBsJdoSWZ35uMwCRL'],
    ['Audi e-Tron GT', 5, 5, 'auto', 'sedan', 'gold', True, 'https://www.electrifying.com/files/NFeDtk7gtILNVgt4/AudietronGT.png'],
    ['Mercedes CLS', 5, 5, 'auto', 'sedan', 'gold', True, 'https://www.mercedes-benz.pt/content/dam/hq/passengercars/cars/cls/cls-coupe-c257-fl-pi/modeloverview/11-2022/images/mercedes-benz-cls-c257-modeloverview-696x392-11-2022.png'],
    ['Jaguar F-Type', 2, 2, 'auto', 'sedan', 'gold', True,'https://freepngimg.com/thumb/jaguar/24597-2-jaguar-f-type.png'],
    ['Porsche Taycan', 5, 5, 'auto', 'sedan', 'gold', True, 'https://file.kelleybluebookimages.com/kbb/base/evox/CP/15460/2024-Porsche-Taycan-front_15460_032_2400x1800_2Y.png'],

    # silver
    ['Nissan Qashqai', 5, 5, 'manual', 'suv', 'silver', True, 'https://www.greenncap.com/wp-content/uploads/nissan-qashqai-2022-0109.png'],
    ['Peugeot 3008', 5, 5, 'manual', 'suv', 'silver', True, 'https://i.pinimg.com/originals/da/90/f0/da90f0319bd65df5051158e1d4bab041.png'],
    ['Volvo XC60', 5, 5, 'manual', 'suv', 'silver', True, 'https://www.motortrend.com/uploads/sites/10/2019/08/2020-volvo-xc60-t5-momentum-4wd-suv-angular-front.png'],
    ['Citroen C4', 5, 5, 'manual', 'suv', 'silver', True, 'https://www.citroen.pt/content/dam/citroen/master/b2c/models/new-c4-e/visualizer/front-view/New%20E-C4%20and%20C4_0MP00NWP_Blanc%20Banquise_FR_1280_720.png'],
    ['Hyundai Tucson', 5, 5, 'manual', 'suv', 'silver', True, 'https://www.motortrend.com/uploads/sites/10/2019/11/2020-hyundai-tucson-sel-4wd-suv-angular-front.png'],
    ['Toyota Corolla', 5, 5, 'manual', 'sedan', 'silver', True, 'https://www.toyotaotis.com.ph/wp-content/uploads/2017/04/Altis-Page-Home-image.png'],
    ['Renault Talisman', 5, 5, 'manual', 'sedan', 'silver', True, 'https://www.chabe.com/wp-content/uploads/2020/06/Renault_Talisman.png'],
    ['Peugeout 508', 5, 5, 'manual', 'sedan', 'silver', True, 'https://www.pngmart.com/files/22/Peugeot-508-PNG-Image.png'],
    ['Hyundai Ioniq 6', 5, 5, 'manual', 'sedan', 'silver', True, 'https://www.motortrend.com/uploads/sites/10/2019/08/2020-ford-fusion-se-sedan-angular-front.png'],
    ['DS 9', 5, 5, 'manual', 'sedan', 'silver', True, 'https://cdn.imagin.studio/getImage?customer=robinsandday&make=ds&modelFamily=ds9&modelRange=ds9&modelVariant=od&modelYear=2023&zoomType=fullscreen&steering=right&width=800&angle=01&paintId=pspc0165&fileType=png'],

    # economic
    ['Opel Astra', 3, 4, 'manual', 'sedan', 'economic', True, '0000'],
    ['Seat Toledo', 5, 5, 'manual', 'sedan', 'economic', True, '0000'],
    ['Fiat Tipo', 5, 5, 'manual', 'sedan', 'economic', True, '0000'],
    ['Ford Fiesta', 5, 5, 'manual', 'sedan', 'economic', True, '0000'],
    ['Renault Megane', 3, 5, 'manual', 'sedan', 'economic', True, '0000'],
    ['Opel Corsa', 2, 2, 'manual', 'compact', 'economic', True, '0000'],
    ['Seat Ibiza', 2, 2, 'manual', 'compact', 'economic', True, '0000'],
    ['Fiat Cronos', 5, 5, 'manual', 'compact', 'economic', True, '0000'],
    ['Ford Mondeo', 5, 5, 'manual', 'compact', 'economic', True, '0000'],
    ['Renault Clio', 5, 5, 'manual', 'compact', 'economic', True, '0000'],

]

#print(len(cars_data))
#print(cars_data[0][0])
# print(f"NOME : {valor[0]:<22} {'CATEGORIA :':>15} {valor[5]:<7}")

for valor in cars_data :
    if valor[5] == "gold":
        print(f"NOME : {valor[0]:<22} {'CATEGORIA :':>15} {valor[5]:<7}")

    elif valor[5] == "silver":
        print(f"NOME : {valor[0]:<22} {'CATEGORIA :':>15} {valor[5]:<7}")

    else:
       print(f"NOME : {valor[0]:<22} {'CATEGORIA :':>15} {valor[5]:<7}")







x = "sorry\n"
print(x * 1000)



numeros = ["VAZIO", "VAZIO", "VAZIO"]

# VARIÁVEIS DE INICIALIZAÇÃO DO FOR
INICIAL = 0
FINAL = 3

continua_001 = True
while continua_001 == True:

    # VERIFICAÇÃO DA LISTA COMPLETA
    if numeros[0] != "VAZIO" and numeros[1] != "VAZIO" and numeros[2] != "VAZIO":
        continua_001 = False
        break

    for contador in range(INICIAL, FINAL):
        print(f"\ncontador atual : {contador+1}")
        n = str(input(f"Digite um número para ser inserido no {contador+1}º espaço : "))

        # VERIFICAÇÃO SE É UM NUMÉRICO DIGITADO
        if n.isnumeric():
            # CASO O ÍNDICE ESTEJA VAZIO, PODERA SER PREENCHIDO. CASO CONTRÁRIO SERÁ NOTIFICADO
            if numeros[contador] == "VAZIO":
                numeros[contador] = n
                print(f"Lista atualizada : {numeros}")
                continua_001 = True
            else:
                print(f"Este espaço já foi preenchido com o valor {numeros[contador]} e não pode ser modificado. ")

        else:
            print("ERROR ! Tente novamente !")
            print(f"Lista atualizada : {numeros}")
            INICIAL = contador
            continua_001 = True
            break

print(f"\nA lista foi preenchida corretamente  {numeros}")










def x(values):
    values[0] = 9
    values[1] = 5
    values[2] = 7


v = [2, 3, 4]
x(v)
print(v)




print('Pedro Tenório\n')
print('BEM VINDO AO CINEMA')

check_001 = True
check_002 = True


while check_001 == True :
    idade_pessoa = input('Qual a sua idade: ')
    if not idade_pessoa.isnumeric():
        # caso o usuário não digite um numero inteiro o programa não continua
        # ficando na pergunta até que venha um número
        print('Digite apenas números.')
        continue

    else:
        idade_pessoa = int(idade_pessoa)
        if idade_pessoa < 3:
            print('- Seu bilhete é gratuito')
        elif idade_pessoa <= 12:
            print('- Seu bilhete custa 10€')
        else:
            print('- Seu bilhete custa 15€')


    while check_002 == True :
        pergunta = str(input('Deseja comprar mais bilhetes[sim/nao]: ')).strip().lower()
        if pergunta == "sim":
            check_002 = True
            break

        if pergunta == "nao":
            check_001 = False
            check_002 = False
            break


        else:
            print('Resposta não aceita...')
            check_002 = True


print('FIM')



if pergunta not in opcao:
    print('Resposta não aceita')
    check = False
else:
    check = True

if pergunta == 'sim':
    continue
if pergunta == 'nao':
    break






print('Pedro Tenório\n')
print('BEM VINDO AO CINEMA')
while True:
    idade_pessoa = input('Qual a sua idade: ')
    if not idade_pessoa.isnumeric():
        # caso o usuário não digite um numero inteiro o programa não continua
        # ficando na pergunta até que venha um número
        print('Digite apenas números.')
        continue
    else:
        idade_pessoa = int(idade_pessoa)
        if idade_pessoa < 3:
            print('- Seu bilhete é gratuito')
        elif idade_pessoa <= 12:
            print('- Seu bilhete custa 10€')
        else:
            print('- Seu bilhete custa 15€')

    opcao = ('sim', 'nao', 'não')
    check = False
    while not check:
        pergunta = input('Deseja comprar mais bilhetes[sim/nao]: ').strip().lower()
        if pergunta not in opcao:
            print('Resposta não aceita')
            check = False
        else:
            check = True

    if pergunta == 'sim':
        continue
    if pergunta == 'nao' or 'não':
        break


#  Qualquer resposta que não for "sim" ou "nao" o programa repetirá a pergunta
# até vir a resposta correta para poder dar continuidade ou fim do programa
#     if opcao == 'nao':
#         break
# print('\nBom Filme')

print('FIM')




respostas_aceitas = ("Sim", "Não")

resposta = str(input("Deseja continuar o programa ? ['Sim'] ou ['Não'] ")).strip().capitalize()

while resposta not in respostas_aceitas:
    print("resposta não aceita. Favor tentar novamente...")
    resposta = str(input("Deseja continuar o programa ? ['Sim'] ou ['Não'] ")).strip().capitalize()

print("\nPrograma finalizado.")



respostas_aceitas = ("Sim", "Não")

controle_01 = False

while controle_01 == False:
    resposta = str(input("Deseja continuar o programa ? ['Sim'] ou ['Não'] ")).strip().capitalize()
    if resposta not in respostas_aceitas:
        print("resposta não aceita. Favor tentar novamente...")
        controle_01 = False
    else:
        controle_01 = True
        print("Saindo do programa ...")
        break

print("\nPrograma finalizado.")



numero = 3
letra = "a"
nome = "pereira"

while ( numero == 2 and letra == "a") or nome == "fabio":
    print("ok")

print("FIM")


def my_fun(n):
    if n == 1:
        return 1
    else:
        print("passei aqui")
        return n + my_fun(n-1)


print(my_fun(4))




from random import randint


def sortear(lista):
    print(f'Os 5 numeros sorteados são:', end=' ')
    for c in range(0, 5):
        c = randint(0, 10)
        print(f'{c} ', end='')
        lista.append(c)

def somaPar(lista):
    print(f'\nSomando os valores pares dos números sorteados temos: ', end='')
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(soma)

numero = []
sortear(numero)
somaPar(numero)








from time import sleep
def l():
    print('~' *30)

def maior(*num):
    higher = 0
    sleep(0.5)
    print('Analisando os valores passados...')
    #sleep(2)
    if len(num) == 0:
        print('Não foi passado nenhum valor')
    else:
        print(f'Foram passados {len(num)} numeros e são eles:')
        for c in num:
            print(c, end=', ')
            if c == [0]:
                higher = c
            else:
                if c > higher:
                    higher = c
        print(f'e o maior número é o {higher}')
    l()
    sleep(1)


maior(12, -1, 2, 23, 0, 7, 8, 9, 12)
maior(1, 2, 4, 5)
maior(1, 9, 5,)
maior(1, 3)
maior()






from time import sleep


def linha():
    print('~' * 30)


def escreva(msg):
    print('~' *(len(msg) + 4))
    print(f'  {msg}')
    print('~'*(len(msg) + 4))
    sleep(2.0)


def contador(x, y, z):
    if z < 0:
        z *= -1
    sleep(1)
    print(f'Contagem de {x} até {y}, de {z} em {z}:')
    sleep(0.5)
    if x > y:
        print('- ORDEM DECRESCENTE -')
        sleep(2.5)
        cont = x
        while cont >= y:
            print(f'{cont} ',end='')
            sleep(0.5)
            cont -= z
    else:
        print('- ORDEM CRESCENTE -')
        sleep(2.5)
        cont = x
        while cont <= y:
            print(f'{cont} ',end='' )
            sleep(0.5)
            cont += z
    print('-> FIM')
    sleep(1)
    linha()
escreva("CONTADOR DE NUMEROS")
print("Exemplo: ")
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez, escolha a sua contagem')
while True:
    inicio = int(input('Escolha o inicio: '))
    fim = int(input('Escolha o fim: '))
    check = True
    while check == True:
        passo = int(input('Escolha o passo: '))
        linha()
        if passo == 0:
            print('ERRO. O passo não pode ser 0.')
            check = True
        else:
            check = False
    contador(inicio, fim, passo)
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('-- Deseja continuar[S/N]: ')).strip().upper()[0]
        if pergunta not in 'SN':
            print('ERRO. Digite APENAS S ou N.')
            linha()
    if pergunta in 'N':
        print('Finalizando o programa...')
        sleep(1.5)
        break
linha()
print('Programa finalizado.')






check = True

while check == True :
    numero = str(input("Digite um número qualquer : "))
    if numero.isnumeric():
        print("ok, é um número. programa finalizado.")
        check = False
    else:
        print("Não é um número.... Tente novamente...")
        check = True

print(f"OK, você digitou o número {numero} e o programa chegou ao fim.")




lista_dicionario = [{"nome": "Fabio", "peso": "100"},{"nome": "Pereira", "peso": "75"}]
print(lista_dicionario[0].items())
print(lista_dicionario[1].items())
print()
print(lista_dicionario[0].keys())
print(lista_dicionario[0].values())

lista_dicionario.insert(0,{"nome": "Priscila", "peso": "60"})

print(lista_dicionario)

lista_dicionario.insert(1, lista_dicionario[0])

print(lista_dicionario)





from time import sleep
jogadores = []
while True:
    jogador = {}
    jogador['nome'] = str(input('Nome do jogador: ')).title().strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    cont = 0
    quant_gols = []
    jogador['gols'] = 0
    jogador['total'] = 0
    while cont < partidas:
        quant = int(input(f'    Quantos gols na {cont+1}ª partida: '))
        quant_gols.append(quant)
        cont += 1
        jogador['gols'] = quant_gols
        jogador['total'] += quant
    jogadores.append(jogador)

    pergunta = ' '
    while pergunta not in 'sn':
        pergunta = str(input('Quer continuar[S/N]: ')).lower().strip()[0]
        if pergunta not in 'sn':
            print('ERRO! Por favor digite S ou N.')
    if pergunta == 'n':
        print("break")
        break
    print('-=' *30)
print('-=' *30)
#print(jogadores)
print(f'{"Nº":<4}{"NOME":<10}{"GOLS":>8}    {"TOTAL":>10}')

for j, p in enumerate(jogadores):
    print(f'{j+1:<4}{str(p["nome"]):<10}{str(p["gols"]):>10}   {str(p["total"]):>8}')
while True:
    print('-=' *30)
    resposta = 0
    while resposta != 999:
        resposta = int(input('Mostrar dados de qual jogador (999 STOP): '))
        if resposta < 0 or resposta > len(jogadores) and resposta != 999:
            print('Numero errado, tente novamente. Não existe jogador com esse numero.')
            print('-=' *30)
        if resposta <= len(jogadores) and resposta > 0:
            print(f'--LEVANTAMENTO DO JOGADOR {jogadores[resposta-1]["nome"]}:')
            for j, item in enumerate(jogadores[resposta-1]['gols']):
                print(f'    No jogo {j+1} fez {item} gols')
            print('-=' * 30)
    if resposta == 999:
        print('Finalizando...')
        break

sleep(1.5)
print('PROGRAMA FINALIZADO')



cadastro = []
cont = 0
tot_idade = 0
pessoas = {}
while True:
    pessoas['nome'] = str(input('Nome: ')).strip().title()
    pessoas['sexo'] = ' '
    while pessoas['sexo'] not in 'MF':
        pessoas['sexo'] = str(input('Sexo[M/F]: ')).upper().strip()[0]
        if pessoas['sexo'] not in 'MF':
            print('ERRO!! Por favor apenas M ou F.')
    check = True
    while check == True:
        pessoas['idade'] = input('Idade: ')
        if pessoas['idade'].isnumeric() == True:
            check = False
        else:
            check = True
            print('ERRO!! Por favor, digite apenas números.')
    pessoas['idade'] = int(pessoas['idade'])
    tot_idade += pessoas['idade']
    cadastro.append(pessoas.copy())
    pergunta = ' '
    while pergunta not in 'sn':
        pergunta = str(input('Deseja continuar[S/N]: ')).lower().strip()[0]
        if pergunta not in 'sn':
            print('ERRO!! Apenas responda S ou N.')
    if pergunta == 'n':
        break
print('-=' *30)
print(f' -> Foram ao todo {len(cadastro)} pessoas cadastradas.')

media = tot_idade / len(cadastro)
print(f' -> A média de idade do grupo cadastrado é de {media:.2f} anos')

print(' -> As mulheres cadastradas:', end=' ')
for p in cadastro:
    if p['sexo'] in 'Ff':
        print(p['nome'], end=' ')
print()
print(f' -> Lista das pessoas com a idade acima da média: ')
for item in cadastro:
    if item['idade'] > media:
        for k, v in item.items():
            print(f'    {k} = {v}; ', end='')
        print()




dados = {}
dados['jogador'] = str(input('Nome do jogador: ')).title().strip()
partidas = int(input(f'Quantas partidas {dados["jogador"]} jogou: '))
cont = 0
quant_gols = []
dados['total'] = 0
while cont < partidas:
    quant_gols.append(int(input(f'    Quantos gols na {cont+1}ª partida: ')))
    dados['gols'] = quant_gols[:]
    dados['total'] = sum(quant_gols)
    cont += 1

'''
    quant = int(input(f'    Quantos gols na {cont+1}ª partida: '))
    quant_gols.append(quant)
    cont += 1
    dados['gols'] = quant_gols
    dados['total'] += quant

'''
print('=-' *30)
print(dados)

print('=-' *30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('=-' *30)
print(f'O jogador {dados["jogador"]}, jogou {partidas} partidas')

for jg, gol in enumerate(dados['gols']):
    print(f'   => Na {jg+1}ª partida {dados["jogador"]}, fez {gol} gols')
print(f'Foi um total de {dados["total"]} gols de {dados["jogador"]}.')




notas_alunos = []
boletim = []

while True:
    nome_aluno = str(input('Qual nome do aluno: ')).strip()
    notas_alunos.append(nome_aluno)

    nota1 = float(input('Primeira nota: '))
    notas_alunos.append(nota1)

    nota2 = float(input('Segunda nota: '))
    notas_alunos.append(nota2)

    #media = (nota1 + nota2) / 2
    #medias.append(media)

    boletim.append(notas_alunos[:])
    notas_alunos.clear()

    pergunta = ' '
    while pergunta not in 'sn':
        pergunta = str(input('Quer continuar [S/N]? R: ')).lower().strip()[0]
    if pergunta == 'n':
        break
print('=-' *40)



print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}    {"SITUAÇÃO":^10}')
for j, p in enumerate(boletim):
    media = (p[1] + p[2]) / 2
    print(f'{j+1:<4}{p[0]:<10}{media:>8.1f}', end='    ')
    if media > 7.0:
        print(f'{"APROVADO":>10}')
    else:
        print(f'{"REPROVADO":>10}')

while True:
    resposta = 0
    print('=-' *40)
    while resposta <= len(boletim):
        resposta = int(input('Mostrar notas de qual aluno? (999 para interromper) R: '))
        if resposta > len(boletim):
            print('ERRO NA RESPOSTA, tente novamente...')
        else:
            print(f'As notas do Aluno {boletim[resposta-1][0]} são: {boletim[resposta-1][1]} e {boletim[resposta-1][2]}')
            print('-=' *40)
    if resposta == 999:
        break

print('=-' *40)
print('PROGRAMA FINALIZADO, VOLTE SEMPRE!!!')



# indices                            *********** 0 ************   *********** 1 ************
# estrutura da sua lista boletim = [ [nome_aluno, nota1, nota2] , [nome_aluno, nota1, nota2], ... ]
# itens dentro da lista                    0        1      2             0        1      2
print("\n")
print(f"SUA LISTA BOLETIM É ESTA : {boletim}")
print(f"CADASTRO NUMERO 0 DA SUA LISTA BOLETIM : {boletim[0]}")
print(f"ITEM 0 DO CADASTRO 0 {boletim[0][0]}")
print(f"ITEM 1 DO CADASTRO 0 {boletim[0][1]}")
print(f"ITEM 2 DO CADASTRO 0 {boletim[0][2]}")

print(f"As notas de {boletim[0][0]} sao {boletim[0][1]} e {boletim[0][2]}")

print("\n")
print(f"CADASTRO NUMERO 1 DA SUA LISTA BOLETIM : {boletim[1]}")
print(boletim[1])
print(f"ITEM 0 DO CADASTRO 1 {boletim[1][0]}")
print(f"ITEM 1 DO CADASTRO 1 {boletim[1][1]}")
print(f"ITEM 2 DO CADASTRO 1 {boletim[1][2]}")
print("\n")


import random

notas_alunos = []
boletim = []



while True:

    for count in range(0, 1001, 1):
        count_temp = str(count+1)
        nome_aluno = ("Aluno_" + count_temp)
        nota1 = random.randint(0, 10)
        nota2 = random.randint(0, 10)
        media = (nota1 + nota2) / 2
        notas_alunos.append([nome_aluno, [nota1, nota2], media])

    print(notas_alunos)
    print(len(notas_alunos))

    #nome_aluno = str(input('Qual nome do aluno: ')).strip()
    #notas_alunos.append(nome_aluno)

    #nota1 = float(input('Primeira nota: '))
    #notas_alunos.append(nota1)

    #nota2 = float(input('Segunda nota: '))
    #notas_alunos.append(nota2)

    #media = (nota1 + nota2) / 2
    #medias.append(media)

    #boletim.append(notas_alunos[:])
    #notas_alunos.clear()

    pergunta = ' '
    while pergunta not in 'sn':
        pergunta = str(input('Quer continuar [S/N]? R: ')).lower().strip()[0]
    if pergunta == 'n':
        break
print('=-' *40)

print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}    {"SITUAÇÃO":^10}')

for count in range (0, 1001, 1):
    print(f"{notas_alunos[count]}")


while True:
    resposta = 0
    print('=-' *40)
    while resposta <= len(notas_alunos):
        resposta = int(input('Mostrar notas de qual aluno? (999 para interromper) R: '))
        if resposta >= len(notas_alunos):
            print('ERRO NA RESPOSTA, tente novamente...')
        else:
            print(f'As notas do Aluno {notas_alunos[resposta][0]} são: {notas_alunos[resposta][1:]}')
            print('-=' *40)
    if resposta == 999:
        break

print('=-' *40)
print('PROGRAMA FINALIZADO, VOLTE SEMPRE!!!')






from random import randint
print('-' *30)
print(f'{"MEGA SENA":^28}')
print('-' *30)

c = 1
check = True
numeros_sorteados = []
contador_erro = 0

while check == True:
    print("PRÓXIMO JOGO :")
    while c <= 6:

        n = randint(1, 60)
        print(f"NUMERO SORTEADO : {n}.")

        if n not in numeros_sorteados:
            numeros_sorteados.append(n)
            c += 1
            check = True

        else:
            print(f"---> Sorteando pela segunda vez pois já saiu o numero {n}.")
            novo_numero = randint(1, 60)
            print(f"---> Novo número sorteado : {novo_numero}.\n")
            check = True

            if novo_numero == n:
                print(f"\033[1;31m    *** Sorteando pela terceira vez pois já saiu o numero {novo_numero}.\033[m")
                outro = randint(1, 60)
                print(f"    *** Novo número sorteado : {outro}.")
                numeros_sorteados.append(outro)
                print("    *** FIM DO PROGRAMA POR ERRO CRITICO.\n")
                check = False
            else:
                numeros_sorteados.append(novo_numero)
            c += 1
    c = 1
    contador_erro += 1
    print("\nJOGO COMPLETO :")
    print(f"{numeros_sorteados}")
    print(f"\033[1;33mTotal de {len(numeros_sorteados)} numeros sorteados.\033[m\n")
    numeros_sorteados.clear()

print(f"\033[7;33;32mQuantidade de jogos para o erro crítico acontecer :\033[m\033[7;31m {contador_erro} \033[m")




pessoas_dados = []
todos = []
menor_peso = maior_peso = totpessoas = 0
while True:
    pessoas_dados.append(str(input('Nome: ')))
    pessoas_dados.append(float(input('Peso: ')))
    if len(todos) == 0:
        maior_peso = menor_peso = pessoas_dados[1]
    else:
        if pessoas_dados[1] > maior_peso:
            maior_peso = pessoas_dados[1]
        if pessoas_dados[1] < menor_peso:
            menor_peso = pessoas_dados[1]
    todos.append(pessoas_dados[:])
    pessoas_dados.clear()
    pergunta = ' '
    while pergunta not in 'sn':
        pergunta = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
    if pergunta == 'n':
        break
for dados in todos:
    if dados[0]:
        totpessoas += 1
print('-=' *30)
print(f'Foram cadastradas {totpessoas} pessoas')
print(f'O maior peso foi {maior_peso}Kg. E o peso foi', end=' ')
for dados in todos:
    if dados[1] == maior_peso:
        print(f'"{dados[0]}"', end=' ')
print(f'\nO menor peso foi {menor_peso}Kg. E o peso foi', end=' ')
for dados in todos:
    if dados[1] == menor_peso:
        print(f'"{dados[0]}"', end=' ')



parenteses = []
expressao = str(input('Digite a expressão: '))
for item in expressao:
    if item == '(':
        parenteses.append('(')
    if item == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')

if len(parenteses) == 0:
    print('Expressão VALIDA.')
else:
    if parenteses[0] == ')':
        print('Expressão INVALIDA')
        print('Pois a ordem dos parenteses esta incorreta.')
    else:
        print('Expressão INVALIDA')


parentesesABERTO = []
parentesesFECHADO = []
expressao = str(input('Digite sua expressão: ')).strip()
for caracter in expressao:
    if caracter == '(':
        parentesesABERTO.append(caracter)
    if caracter == ')':
        parentesesFECHADO.append(caracter)
if len(parentesesABERTO) == len(parentesesFECHADO):
    print('Sua expressão está CORRETA.')
else:
    print('Sua expressão está INCORRETA.')




lista = ["casa", "colegio", "parede","pizza"]
print(len(lista))
print(lista)
print(f"item 0 {lista[0]}")
print(f"item 1 {lista[1]}")
print(f"item 2 {lista[2]}")
print(f"item 3 {lista[3]}\n")

lista.insert(2, "CHANGE 0")
print(len(lista))

print(lista)
print(f"item 0 {lista[0]}")
print(f"item 1 {lista[1]}")
print(f"item 2 {lista[2]}")
print(f"item 3 {lista[3]}")
print(f"item 4 {lista[3]}")



# .insert
numeros = []
maior = 0
menor = 0
for contador in range(0, 5):
    n = int(input('Digite um valor: '))
    if contador == 0:
        numeros.insert(0, n)
        print('Valor foi adicionado ao final da lista.')
    if contador == 1:
        if n > numeros[0]:
            numeros.insert(1, n)
            print('Este valor é maior, por isso vai pro final da lista.')
        if n < numeros[0]:
            numeros.insert(0, n)
            print('Este valor foi adicionado na posição 0.')
    if contador == 2:
        if n < numeros[0] and n < numeros[1]:
            numeros.insert(0, n)
            print('Este valor foi adicionado na posição 0.')
        if n > numeros[0] and n > numeros[1]:
            numeros.insert(2, n)
            print('Este valor é o maior, por isso vai para o final da lista.')
        if n > numeros[0] and n < numeros[1] or n < numeros[0] and n < numeros[1]:
            numeros.insert(1, n)
            print('Este valor foi adicionado na posição 1.')
    if contador == 3:
        if n > numeros[0] and n > numeros[1] and n > numeros[2]:
            numeros.insert(3, n)
            print('Este valor é ainda maior por isso vai pro final da lista.')
        if n < numeros[0] and n < numeros[1] and n < numeros[2]:
            numeros.insert(0, n)
            print('Este valor foi adicionado na posição 0')
        if n > numeros[0] and n < numeros[1] and n < numeros[2]:
            numeros.insert(1, n)
            print('Este valor foi adicionado na posição 1')
        if n > numeros[0] and n > numeros[1] and n < numeros[2]:
            numeros.insert(2, n)
            print('Este valor foi adicionado na posição 2')
    if contador == 4:
        if n > numeros[0] and n > numeros[1] and n > numeros[2] and n > numeros[3]:
            numeros.insert(4, n)
            print('Este sim é o mair valor digitado até, portanto vai para o final da lista.')
        if n < numeros[0] and n < numeros[1] and n < numeros[2] and n < numeros[3]:
            numeros.insert(0, n)
            print('Este valor foi adicionado na posição 0.')
        if n > numeros[0] and n > numeros[1] and n > numeros[2] and n < numeros[3]:
            numeros.insert(3, n)
            print('Este valor foi adicionado na posição 3.')
        if n > numeros[0] and n > numeros[1] and n < numeros[2] and n < numeros[3]:
            numeros.insert(2, n)
            print('Este valor foi adicionado na posição 2.')
        if n > numeros[0] and n < numeros[1] and n < numeros[2] and n < numeros[3]:
            numeros.insert(1, n)
            print('Este valor foi adicionado na posição 1.')
print('-=' *40)
print(f'A lista que você digitou em ordem crescente: {numeros}')








valores = []
maior = 0
menor = 0
for pos in range(0, 5):
    valores.append(int(input(f'Digite um valor para a {pos +1}ª posição : ')))
    if pos == 0:
        maior = valores[pos]
        menor = valores[pos]
    else:
        if valores[pos] < menor:
            menor = valores[pos]
        if valores[pos] > maior:
            maior = valores[pos]
print('-=' *40)
print(f'Você digitou os valores {valores}.')
print(f'O maior valor digitado foi {maior} nas posições ',end=' ')
for posiçãomaior, valor in enumerate(valores):
    if valor == maior:
        print(f'{posiçãomaior}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end=' ')
for posiçãomenor, valor in enumerate(valores):
    if valor == menor:
        print(f'{posiçãomenor}...',end=' ')


valores = []
for pos in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {pos}: ')))
print('-=' *40)
print(f'Você digitou os valores {valores}.')
print(f'O maior valor digitado foi {max(valores)} nas posições ',end=' ')
for posiçãomaior, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{posiçãomaior}...', end=' ')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end=' ')
for posiçãomenor, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{posiçãomenor}...',end=' ')



vogais = ("a", "e", "i", "o", "u")
vogais_encontradas = list()

palavra = "cachorro"

for letra in range(0, len(palavra)):
    print(f"Vamos analisar a letra : {palavra[letra]}")
    if palavra[letra] in vogais:
        print(f"A letra '{palavra[letra]}' é uma vogal")
        vogais_encontradas.append(palavra[letra])
    else:
        print(f"A letra '{palavra[letra]}' não é uma vogal")

print(f"\nVogais encontradas na palavra '{palavra}' : '{vogais_encontradas}' ")



palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'praticar', 'estudar',
            'trabalhar', 'mercado', 'programar', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p} temos',end=' ')
    for v in p:
        if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u':
            print(f'{v}', end=' ')



print('='* 30)
print('        BANCO MILENIUM')
print('=' *30)
valor = int(input('Qual valor você quer sacar: R$ '))
cedulas100 = valor // 100
sobr = valor % 100
cedulas50 = sobr // 50
sobra = sobr % 50
cedulas20 = sobra // 20
sobra1 = sobra % 20
cedulas10 = sobra1 // 10
sobra2 = sobra1 % 10
cedulas1 = sobra2 // 1
print(f'{cedulas100} cedulas de 100')
print(f'{cedulas50} cedulas de 50')
print(f'{cedulas20} cedulas de 20')
print(f'{cedulas10} cedulas de 10')
print(f'{cedulas1} cedulas de 1')



primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
count = 1
while count <= 10:
    print(f'{termo}')
    termo += razao
    count += 1
mais = int(input('Quantos termos quer mostrar? '))
while mais != 0:
    count = 1
    while mais >= count:
        print(f'{termo}')
        termo += razao
        count += 1
    mais = int(input('Quer mostrar mais quantos termos? '))
print('FIM')




print('SEQUÊNCIA DE FIBONACCI')
print('*' *23)
termo = int(input('Digite quantos termos você quer mostrar: '))
penultimo = 0
ultimo = 1
count = 2
soma = 0
while termo <= count:
    print(f'{penultimo} -> {ultimo} -> {soma}')
    soma = penultimo + ultimo
    count += 1





from random import randint
from time import sleep


print('*' *20)
print('JOGO DA ADIVINHAÇÃO')
print('*' *20)
#sleep(1)
print('O PC pensará num numero de 0 a 10 e você terá que adivinha-lo.')
#sleep(3)
print('E o jogo começa...')
#sleep(2)
print('AGORA!!!!')
pc = randint(0, 10)
print(pc)
soma = 1
tentativa = int(input('Que numero o PC pensou? R: '))
if tentativa == pc:
    print('PARABÉEEEENS, VOCÊ ACERTOU DE PRIMEIRA.')
while pc != tentativa:
    if tentativa > pc:
        tentativa = int(input('É menos, Tente novamente: '))
        soma += 1
    if tentativa < pc:
        tentativa = int(input('É mais, tente novamente: '))
        soma += 1
    if tentativa == pc:
        if soma <= 4:
            print('VOCÊ ACERTOU!')
        if soma >= 5:
            print('UFA.. FINALMENTE, VOCÊ ACERTOU.')
print(f'O PC pensou no numero {pc} e você acertou digitando o numero {tentativa}')
print(f'Para acertar você precisou de {soma} tentativas.')



print('=' *20)
print('\033[1;33mFORMAÇÃO DE TRIÂNGULOS\033[m')
print('=' *20)
print('')
print('Digite TRÊS retas e direi se podem ou não formar triangulo')
print('E também direi o TIPO de triângulo que pode formar')
r1 = float(input('1º reta: '))
r2 = float(input('2º reta: '))
r3 = float(input('3º reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas PODEM formar um triângulo.')
    print('Agora de acordo com essas retas')
    if r1 == r2 and r1 == r3 and r3 == r2: #OU pode fazer da seguinte forma: r1 == r2 == r3:
        print('Os três lados IGUAIS: EQUILÁTERO')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
        print('DOIS lados iguais e um DIFERENTE: ISOSCELES')
    elif r1 != r2 and r1 != r3 and r2 != r3: #OU pode fazer da seguinte forma r1 != r2 != r3 != r1:
        print('Os três lados DIFERENTES: ESCALENO')
else:
    print('Essas retas NÃO PODEM formar um triângulo.')






# Programa para comprar uma casa
# Perguntar valor da casa, salario e quantos anos vai pagar
# Calcular valor da prestação mensal
# Sabendo que não pode exceder 30% do salário
# ou entao sera negado
print('=' * 20)
print('APROVAÇÃO DE CRÉDITO')
print('=' * 20)
nome_vendedor = str(input('Nome do vendedor: '))
c = float(input('Qual valor da casa, {}? '.format(nome_vendedor)))  # Variavel declarada como float
s = float(input('Qual salário do comprador, {}? '.format(nome_vendedor)))  # Variavel declarada como float
a = int(input('Em quantos anos o comprador quer pagar, {}? '.format(nome_vendedor)))
print(' ')  # Ao invés de usar esse print para pular linhas , utilize o "\n".
print('{}, de acordo com as regras da empresa...'.format(nome_vendedor))
print(' ')  # Ao invés de usar esse print para pular linhas , utilize o "\n".
pm = c / (12 * a)
exs = (s * 30) / 100  # Essa alteração não modifica o resultado.
print(
    f"\n30% do salario : {exs:.2f} // Parcela Mensal : {pm:.2f}")  # Apenas uma saída para facilitar a verificação dos resultados.
print(
    f"Coeficiente : {pm / s:.3f}\nPara o empréstimo ser aceito o coeficiente precisa ser menor que 0.3.")  # Apenas uma saída para facilitar a verificação dos resultados.

if exs <= pm:
    print('O credito para o seu comprador \033[1;31mNÃO FOI APROVADO\033[m')
    print('Pois a \033[4mtaxa de esforço\033[m do comprador que é de {:.2f}€'.format(exs))
    print('Não coincide com o valor necessario')
else:
    print('O credito para seu comprador foi \033[1;32mAPROVADO\033[m')
    print('Pois a \033[4mtaxa de esforço\033[m do comprador que é de {:.2f}€'.format(exs))
    print('Coincide com as regras da empresa')
print(' ')  # Ao invés de usar esse print para pular linhas , utilize o "\n".
print('Obrigado {} e tenha um otimo dia!'.format(nome_vendedor))


frase = str(input("Digite uma frase de até 5 palavras : ")).strip()
frase_separada = frase.split()

escolha = 0
continua = True

while continua == True:
    try:
        escolha = int(input("Qual destas palavras você quer que eu mostre ? ( 1 - 5 ) "))
    except (ValueError, TypeError):
        print("Você não digitou um número inteiro entre 1 e 5 corretamente")

    else:
        if escolha <= 0 or escolha >= 6:
            print("Você não digitou um número dentro dos parametros passados")
        else:
            print("Você escolheu a {}º palavra. A palavra é : {}".format(escolha, frase_separada[escolha - 1]))



frase = str(input("Digite uma frase de até 5 palavras : ")).strip()
escolha = int(input("Qual destas palavras você quer que eu mostre ? ( 1 - 5 ) "))
frase_separada = frase.split()
print("Você escolheu a {}º palavra. A palavra é : {}".format(escolha, frase_separada[escolha-1]))


frase = str(input('Digite uma frase com até CINCO palavras: ')).strip()
escolha = str(input('Agora me diga a posição da palavra, que eu direi qual é a palavra: '))
frase_partida = frase.split()
if escolha == '1':
    print('Nessa posição encontra-se a palavra {}'.format(frase_partida[0]))
if escolha == '2' :
    print('Nessa posição encontra-se a palavra {}'.format(frase_partida[1]))
if escolha == '3':
    print('Nessa posição encontra-se a palavra {}'.format(frase_partida[2]))
if escolha == '4':
    print('Nessa posição encontra-se a palavra {}'.format(frase_partida[3]))
if escolha == '5':
    print('Nessa posição encontra-se a palavra {}'.format(frase_partida[4]))


frase_completa = "CLUBE DE REGATAS VASCO DA GAMA"
frase_repartida = frase_completa.split()
print(frase_completa)
print("\nFrase repartida 'lembrando que o .split() forma uma lista' : {}".format(frase_repartida))

# Presta atenção nesses comandos :
print("Tamanho da frase incluindo os espaços em branco : {}".format(len(frase_completa)))
print("A frase tem {} caracteres sem os espaços em branco".format(len(frase_completa) - frase_completa.count(" ")))
print("A primeira palavra da frase é {}, e tem {} caracteres".format(frase_repartida[0], len(frase_repartida[0])))
print("A segunda palavra da frase é {}, e tem {} caracteres".format(frase_repartida[1], len(frase_repartida[1])))
print("A terceira palavra da frase é {}, e tem {} caracteres".format(frase_repartida[2], len(frase_repartida[2])))
print()

# Presta atenção nesses comandos :
# O primeiro [ ] chama a palavra e se colocarmos em seguida um outro [ ], este irá percorrer a palavra.
print("A primeira letra da primeira palavra da frase é : {}".format(frase_repartida[0][0]))
print("A segunda letra da primeira palavra da frase é : {}".format(frase_repartida[0][1]))
print("A terceira letra da primeira palavra da frase é : {}".format(frase_repartida[0][2]))
print("A quarta letra da primeira palavra da frase é : {}".format(frase_repartida[0][3]))
print("A quinta letra da primeira palavra da frase é : {}".format(frase_repartida[0][4]))
print()

# Lembra que o '-1' como índice retorna o último componente ?
# O primeiro [-1] chama a última palavra e se colocarmos em seguida um outro [ ], este irá percorrer a palavra selecionada.
print("A ultima letra da ultima palavra da frase é : {}".format(frase_repartida[-1][-1]))

# Outra forma de você chegar ao último item de uma lista :
# Basta você saber a quantidade de itens e diminuir um.
print("A ultima palavra da frase é : {}".format(frase_repartida[len(frase_repartida)-1]))




nome_completo = str(input("Digite seu nome completo : ").strip())
nome_partido = nome_completo.split()
print("\nNome repartido 'lembrando que o .split() forma uma lista' : {}".format(nome_partido))

print("Nome em maiúsculo : {}".format(nome_completo.upper()))
print("Nome em minúsculo : {}".format(nome_completo.lower()))
print("Tamanho do nome completo incluindo os espaços em branco : {}".format(len(nome_completo)))
print("Seu nome todo tem {} caracteres sem os espaços em branco".format(len(nome_completo) - nome_completo.count(" ")))
print("Seu primeiro nome que é {}, tem {} caracteres".format(nome_partido[0], len(nome_partido[0])))


nome = str(input('Digite seu nome todo: ')).strip()
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('E seu primeiro nome tem {} letras'.format(nome.find(' ')))



import emoji
print(emoji.emojize("Olá Mundo ! :1st_place_medal:"))
print(emoji.emojize("Olá Mundo ! :thumbs_up:"))
print(emoji.emojize("Olá Mundo ! :sunglasses:", language="alias"))
print(emoji.emojize("Olá Mundo ! :sunglasses:", language="pt"))
print(emoji.emojize("Olá Mundo ! :sunglasses:"))


nome = input("Qual o seu nome ? ")
print("Bem-vindo", nome)

dia = input("\nEm que dia você nasceu ? ")
mes = input("Em que mês você nasceu ? ")
ano = input("Em que ano você nasceu? ")

print("{}, você nasceu no dia {} de {} de {}.".format(nome, dia, mes, ano))
print(nome + ", você nasceu no dia", dia, "de", mes, "de", ano + ".")
print(f"{nome}, você nasceu no dia {dia} de {mes} de {ano}.")

print("\nVAMOS FAZER UMA SOMA SIMPLES")
num1 = int(input("Digite o primeiro valor : "))
num2 = int(input("Digite o segundo valor : "))
soma = num1 + num2
print(f"A soma é {soma}")



print("ELEIÇÕES ANOS 2000\n")

bolsonaro = 0
lula = 0

vota = True

while vota == True:
    print("Eleitor, escolha o seu candidato :")
    print("DIGITE 22 PARA votar em Bolsonaro")
    print("DIGITE 13 PARA votar em Lula")
    voto = str(input("NUMERO : "))

    if voto not in ["22", "13"]:
        print("Candidato inválido ! Tente novamente !")

    else :
        if voto == "22":
            bolsonaro += 1

        if voto == "13":
            lula += 1

    esc_02 = True
    while esc_02 == True:

        esc_01 = str(input("Deseja continuar a votação ?")).strip()[0:1]

        if esc_01 == "s":
            vota = True
            esc_02 = False
            continue

        if esc_01 == "n":
            vota = False
            esc_02 = False
            break

        else:
            print("opção inválida !")
            esc_02 = True



print("VOTAÇÃO ENCERRADA")
print("\nContagem de votos")
print(f"Bolsonaro : {bolsonaro}")
print(f"Lula : { ( lula + bolsonaro + lula ) * 8 }")



a = 100.1342
print(round(a, 3))
print("{:.3f}".format(a))

#print("{:.<20}{:>4}{:>6.2f}".format(produtos[valor], "RS ", produtos[valor + 1]))


l = list("128y9t345h9780523g4fh7823r4gfh7984f31j98-d34f1ejk80-9df3er1k0934")

print(len(l))
print(l[0])
print(l[len(l)-1])



from time import sleep

print("\033[0;30;43m*************************************************\033[m\n"
      "\033[7;30;43m*             Programação em Python             *\033[m\n"
      "\033[7;30;43m*                Fábio JS Pereira               *\033[m\n"
      "\033[0;30;43m*************************************************\033[m\n"
      "\n"
      "\033[0;30;47mPrograma 01 : Média aritimética\033[m\n")
input()
 


palavra = "fabiojspereira"

lista_temp = list (palavra[:])

print(lista_temp)



cpf = input('Digite um CPF: ')
caract = len(cpf)

if not cpf.isnumeric():
    print('CPF inválido! Digite apenas números!')
elif not caract == 11:
    print('CPF inválido. Digite um CPF válido!')
else:
    verificacao_cpf = list(cpf[:9])  # pega os 09 primeiros dígitos do CPF
    result_cpf = cpf[9:]  # pega os 02 últimos dígitos do CPF

#  cálculo conferir o primeiro dígito:

v1, v2, v3, v4, v5, v6, v7, v8, v9 = verificacao_cpf

valor1 = int(v1) * 10
valor2 = int(v2) * 9
valor3 = int(v3) * 8
valor4 = int(v4) * 7
valor5 = int(v5) * 6
valor6 = int(v6) * 5
valor7 = int(v7) * 4
valor8 = int(v8) * 3
valor9 = int(v9) * 2

result_1 = valor1 + valor2 + valor3 + valor4 + valor5 + valor6 + valor7 + valor8 + valor9
print(result_1)

dig_1 = 11 - (result_1 % 11)

if dig_1 > 9:
    dig_1 = 0

#  cálculo conferir o segundo dígito:

valor1 = int(v1) * 11
valor2 = int(v2) * 10
valor3 = int(v3) * 9
valor4 = int(v4) * 8
valor5 = int(v5) * 7
valor6 = int(v6) * 6
valor7 = int(v7) * 5
valor8 = int(v8) * 4
valor9 = int(v9) * 3
valor10 = dig_1 * 2

result_2 = valor1 + valor2 + valor3 + valor4 + valor5 + valor6 + valor7 + valor8 + valor9 + valor10
print(result_2)

dig_2 = 11 - (result_2 % 11)

# validando o CPF:

novo_CPF = cpf[:9] + str(dig_1) + str(dig_2)
if novo_CPF == cpf:
    print(f'O cpf {cpf} foi validado com sucesso!')
else:
    print(f'O {cpf} é inválido!')
	
	

palavras = ("casa", "carro", "bicicleta", "computador", "paralelepípedo", "apartamento", "praia", "sofa", "cachorro")
grupo_vogais = ["a", "e", "i", "o", "u"]

vogais_encontradas = list()

for cada_palavra in palavras:
	print(f"\nNa palavra \033[1;33m{cada_palavra.upper()}\033[m, temos as seguintes vogais : ", end="")
	for caracter in range(0, len(cada_palavra)):
		if cada_palavra[caracter] in grupo_vogais:
			vogais_encontradas.append(cada_palavra[caracter])
	print(f"\033[1;34m{sorted(set(vogais_encontradas))}\033[m", end=" ")
	vogais_encontradas = []
	print("\nlimpando a lista de vogais...")



def centraliza_texto(texto="LISTAGEM DE PRODUTOS"):

	linha = len(texto)+10
	print("-" * linha)
	print("     {:^20}".format(texto))
	print("-" * linha)


produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
centraliza_texto()

for valor in range (0, len(produtos), 2 ):
	print("{:.<20}{:>4}{:>6.2f}".format(produtos[valor], "RS ", produtos[valor+1]))



tupla = tuple()
numeros_pares = list()

tupla = (
	int(input("Digite um valor : ")),
	int(input("Digite um valor : ")),
	int(input("Digite um valor : ")),
	int(input("Digite um valor : "))
	)

print(f"A tupla foi criada : {tupla}")

count_temp = 0
contador = 0
check = True
for valor in range (0, len(tupla)):
	if tupla[valor] == 9:
		#print(f"{tupla[valor]}. Numero 9 digitado...")
		contador += 1

	if (tupla[valor]) % 2 == 0:
		#print(f"{tupla[valor]}. Numero par digitado...")
		numeros_pares.append(tupla[valor])

	while check == True:
		#count_temp += 1
		#print(f"ENTREI NO WHILE PELA {count_temp}º VEZ...")
		if tupla[valor] == 3:
			#print(f"{tupla[valor]}. Numero 3 digitado...")
			pos_num_3 = valor
			check = False
			break

		else:
			#print(f"{tupla[valor]}. Numero qualquer digitado... foda-se...")
			check = True
			break

print(f"\nQuantidade de números 9 digitados é de : {contador} vez(es).")
#print(f"\nA quantidade de números 9 é de {tupla.count(9)}")
print(f"\nQuantidade de números pares digitados : {len(numeros_pares)}")
print(f"Listagem de números pares digitados : {numeros_pares}")

if check == True:
	print(f"\nO valor 3 não foi digitado em nenhum momento ....")
else:
	print(f"\nO valor 3 foi digitado primeiramente na {pos_num_3 + 1}º posição.")



from random import randint

tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100) )

print(f"Tupla Gerada : {tupla}")

# Calcular menor valor e maior valor na tupla gerada :

menor = maior = tupla[0]
for valor in range (0, len(tupla), 1):
	if tupla[valor] < menor:
		menor = tupla[valor]
	if tupla[valor] > maior:
		maior = tupla[valor]

print(f"\nMaior Valor : {maior}")
print(f"Menor Valor : {menor}")
#print(f"\nO maior número dentro da tupla é : {max(tupla_gerada)}.")
#print(f"O menor número dentro da tupla é : {min(tupla_gerada)}.")



times = (
	"Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro",
	"Flamengo", "Vasco", "Chapecoense", "Atlético-MG", "Botafogo",
	"Athletico", "Bahia", "São Paulo", "Fluminense", "Sport", "Vitória",
	"Coritiba", "Avaí", "Ponte Preta", "Atlético-GO"
	)

print("Classificação final do Campeonato Brasileiro : ")
for valor in range (0, len(times)):
	print(f"{valor+1}º {times[valor]}")

print(f"\nExibindo os 5 primeiros colocados : ")
for valor in range (0,5):
	print(f"{valor + 1}º {times[valor]}")

print(f"\nExibindo os 4 últimos colocados : {times[-4:]}")

print("\nExibição em ordem alfabética : ")
lista_times_ordenada = sorted(times)
for valor in range (0, len(lista_times_ordenada)):
	print(lista_times_ordenada[valor])

print("\nPosição do clube Chapecoense :")
for valor in range (0, len(times)):
	if times[valor] == "Chapecoense":
		print(f"Chapecoense encontra-se na posição : {valor+1}º.")



extenso = (
	"zero", "um", "dois", "três", "quatro", "cinco",
	"seis", "sete", "oito", "nove", "dez",
	"onze", "doze", "treze", "catorze", "quinze",
	"dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
	)

numero = int(input("Digite um número entre 0 e 20 para que seja exibido por extenso : "))

if 0 <= numero <= 20:
	print(f"\nO número digitado foi {numero}. Por extenso : {extenso[numero]}")
else:
	print("Valor incorreto. Digite um número entre 0 e 20... ")



dados_jogador = dict()
lista_de_gols = list()
total_de_gols = 0

dados_jogador ["nome"] = str(input("Digite o nome do jogador : ")).strip()
dados_jogador ["qtd_partidas"] = int(input(f"Digite a quantidade de partidas que o jogador {dados_jogador ['nome'] } participou : "))

lista_de_gols = list(range(0, dados_jogador["qtd_partidas"]))  # Criação da lista com a quantidade de itens.

for partida in range (0, dados_jogador["qtd_partidas"]):
	lista_de_gols[partida] = int(input(f"Digite a quantidade de gols na partida {partida+1} : "))

dados_jogador["gols"] = lista_de_gols
total_de_gols = sum(dados_jogador["gols"])
dados_jogador ["total_gols"] = total_de_gols

print(f"{dados_jogador}\n")

for k,v in dados_jogador.items():
	print(f"O campo {k}, tem o valor : {v}")



def contador(*num):
	qtd_num = len(num)
	print(f"\nExistem {qtd_num} números dentro do parâmetro {num} passado :")

	for value in num:
		print(f"Valores passados : {value}")
	print("FIM\n")

contador(10,12,33,4)
contador(1,2,3)
contador()
contador(10)



def descrever_pet(pet_name, pet_tipo="cão"):
	print(f"Eu tenho um animal que se chama : {pet_name.title()}.")
	print(f"{pet_name.title()} é um {pet_tipo}...")


descrever_pet(pet_name="jhony")



def descrever_pet(pet_name, pet_tipo):
	print(f"Eu tenho um animal que se chama : {pet_name.title()}.", end="")
	print(f" {pet_name.title()} é um {pet_tipo}...")


descrever_pet(pet_name="jhony", pet_tipo="cachorro")



def descrever_pet(pet_name,pet_tipo):
	print(f"Eu tenho um animal que se chama : {pet_name.title()}")
	print(f"{pet_name.title()} é um {pet_tipo}...")

descrever_pet("jhony", "cachorro")



def favorite_book(titulo):
	print(f"Um dos meus livros favoritos é : {titulo.title()}")


favorite_book("enigma na televisão")


def display_message():
	print("Estamos aprendendo sobre funções em Python.")


display_message()

lista_1 = [1,2,3,4]
lista_1.append([5,6,7])
print(lista_1)
print(len(lista_1))
print(lista_1[4])
print(lista_1[4][0])
print(lista_1[4][1])
print(lista_1[4][2])



A = []
B = {}
C = ()

print(type(A))
print(type(B))
print(type(C))


def make_album(artist, album, trilhas=0):
	dicionario_musical = {"artista":artist.title(), "album":album.title()}

	if trilhas > 0:
		dicionario_musical["trilhas"] = trilhas

	return(dicionario_musical)



album = make_album('metallica', 'ride the lightning',8)
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)


a = ("p" * 2) * 3
b = ("p" * 3) * 2
print(a == b)



lista = ["Fabio", "Jorge", "de", "Souza", "Pereira"]
x = "TESTE"
a = "BOA"
print("   ".join(lista))



import colorama

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

print('\033[31m' + 'some red text')
print('\033[39m')



a = True
b = False

print( a and b )

#print(bool(a))
#print(bool(b))
#print(bool(c))



def descricao_pet(nome_animal, tipo_animal="cachorro"):
	print(f"\nEu tenho um {tipo_animal}.")
	print(f"Meu {tipo_animal} se chama {nome_animal.title()}.")

descricao_pet("jhony")
#descricao_pet(nome_animal="fred",tipo_animal="tartaruga")




def descricao_pet(nome_animal,  idade_animal, tipo_animal="cachorro"):
	print(f"\nEu tenho um {tipo_animal}.")
	print(f"Meu {tipo_animal} se chama {nome_animal.title()} e ele tem {idade_animal} anos.")

descricao_pet("jhony",12)
#descricao_pet(nome_animal="fred",tipo_animal="tartaruga")


def saudacao(username):
	print(f"Olá {username}. Seja bem vindo ! ")


saudacao(15)



dicionario = dict()

check_001 = True

while check_001 :
	chave = input("\nDigite o seu nome : ")
	valor = input("Digite sua idade : ")

	dicionario[chave] = valor

	prompt = "\nDeseja continuar ?"
	prompt += "\nResponda 'sim' ou 'não' : "
	continua = input(prompt)

	if continua == "sim":
		check_001 = True
	else :
		check_001 = False

print("Imprimindo o dicionário :")
for chave, valor in dicionario.items():
	print(f"CHAVE : {chave}",end=" ")
	print(f"VALOR : {valor}")

print(dicionario)




lista_de_resposta = {}

check_001 = True

while check_001 == True:
	nome = input(f"Qual o seu nome ? ")
	resposta = input(f"Qual sua cor favorita {nome.title()} ? ")
	lista_de_resposta[nome] = resposta

	continua_001 = input("Deseja continuar o cadastro ? [sim / nao]")
	if continua_001 == "nao":
		check_001 = False
	else:
		check_001 = True

print(f"\nRESULTADOS :")

for chave, valor in lista_de_resposta.items():
	print(f"A cor favorita de {chave.title()} é {valor.upper()}.")

print(lista_de_resposta)



usuarios_sem_cadastro = ["1", "2", "3", "4", "5", "6", "7", "8"]
usuarios_confirmados = list()

while len(usuarios_sem_cadastro) != 0 :
	usuario_atual = usuarios_sem_cadastro.pop()
	print(f"Verificando usuário : {usuario_atual.title()}.")
	usuarios_confirmados.append(usuario_atual)

print(f"\nUsuários confirmados :")
usuarios_confirmados.sort()

for nome in usuarios_confirmados:
	print(nome.title())



numero = 0
while numero < 10 :
	numero += 1
	if numero % 2 == 0:
		continue
		print("Este trecho não será exibido por conta do continue...")
	print(numero)



from time import sleep\

contador_001 = 0
contador_002 = 1

while contador_001 < 5 :
	print(contador_001,end=" ")
	contador_001 += 1
	#if contador_001 == 3:
		#break

	while contador_002 <= 10 :
		#sleep(0.25)
		if contador_002 >= 5:
			print("Chegou no 5")
			contador_002 += 1
			break
			break

		else :
			print("\033[1;34m", contador_002, "\033[m", end=" ")
			contador_002 += 1

print("Chegou no 3 primeiro while")


prompt = "\nDigame alguma coisa e eu irei repetir."
prompt += "\nDigite 'quit' para sai : "

continua = True
while continua == True :
	message = input(prompt)
	if message == "quit" :
		continua = False
	else:
		print(message)


prompt = "\nDigame alguma coisa e eu irei repetir."
prompt += "\nDigite 'quit' para sai : "

message = ""
while message != "quit" :
	message = input(prompt)
	if message == "quit" :
		break
	else:
		print(message)


numero = 1
while numero <= 5:
	print(numero, end=" ")
	numero += 1


idade = input("Digite sua idade : ")
print(idade)
print(type(idade))


prompt = "Se você nos disser seu nome, poderemos conversar melhor."
prompt += "\nRsponda a questão abaixo."
prompt += "\nQual seu nome : "
name = input(prompt)
print(f"Olá {name} !")


linguagens_favoritas = {
	"fabio": ["python", "c++", "visual basic"],
	"mario": ["python"],
	"carlos": ["html"],
	"pereira": ["pascal"],
	"jhony": ["pascal","C"],
	"jorge": ["python", "pascal"],
	}

for chave, valor in linguagens_favoritas.items():
	if len(valor) > 1:
		print(f"O programador {chave.title()} gosta de várias linguagens :")
		for cada_linguagem in valor:
			print(f"\t{cada_linguagem}")
	else :
		print(f"\nO programador {chave.title()} tem apenas uma linguagem favorita :")
		for cada_linguagem in valor:
			print(f"\t{cada_linguagem}")




linguagens_favoritas = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}
for values in linguagens_favoritas.values():
	print(values.title())

pizza = {"massa":"grossa", "ingredientes":["queijo", "tomate", "camarão"]}
print(f"Foi feito o pedido de uma pizza com massa \033[1;34m{pizza['massa']}\033[m e com os seguintes ingredientes :")

for ingredientes in pizza["ingredientes"]:
	print(ingredientes)


friends = ["phil", "sarah"]

for name in linguagens_favoritas.keys():
	print(name.title())
	if name in friends:
		print(f"Ola {name}. Vi que sua linguagem favorita é : {linguagens_favoritas[name].title()}")

print(linguagens_favoritas.keys())
print(linguagens_favoritas.values())
print(linguagens_favoritas.items())

for name in sorted(linguagens_favoritas.keys()):
	print(name)


user_0 = {"username" : "efermi" , "first" : "enrico" , "last" : "fermi"}

for k, v in user_0.items():
	print("\nKEY : " + k)
	print("Value :" + v)



dicionario = {
	"fabio":"Python",
	"pereira":"c",
	}
print(dicionario)


lista_1 = [11,2,23]
lista_2 = [2,11,23]
print(lista_1 == lista_2)


def x (val):
	val[0] = 45


val = [2,4,6]
x(val)
print(val)

lista = [1,2,3,4,5,6,7,8,9,0,]
print(lista[-3:])

lista_quadrados = list()
for valor in range (1, 11) :
	quadrados = valor ** 2
	lista_quadrados.append(quadrados)

print(lista_quadrados)


motocicletas = ["honda", "yamaha", "suzuki"]
print(motocicletas)
motocicletas.sort(reverse=True)
motos_caras = "suzuki"
motocicletas.remove(motos_caras)
print(motocicletas)
motos_caras = "honda"
motocicletas.remove(motos_caras)
print(motocicletas)
print(len(motocicletas))


motocicletas = ["honda","yamaha","suzuki"]
print(motocicletas)
moto_pop = motocicletas.pop()
print(motocicletas)
print(moto_pop)

motocicletas = ["honda","yamaha","suzuki"]
print(motocicletas)
del motocicletas[0]
print(motocicletas)
del motocicletas[1]
print(motocicletas)


import time

inicio = int(input("Digite o valor máximo : "))
fim = 0

for contador in range(inicio, fim-1, -1):
	if contador == inicio :
		print(contador)
	else:
		time.sleep(1)
		print(contador)

print("\nTempo encerrado !")


x = 0
for count in universo :
	print("contador", count)
	if count == universo[x]:
		print(f"\033[1;34m{count} \033[m")
	else:
		print(f"{count}")
	x = x + 3



for l in "fabio":
	if l == "b":
		print(l)
		print(f"A letra 'b' está presente...")
	else:
		print(l)
print("FIM")


for count in range(10):
	print(count)

A = "FABIO"
C = "PEREIRA"

lista = [A,"B",C]
print(lista)

lista.pop()

print(lista)

for i in range(3):
	print("INICIO DE I")
	print(f"i =",i)
	print("FIM DE I")
	for j in range(i):
		print("INICIO DE J")
		print(f"i = ",i,"j = ",j)
		if i == j:
			print("RESULTADO :")
			print(i,end="")
		print("FIM DE J")


mydict = {'a':1,'b':2,'c':3}
print(mydict['a'])
print(mydict.keys())
print(mydict.values())
print(mydict.items())


l1 = [10,20,30,40,50]
l2 = [10,20,30,40,50]

l2.append(60)
l1 = l2

print( l1 == l2 )
print( l1 is l2 )

print(f"LISTA 1",l1 )
print(f"LISTA 2",l2 )

for i in range ( 5 ):
	print( i, end= '' )
	if i == 1:
		continue
else:
	print("end")


l1 = [10,20,30]
l2 = l1

l1[0] = "y"
l2[1] = "x"

print(f"LISTA 1 {l1}\nLISTA 2 {l2}")

l1 = [10,20,30]
l2 = l1[:]
l2[1] = "x"
print(f"LISTA 1 {l1}\nLISTA 2 {l2}")

while continua_001 == True:
	print(f"{'MENU PRINCIPAL':<45}")
	esc_001 = str(input("\nDigite uma opção : "))

	if esc_001 == "1":
		cadastrar()

	elif esc_001 == "2":
		consultar()

	elif esc_001 == "3":
		remover()

	elif esc_001 == "9":
		continua_002 = True
		while continua_002 == True:
			esc_002 = str(input("Deseja sair do programa [ S / N ] ? ")).strip().lower()[0]
			if esc_002 == "s":
				continua_001 = False
				continua_002 = False

			elif esc_002 == "n":
				continua_001 = True
				continua_002 = False

			else:
				print("Opção inválida !")
				continua_001 = True
				continua_002 = True

def soma(* valores):
	s = count = 0
	while count < len(valores):
	#for x in valores:
		s = s + valores[count]
		count +=1
	print(f"A soma dos valores {valores} é igual a {s}")

soma(1,5,8,9)



def dobravalor(lista):
	count = 0
	while count < len(lista) :
		lista[count] = lista[count] * 2
		print(lista[count])
		count+=1

exemplo = [4,10,40,1,0,100]
dobravalor(exemplo)
print(exemplo)

def dobrar(lst) :
	item = 1
	while item < len(lst) :
		lst[item] = lst[item]*2
		item = item + 1

lista = [1,2,3,4,5,6,7,8,9]
dobrar(lista)

print(lista)


def soma(a, b):
	print(f"A = {a} e B = {b}")
	s = a + b
	print(f"\nA soma A + B = {s}")

#Programa Principal


soma(4, 5)
soma(8, 9)
soma(2, 1)


x = ["Fabio"]
y = ["Pereira"]

count

print("{:^20}".format(x))

print(f'{count:^5}{cadastro[count][0]:^15}{cadastro[count][2]:^7}')
# print("{:<5}{:<15}{:<5}".format(count+1,cadastro[count][0],cadastro[count][2]))
print(f'{count + 1:^5}{cadastro[count][0]:^15}{cadastro[count][2]:^5}')


dado = list()
pessoas = list()

for count in range ( 0 , 3 ) :
	dado.append(str(input("Digite o nome da pessoa : ")))
	dado.append(int(input("Digite a idade da pessoa : ")))
	pessoas.append(dado[:])
	dado.clear()

print(pessoas)

lista_3 = [ ["Fabio",40], ["Jorge",50], ["Souza",60], ["Pereira",70], ["JHONY",12] ]
print(lista_3[0][0])
print(lista_3[1][1])
print(lista_3[2][0])
print(lista_3[3][1])
print(lista_3[4][0])

lista = ["A","B","C","D","E"]
lista.append("Fabio")
lista.append("Jorge")
lista.append(("de"))
lista.append("Souza")
print(len(lista))
print(f"LISTA antes do APPEND: {lista}")

lista[0] = 0
lista[1] = 1
lista[2] = 2
lista[3] = 3

print(f"LISTA : {lista}")

lista_2 = [10,11,12]
lista_2.append(lista)
lista_2.append("FIM")
print(f"LISTA_2 : {lista_2}")



lista = ["a","A","B"]
print(lista)
lista.sort()

print(lista)


lista = []


for count in range ( 1, 6) :
	lista.append(int(input("Insira um numero : ")))

item_atual = 44
print(lista)
print(f"Tamanho da lista : {len(lista)}")

lista.insert(len(lista)-5, item_atual)

print(lista[0])


for count in range ( 5, 11 ) :
	print(count)
	lista.append(count)
	print(lista)
	print(lista[count])
	print(lista)
	print("-----")




mylist = ["python","hub"]
for i in mylist :
	mylist.append(i.upper())

print(mylist)
x = 11

for count in range(x):
	print(f"Numero do loop : {count}")

print("FIM")




for i in range(0,2):
	#print(i)
	x = x - 2
	print(x)



lanche = ("hamburguer","Suco","Pizza","Pudim","Batata Frita")
#for c in range(0,len(lanche)):
#	print(f"Eu comi : {lanche[c]}")

for pos, comida in enumerate(lanche):
	print(f"Eu vou comer {comida} na posição {pos}")



n = input("Digite algo : ")
if n[0] in 'aeiou':
	print("VOGAL")
else:
	print("NAO VOGAL")



import random

print("\n")
print("*** PARTE LISTA 0 ***")

frase = str("Fabio Pereira").split()  # Divide a string em uma lista
print(frase)
x = "".join(frase)  # Retirando os espaços em branco
print(x)
lista_0 = []
lista_0[len(lista_0):] = x
print(len(lista_0))
print(lista_0)

lista_0.append(x)
print(lista_0)
y = "".join(lista_0)
print(y)
z = lista_0
print(z)

print("\n")
print("*** PARTE LISTA 1 ***")
lista_1 = ['','','X','Y']

lista_1[1] = "Z"
lista_1.append("FABIO")
print(lista_1)
print(len(lista_1))
print(lista_1[0:1])
print(lista_1)
#lista_1[len(lista_1):] = "LAPTOP"
lista_1[5:] = "LAPTOP"
print(lista_1)
lista_1[len(lista_1):] = ["TESTE"] # Com os colchetes a string "TESTE" é inserida e não char a char.
print(lista_1)
print(len(lista_1))

print("\n")
print("*** PARTE LISTA 2 ***")

lista_2 = [6,7,8]
lista_3 = lista_0 + lista_1 + lista_2
print(f"Lista Geral : {lista_3}")

conjunto_1 = {1,2,3}
conjunto_2 = {2,3,"a","b"}
print(conjunto_1)
print(conjunto_2)

conjunto_1.update(conjunto_2)
print(f"Resultado do Update no conjunto_1 com Conjunto_2 : {conjunto_1}")

print(f"Lista_3 antes do embaralhamento : {lista_3}")
random.shuffle((lista_3))

print(f"Resultado do random no conjunto : {lista_3}")


#print(lista_1[0])
#print(lista_3[0])

#lista_1.append(50)
#print(lista_1)


# lista_1.replace(lista_1[0],lista_3[1])
# print(lista_1)


# lists[0].append(3)
"""
