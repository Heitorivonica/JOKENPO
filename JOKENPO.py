import random #importando a biblioteca random para escolhas aleatorias
import os     #importanto a biblioteca os para limpar a tela
import time   #importando a biblioteca time para pausas no jogo

def limpar_tela():  #criando a função para limpar o console depois das jogadas
    os.system("cls" if os.name == "nt" else "clear")  

def resultado(jogador, computador):   #criando a função para determinar as regras e resultados do jogo
    if jogador == computador:
        return "Empate!"              #se as escolhas forem iguais, é empate
    elif (
        (jogador == "pedra" and computador == "tesoura") or   #utilizando or para definir as condições de vitória do jogador
        (jogador == "tesoura" and computador == "papel") or
        (jogador == "papel" and computador == "pedra")
    ):
        return "Você venceu!"
    else:                                      #se nenhuma das condições anteriores forem atendidas, o computador vence
        return "Computador venceu!"

def jogar():                 #função principal do jogo
    placar = {"vitorias": 0, "derrotas": 0, "empates": 0} #dicionario para armazenar o placar    

    while True:         #loop infinito para o jogo até o jogador decidir sair 
        limpar_tela()
        print("====== JOKENPÔ ======")

        escolha = input("Escolha (pedra, papel, tesoura) ou 'sair': ").lower()

        if escolha == "sair":   #condição para sair do jogo
            print("Obrigado pela jogatina!")
            break

        if escolha not in ["pedra", "papel", "tesoura"]:  #validação da escolha do jogador se não for valida explica que é invalida e volta ao inicio do loop
            print("Escolha inválida!")
            time.sleep(1)
            continue

        # Escolha do computador
        computador = random.choice(["pedra", "papel", "tesoura"])  #escolha aleatoria do computador
         

        print(f"\nVocê escolheu: {escolha}")    #mostra a escolha do jogador
        print(f"Computador escolheu: {computador}") #mostra a escolha do computador

        resultado_jogo = resultado(escolha, computador)    #chama a função resultado para determinar o vencedor
        print(f"\nResultado: {resultado_jogo}")         #mostra o resultado do jogo

        # Atualiza placar
        if resultado_jogo == "Você venceu!":            #atualiza o placar de vitorias,derrotas e empates
            placar["vitorias"] += 1
        elif resultado_jogo == "Computador venceu!":
            placar["derrotas"] += 1
        else:
            placar["empates"] += 1

        print(f"\nPlacar: {placar}")            #mostra o placar atualizado
        time.sleep(2)                            #pausa de 2 segundos antes de reiniciar o loop

jogar() #chama a função jogar para iniciar o jogo