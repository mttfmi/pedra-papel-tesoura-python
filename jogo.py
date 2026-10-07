import getpass
import os

def limpar_tela():
    os.system("cls")

def mostrar_placar(vit1, vit2):
    print(f"Vitórias do jogador 1: {vit1}")
    print(f"Vitórias do jogador 2: {vit2}")

def verificar_As_jogadas(jogada1, jogada2):
    if jogada1 == jogada2:
        return 'Empate'
    if (jogada1 == 'pedra' and jogada2 == 'tesoura'
            or jogada1 == 'tesoura' and jogada2 == 'papel'
            or jogada1 == 'papel' and jogada2 == 'pedra'):
        return 'Jogador 1 ganhou'
    else:
        return 'Jogador 2 ganhou'

def verificar_qm_ganhou(vitoria1, vitoria2):
    if vitoria1 == 3:
        return (f"*****PARABÉNS, JOGADOR 1 GANHOU!!*****"
                f"\nPLACAR:\nVitórias do jogador 1: {vitoria1}"
                f"\nVitórias do jogador 2: {vitoria2}")

    return (f"*****PARABÉNS, JOGADOR 2 GANHOU!!*****"
            f"\nPLACAR:\nVitórias do jogador 1: {vitoria1}"
            f"\nVitórias do jogador 2: {vitoria2}")

def resposta_valida(jogar_dnv):
    opcoes_validas_verificação = ('s', 'n')
    if jogar_dnv in opcoes_validas_verificação:
        return True
    return False
while True:
    opcoes_validas = ('pedra', 'papel', 'tesoura')
    vitjogador1 = 0
    vitjogador2 = 0

    while vitjogador1 < 3 and vitjogador2 < 3:
        print('\n--- ADEDONHA JOGO ---\n')

        jogada1 = getpass.getpass(
            'Digite sua jogada primeiro jogador: ')
        jogada1 = jogada1.lower().replace(" ", "")
        jogada2 = getpass.getpass(
            'Digite sua jogada segundo jogador: ')
        jogada2 = jogada2.lower().replace(" ", "")

        if jogada1 in opcoes_validas and jogada2 in opcoes_validas:
            pass
        else:
            limpar_tela()
            print('Digite apenas pedra, papel ou tesoura.')
            continue
        resultado_rodada = verificar_As_jogadas(jogada1, jogada2)

        if resultado_rodada == 'Jogador 1 ganhou':
            vitjogador1 += 1
        elif resultado_rodada == 'Jogador 2 ganhou':
            vitjogador2 += 1

        limpar_tela()
        print(resultado_rodada)
        mostrar_placar(vitjogador1, vitjogador2)
    limpar_tela()
    print(verificar_qm_ganhou(vitjogador1, vitjogador2))

    while True:
        jogar_dnv = input('\nJogar de novo? (s/n): ')
        jogar_dnv = jogar_dnv.lower().replace(" ", "")
        resposta_valida_funç = resposta_valida(jogar_dnv)

        if resposta_valida_funç == True:
            break
        else:
            limpar_tela()
            print('Digite apenas s/n')

    if jogar_dnv == 's':
        limpar_tela()
    else:
        print('programa finalizado')
        break
